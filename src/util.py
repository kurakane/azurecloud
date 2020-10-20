"""タスク間で共有して使用する共通処理."""

import bz2
import datetime
import os
import pickle
import shutil
import sys
import time

import cfg


def get_env(env):
    """環境変数から値を取得する."""
    if env in os.environ:
        job_id = os.environ[env]
        return job_id

    else:
        print(f'環境変数が設定されていません. 異常終了します. [{env}]')
        sys.exit(-1)


def get_job_id():
    """環境変数からJOB IDを取得する."""
    return get_env('AZ_BATCH_JOB_ID')


def get_task_id():
    """環境変数からTASK IDを取得する."""
    return get_env('AZ_BATCH_TASK_ID')


def get_workdir():
    """環境変数から作業フォルダを取得する."""
    return get_env('AZ_BATCH_TASK_WORKING_DIR')


def get_inputdir():
    """入力ファイルパスを取得する."""
    return cfg.STORAGE_CONTAINER_INPUT + get_job_id()


def get_outputdir():
    """出力ファイルパスを取得する."""
    return cfg.STORAGE_CONTAINER_OUTPUT + get_job_id()


def print_env():
    """デバッグ用に環境変数を出力する."""
    print(f'ノード:[{get_env("AZ_BATCH_NODE_ID")}]')
    print(f'タスクID:[{get_env("AZ_BATCH_TASK_ID")}]')
    print('--')


def print_sec(start_time):
    """デバッグ用に秒数を出力する."""
    print(f'[{(time.time() - start_time):,.3f}] sec')


def print_file_size(file_path):
    """デバッグ用にファイルサイズを出力する."""
    print(f'[{(os.path.getsize(file_path) / 1024 / 1024):,.3f}]  MB')


def load_bz2_file(file_path, file_name):
    """BZ2圧縮されたファイルをloadする."""
    file_path_bz2 = os.path.join(file_path, file_name)

    if not os.path.exists(file_path_bz2):
        print(f'入力ファイルが存在しません. 異常終了します. [{file_path_bz2}]')
        sys.exit(-1)

    with open(file_path_bz2, 'rb') as f:
        # 解凍するために一時ファイルを準備.
        file_path_pickle = os.path.join(get_workdir(), file_name + '.tmp')
        # 解凍した一時ファイルをローカルに書き込む.
        start_time = time.time()
        with open(file_path_pickle, 'wb') as f2:
            print(f'一時ファイルを展開します. [{file_path_pickle}]', end='')
            f2.write(bz2.decompress(f.read()))
        print(' <OK>')
        print_sec(start_time)
        print_file_size(file_path_pickle)

    # 解凍ファイルからloadする.
    start_time = time.time()
    print(f'ファイルをloadします. [{file_path_pickle}]', end='')
    with open(file_path_pickle, 'rb') as f:
        data = pickle.load(f)
        # ローカルの一時ファイルを削除する.
        os.remove(file_path_pickle)

    print(' <OK>')
    print_sec(start_time)
    return data


def upload_bz_file(file_path, file_name, obj):
    """bz圧縮したファイルをアップロードする."""

    # アップロードファイルをローカルに出力する.
    file_path_tmp = os.path.join(get_workdir(), file_name + '.tmp')
    start_time = time.time()
    print(f'ファイルをNodeローカルに出力します. [{file_path_tmp}]', end='')
    with open(file_path_tmp, 'wb') as f:
        pickle.dump(obj, f)
    print(' <OK>')
    print_sec(start_time)
    print_file_size(file_path_tmp)

    # アップロードファイルをBZ2で圧縮する.
    file_path_bz2 = os.path.join(get_workdir(), file_name + '.bz2')
    start_time = time.time()
    print(f'ファイルをBZ2圧縮します. [{file_path_tmp}] -> [{file_path_bz2}]', end='')
    with open(file_path_tmp, 'rb') as f:
        data = f.read()
        with open(file_path_bz2, 'wb') as f2:
            f2.write(bz2.compress(data))
    print(' <OK>')
    print_sec(start_time)
    print_file_size(file_path_bz2)

    # BZ2ファイルをAzureStorageにアップロード(コピー)する.
    fil_path_output = os.path.join(file_path, file_name + '.bz2')
    if not os.path.exists(file_path):
        os.mkdir(file_path)

    start_time = time.time()
    print(f'ファイルをAzureStorageへコピーします. [{file_path_bz2}] -> [{fil_path_output}]', end='')
    shutil.copy(file_path_bz2, fil_path_output)
    print(' <OK>')
    print_sec(start_time)

    # ローカルの一時ファイルを削除する.
    print(f'一時ファイルを削除します. [{file_path_tmp}]', end='')
    os.remove(file_path_tmp)
    print(' <OK>')
    print(f'一時ファイルを削除します. [{file_path_bz2}]', end='')
    os.remove(file_path_bz2)
    print(' <OK>')
