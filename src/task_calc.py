# 計算のTaskのモジュール.

import os

import cfg
import util

def run():
    # JOB IDを取得する.
    job_id = util.get_job_id()
    # 入力ファイルのパスを生成する. JOB IDをそのままディレクトリとする.
    input_file_path = cfg.STORAGE_CONTAINER_INPUT + job_id

    # 休日情報を復元する.
    holidays = util.load_bz2_file(os.path.join(input_file_path, cfg.FILE_HOLIDAYS + '.bz2'))
    print(holidays.dump())

    print('calc')


run()
