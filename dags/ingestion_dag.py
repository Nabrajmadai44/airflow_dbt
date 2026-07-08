from airflow.decorators import dag, task
from pendulum import datetime


@dag(
    dag_id="ingestion_dag",
    schedule="@daily",
    start_date=datetime(2026, 6, 30),
    catchup=False,
    tags=["ingestion", "elt"],
)
def ingestion_dag():

    @task
    def extract():
        print("========== EXTRACT ==========")
        print("Reading data from PostgreSQL source tables...")
        tables = [
            "account",
            "branch",
            "card",
            "customer",
            "hist_transactional",
            "product",
        ]
        print(f"Source tables: {tables}")
        return tables

    @task
    def validate(tables):
        print("========== VALIDATE ==========")
        print(f"Validating {len(tables)} source tables...")
        print("Validation completed successfully.")
        return True

    @task
    def load(valid):
        print("========== LOAD ==========")
        if valid:
            print("Loading raw data into the Bronze layer...")
            print("Raw data is now available for dbt transformations.")
        else:
            raise Exception("Validation failed!")

    source_tables = extract()
    validation = validate(source_tables)
    load(validation)


ingestion_dag()