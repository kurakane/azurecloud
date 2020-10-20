"""集約するTaskのモジュール."""

import os
import sys

import pandas as pd

import cfg
import util


def run():

    util.print_env()

    # コマンドライン引数を受け取る.
    args = sys.argv

    for arg in args:
        # NPVファイルを読込する.
        path_npv = os.path.join(util.get_outputdir(), arg, cfg.FILE_NPV)
        print(f'NPVファイルを読込します [{path_npv}]')
        df = pd.read_csv(path_npv)
        print(df.info())

    print('正常終了しました.')

run()
