from datetime import datetime, timedelta

from airflow.models import DAG, BaseOperator

try:
    from airflow.operators.empty import EmptyOperator
except ModuleNotFoundError:
    from airflow.operators.dummy import DummyOperator as EmptyOperator  # type: ignore
from airflow.providers.microsoft.azure.operators.data_factory import AzureDataFactoryRunPipelineOperator
from airflow.providers.microsoft.azure.sensors.data_factory import AzureDataFactoryPipelineRunStatusSensor
from airflow.utils.edgemodifier import Label

with DAG(
    dag_id="run_adf_pipeline_SamplePipeline",
    start_date=datetime(2023, 4, 17),
    schedule_interval="@daily",
    catchup=False,
    default_args={
        "retries": 1,
        "retry_delay": timedelta(minutes=3),
        "azure_data_factory_conn_id": "airflow-davew", #This is a connection created on Airflow UI
        "factory_name": "airflow-davew",  # This can also be specified in the ADF connection.
        "resource_group_name": "rgadfWorkshop",  # This can also be specified in the ADF connection.
    },
    default_view="graph",
) as dag:
    begin = EmptyOperator(task_id="begin")
    end = EmptyOperator(task_id="end")

    # [START howto_operator_adf_run_pipeline]
    run_pipeline1: BaseOperator = AzureDataFactoryRunPipelineOperator(
        task_id="run_pipeline1",
        pipeline_name="SamplePipeline" #, 
        #parameters={"myParam": "value"},
    )
    # [END howto_operator_adf_run_pipeline]

    # [START howto_operator_adf_run_pipeline_async]
 #   run_pipeline2: BaseOperator = AzureDataFactoryRunPipelineOperator(
 #       task_id="run_pipeline2",
 #       pipeline_name="<PipelineName>",
 #       wait_for_termination=False,
 #   )

 #   pipeline_run_sensor: BaseOperator = AzureDataFactoryPipelineRunStatusSensor(
 #       task_id="pipeline_run_sensor",
 #       run_id=run_pipeline2.output["run_id"],
 #   )
    # [END howto_operator_adf_run_pipeline_async]

    begin >> Label("No async wait") >> run_pipeline1
    #begin >> Label("Do async wait with sensor") >> run_pipeline2
    [run_pipeline1] >> end

    # Task dependency created via `XComArgs`:
    #   run_pipeline2 >> pipeline_run_sensor