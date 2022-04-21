import datetime
from email.policy import default
from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from datetime import dattetime, timedelta

default_args = {
    'owner' : 'airflow',
    'depends_on_past' : False,
    'start_date' : datetime(2022,1,1),
    'email_on_failure' : False,
    'email_on_retry' : False,
    'retries' : 0,
    'retry_delta' : timedelta(seconds=5)
} 


dag = DAG(
    dag_id = " NAME OF THE DAG "
    description = 'description of the dag'
    schedule_interval = '* * * * *'
    max_active_runs = 1
    default_args = default_args
)

step1 = check_size = BashOperator(
    task_id = 'check_size',
    bash_command = "entery the bash command",
    dag=dag
)
 
step2 = check_size2 = BashOperator(
    task_id = 'check_size',
    bash_command = "entery the bash command",
    dag=dag
)
 
step3 = check_size3 = BashOperator(
    task_id = 'check_size',
    bash_command = "entery the bash command",
    dag=dag
) 
 
step1 >> step2 >> step3
    
}
