# 約定データを取得するTaskのモジュール.

import os

import cfg
import util


def run():

    # JOB IDを取得する.
    job_id = util.get_job_id()
    # 入力ファイルのパスを生成する. JOB IDをそのままディレクトリとする.
    input_file_path = cfg.STORAGE_CONTAINER_INPUT + job_id

    # 検索条件を復元する.
    condition = util.load_bz2_file(os.path.join(input_file_path, cfg.FILE_SELECT + '.bz2'))
    print(condition.dump())

    print('約定データを検索します.')

    print('約定データをAzureStorageに格納します.')


run()
