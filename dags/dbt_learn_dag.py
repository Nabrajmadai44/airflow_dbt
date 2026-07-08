from cosmos import DbtDag, ProjectConfig, ProfileConfig, ExecutionConfig
from pendulum import datetime
from pathlib import Path

DBT_PROJECT_PATH = Path("/usr/local/airflow/dbt/dbt_learn")

profile_config = ProfileConfig(
    profile_name="dbt_learn",
    target_name="dev",
    profiles_yml_filepath=DBT_PROJECT_PATH / "profiles.yml",
)

dbt_learn_dag = DbtDag(
    project_config=ProjectConfig(DBT_PROJECT_PATH),
    profile_config=profile_config,
    execution_config=ExecutionConfig(
        dbt_executable_path="/usr/local/airflow/dbt_venv/bin/dbt",
    ),
    schedule=None,
    start_date=datetime(2025, 6, 28),
    catchup=False,
    dag_id="dbt_learn_cosmos",
    tags=["dbt", "cosmos"],
)