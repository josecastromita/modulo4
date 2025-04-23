from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime

with DAG('hola_mundo', start_date=datetime(2023, 1, 1), schedule_interval='@daily', catchup=False) as dag:
    tarea = BashOperator(
        task_id='imprimir_mensaje',
        bash_command='echo "Hola mundo desde Airflow!"'
    )