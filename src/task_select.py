# 約定データを取得するTaskのモジュール.

import os

import azure.storage.blob as azureblob

import cfg
import util
import dummy
import pickle


def run():

    # JOB IDを取得する.
    job_id = util.get_job_id()
    # 入力ファイルのパスを生成する. JOB IDをそのままディレクトリとする.
    input_file_path = cfg.STORAGE_CONTAINER_INPUT + job_id

    # 検索条件を復元する.
    condition = util.load_bz2_file(os.path.join(input_file_path, cfg.FILE_SELECT + '.bz2'))
    print(condition.dump())

    print('約定データを検索します.')
    spl_trades = []
    for i in range(100):
        spl_trades = dummy.SplTrade()

    print('約定データをAzureStorageに格納します.')
    # AzureStorageのクライアントを生成する.
    blob_service_client = azureblob.BlockBlobService(
        account_name=cfg.STORAGE_ACCOUNT_NAME, account_key=cfg.STORAGE_ACCOUNT_KEY)

    # アップロードファイルをローカルに出力する.
    with open(cfg.FILE_TMP, 'wb') as f:
        pickle.dump(object, f)

    print(blob_service_client)


run()
