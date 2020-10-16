"""タスク間で共有して使用する共通処理."""

import pickle
import sys
import os
import bz2
import cfg


def get_env(env):
    if env in os.environ:
        job_id = os.environ[env]
        return job_id

    else:
        print(f'環境変数が設定されていません. 異常終了します. [{env}]')
        sys.exit(-1)


def get_job_id():
    """環境変数からJOB IDを取得する."""
    return get_env('AZ_BATCH_JOB_ID')


def get_workdir():
    """環境変数から作業フォルダを取得する."""
    return get_env('AZ_BATCH_TASK_WORKING_DIR')


def load_bz2_file(file_path):
    """BZ2圧縮されたファイルをloadする."""
    if not os.path.exists(file_path):
        print(f'入力ファイルが存在しません. 異常終了します. [{file_path}]')
        sys.exit(-1)

    with open(file_path, 'rb') as f:
        # 解凍するためにファイルパスのファイル名を変更.
        file_path_pickle = os.path.join(get_workdir(), cfg.FILE_TMP)
        # 解凍した一時ファイルをローカルに書き込む.
        with open(file_path_pickle, 'wb') as f2:
            f2.write(bz2.decompress(f.read()))
    
    # 解凍ファイルからloadする.
    with open(file_path_pickle, 'rb') as f:
        data = pickle.load(f)

        # ローカルの一時ファイルを削除する.
        os.remove(file_path_pickle)

        return data


def dump_env():
    for env in os.environ:
        if 'AZ_' in env:
            print(env)
