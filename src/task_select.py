"""約定データを取得するTaskのモジュール."""

import cfg
import dummy
import util


def run():

    util.print_env()

    # 検索条件を復元する.
    condition = util.load_bz2_file(util.get_inputdir(), cfg.FILE_SELECT + '.bz2')
    print(condition.dump())

    print('約定データを検索します.')
    # ★ダミーデータ作成. ここで検索を行う.
    spl_trades = []
    for i in range(condition.count):
        spl_trades.append(dummy.SplTrade(condition.data_count))

    # 約定データを格納する.
    util.upload_bz_file(util.get_inputdir(), cfg.FILE_TRADES, spl_trades)

    print('正常終了しました.')


run()
