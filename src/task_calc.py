"""計算のTaskのモジュール."""

import os

import pandas as pd

import cfg
import dummy
import util


def run():

    util.print_env()

    # 休日情報を復元する.
    holidays = util.load_bz2_file(util.get_inputdir(), cfg.FILE_HOLIDAYS + '.bz2')
    print(holidays.dump())

    # 約定データを復元する.
    spl_treads = util.load_bz2_file(util.get_inputdir(), cfg.FILE_TRADES + '.bz2')
    print(f'明細数. [{len(spl_treads)}]')

    # 出力先のフォルダを生成する.
    path_output = os.path.join(util.get_outputdir(), util.get_task_id())
    os.makedirs(path_output)
    # 出力ファイルパスを生成する.
    path_output_npv = os.path.join(path_output, cfg.FILE_NPV)

    # ★NPVファイルを模倣.
    df = pd.DataFrame([], columns=['TradeNo', 'NPV', 'Message'], index=range(len(spl_treads)))

    # 約定データからcsvファイルを出力する.
    for i, spl_trade in enumerate(spl_treads):
        spl_trade.dump()
        row = ['T' + str(i + 1).zfill(8), spl_trade.datas[0], len(spl_trade.datas)]
        df.iloc[i,:] = row
    df.to_csv(path_output_npv, index=False)

    print('正常終了しました.')


run()
