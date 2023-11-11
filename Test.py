
import datetime

from airflow import DAG
from airflow.operators.empty import EmptyOperator

with DAG(
     dag_id="my_dag_name",
     start_date=datetime.datetime(2023, 11, 11),
     schedule="@daily",
):
     EmptyOperator(task_id="task")
