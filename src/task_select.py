# 約定情報を取得するTaskの為のモジュール.

import os
import pickle
import sys

# 検索条件のファイル名.
FILE_SELECT = 'condition.txt'

def run():

    job_id = ''
    if 'AZ_BATCH_JOB_ID' in os.environ:
        job_id = os.environ["AZ_BATCH_JOB_ID"]
        print(f'JOB ID:{job_id}')

    else:
        print(f'環境変数が設定されていません. 異常終了します. [AZ_BATCH_JOB_ID]')
        sys.exit(-1)

    # JOB IDをそのままディレクトリとする.
    file_name = os.path.join(job_id, FILE_SELECT)
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
