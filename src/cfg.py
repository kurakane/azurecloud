# 各種定義ファイル.

# 入力ファイルのAzureStorageコンテナ名.(パス形式)
STORAGE_CONTAINER_INPUT = '/data-in/'
# 出力ファイルのAzureStorageコンテナ名.(パス形式)
STORAGE_CONTAINER_OUTPUT = '/data-out/'

# 休日情報のファイル名. (クライアント側と合わせること)
FILE_HOLIDAYS = 'Holidays'
# 検索条件のファイル名. (クライアント側と合わせること)
FILE_SELECT = 'ObsTradeQueryBuilder'
# 明細のファイル名. (クライアント側と合わせること)
FILE_TRADES = 'SplTrades'

# NPVファイル名.
FILE_NPV = 'npv.csv'

# -- 以下タスク生成用定義. 後ほど削除 --
# コンテナのURL.
CONTAINER_URL = 'yamayamaregistory.azurecr.io'
# Pythonのコンテナ名.
CONTAINER_PY_NAME = '/azurecloud:latest'
# アップロード先のAzureStorageコンテナ名.
STORAGE_CONTAINER_UPLOAD = 'data-in'
# ダウンロード先のAzureStorageコンテナ名.
STORAGE_CONTAINER_DOWNLOAD = 'data-out'
# Pythonコンテナ接続時のオプション.
CONTAINER_PY_OPT = '--workdir /app --volume /mnt/data-in:/' + STORAGE_CONTAINER_UPLOAD + ' --volume /mnt/data-out:/' + STORAGE_CONTAINER_DOWNLOAD
# AzureBatchのバッチアカウント名.
BATCH_ACCOUNT_NAME = 'yamayamabatch'
# AzureBatchのアクセスキー.
BATCH_ACCOUNT_KEY = 'Ko5u/RSuisLs/D4KnrS0m/DHzh07TaILWqw94kO4RXv6A2ylh2dtLOEmm6zVdr8OrCmVjsap7yTul4mKhpdeBw=='
# AzureBatchのアカウントURL
BATCH_ACCOUNT_URL = 'https://yamayamabatch.westus.batch.azure.com'
# Taskテスト.
TASK_ID_TASK_TEST= 't_task_test_'
# Taskテストのファイル名.
TASK_TEST_APP = 'echo.py'