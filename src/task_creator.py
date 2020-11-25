import cfg
import sys
import datetime
import time
import azure.batch.batch_auth as batch_auth
import azure.batch._batch_service_client as batch
import azure.batch.models as batchmodels
import azure.storage.blob as azureblob

def setting_container():
    """TaskContainerSettingsを生成する."""
    return batch.models.TaskContainerSettings(
        image_name=cfg.CONTAINER_URL + cfg.CONTAINER_PY_NAME,
        container_run_options=cfg.CONTAINER_PY_OPT)

def eval_task_status(task_return):
    """Taskの投入結果を判定する."""
    for result in task_return.value:
        # print(f'[{result.task_id}] [{result.status}]')
        if result.status != batchmodels.TaskAddStatus.success:
            raise RuntimeError("TASKの投入に失敗しました")

def create_task(client, job_id):
    """
    Task作成用のTASKを投入する.
    """
    command = 'python ' + cfg.TASK_TEST_APP

    task_ids = []
    tasks = []

    for i in range(3):
        # TASK IDを作成する.
        task_id = cfg.TASK_ID_TASK_TEST + str(i).zfill(3)
        task_ids.append(task_id)
        # TASKを生成する.
        task = batch.models.TaskAddParameter(
                id=task_id,
                command_line=command,
                container_settings=setting_container()
                )
        tasks.append(task)

    # TASKをJOBに追加する.
    print(f'TASKを投入します [{len(task_ids)}]', end='')
    result = client.task.add_collection(job_id, tasks)
    eval_task_status(result)
    print(f' <OK>')

def run():
    credentials = batch_auth.SharedKeyCredentials(
        cfg.BATCH_ACCOUNT_NAME, cfg.BATCH_ACCOUNT_KEY)
    client = batch.BatchServiceClient(
        credentials, batch_url=cfg.BATCH_ACCOUNT_URL)

    job_id = sys.argv

    create_task(client, job_id)


run()