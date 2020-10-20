"""集約するTaskのモジュール."""

import sys

import util


def run():

    util.print_env()

    # コマンドライン引数を受け取る.
    args = sys.argv

    for arg in args:
        print(arg)

    print('正常終了しました.')

run()
