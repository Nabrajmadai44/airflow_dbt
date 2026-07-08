from airflow.decorators import dag, task
from airflow.operators.trigger_dagrun import TriggerDagRunOperator
from pendulum import datetime


@dag(
    dag_id="master_dag",
    schedule="@daily",
    start_date=datetime(2026, 6, 29),
    catchup=False,
    tags=["master", "orchestration"],
)
def master_dag():

    @task
    def ingest_data():
        """
        Simulates extracting data from a source system
        and loading it into the Bronze layer.
        """
        print("Ingesting source data...")

        rows = [
            {"id": 1, "value": "a"},
            {"id": 2, "value": "b"}
        ]

        print(f"Ingested {len(rows)} rows")
        return len(rows)

    trigger_dbt_learn = TriggerDagRunOperator(
        task_id="trigger_dbt_learn_cosmos",
        trigger_dag_id="dbt_learn_cosmos",
        wait_for_completion=True,
        poke_interval=30,
        reset_dag_run=True,
        deferrable=False,
    )

    @task
    def end():
        print("Master DAG completed successfully.")
        print("Data ingestion and dbt transformations finished.")

    ingest_data() >> trigger_dbt_learn >> end()


master_dag()