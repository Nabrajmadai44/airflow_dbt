FROM astrocrpublic.azurecr.io/runtime:3.2-5

COPY --chown=astro:root dbt/ /usr/local/airflow/dbt/

RUN python -m venv /usr/local/airflow/dbt_venv && \
    /usr/local/airflow/dbt_venv/bin/pip install --upgrade pip && \
    /usr/local/airflow/dbt_venv/bin/pip install \
        dbt-core==1.11.1 \
        dbt-postgres==1.10.2