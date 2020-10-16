"""タスク間で共有して使用する共通処理."""

import pickle
import sys
import os
import bz2


def get_job_id():
    """環境変数からJOB IDを取得する."""
    if 'AZ_BATCH_JOB_ID' in os.environ:
        job_id = os.environ["AZ_BATCH_JOB_ID"]
        return job_id

    else:
        print(f'環境変数が設定されていません. 異常終了します. [AZ_BATCH_JOB_ID]')
        sys.exit(-1)


def load_bz2_file(file_path):
    """BZ2圧縮されたファイルをloadする."""
    if not os.path.exists(file_path):
        print(f'入力ファイルが存在しません. 異常終了します. [{file_path}]')
        sys.exit(-1)

    with open(file_path, 'rb') as f:
        # 解凍するためにファイル名を変更.
        file_path_pickle = file_path.replace('.bz2', '.dmp')
        # 解凍ファイルを書き込む.
        with open(file_path_pickle, 'wb') as f2:
            f2.write(bz2.decompress(f.read()))
    
    # 解凍ファイルからloadする.
    with open(file_path_pickle, 'rb') as f:
        data = pickle.load(f)
        return data
