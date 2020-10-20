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

    for i, arg in enumerate(args):
        # NPVファイルを読込する.
        if i:
            path_npv = os.path.join(util.get_outputdir(), arg, cfg.FILE_NPV)
            print(f'NPVファイルを読込します [{path_npv}]')
            df = pd.read_csv(path_npv)
            df.info()

    print('正常終了しました.')

run()
