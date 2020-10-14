# 約定データを取得するTaskのモジュール.

import os
import pickle
import sys

import cfg

def run():

    job_id = ''
    if 'AZ_BATCH_JOB_ID' in os.environ:
        job_id = os.environ["AZ_BATCH_JOB_ID"]
        print(f'JOB ID:{job_id}')

    else:
        print(f'環境変数が設定されていません. 異常終了します. [AZ_BATCH_JOB_ID]')
        sys.exit(-1)

    # JOB IDをそのままディレクトリとする.
    file_name = os.path.join('/data-in/' + job_id, cfg.FILE_SELECT)
    print(f'入力ファイル [{file_name}]')

    if not os.path.exists(file_name):
        print(f'入力ファイルが存在しません. 異常終了します. [{file_name}]')
        sys.exit(-1)

    with open(file_name, 'rb') as f:
        condition = pickle.load(f)
        print(condition)

    print('約定データを検索します.')

    print('約定データをAzureStorageに格納します.')


run()
