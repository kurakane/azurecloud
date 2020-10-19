# 計算のTaskのモジュール.

import os

import cfg
import util
import dummy


def run():

    # 休日情報を復元する.
    holidays = util.load_bz2_file(util.get_inputdir(), cfg.FILE_HOLIDAYS + '.bz2')
    print(holidays.dump())

    # 約定データを復元する.
    spl_treads = util.load_bz2_file(util.get_inputdir(), cfg.FILE_TRADES + '.bz2')
    print(f'明細数. [{len(spl_treads)}]')

    # Task IDを取得する.

    # 約定データからcsvファイルを出力する.
    for spl_trade in spl_treads:
        print('XXXXXXXXXXXXXXXXXXXXXXX')

    print('calc')


run()
