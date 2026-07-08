
{{config(
    materialized = 'table',
    on_schema_change = 'sync_all_columns',
        post_hook = [
        "Create index if not exists idx_slv_customer_nationality on {{ this }} (nationality)"
    ],
)}}

with src as (
    select * from 
    {{ source(
        'postgres',
        'customer'
    )}}
)
select
    cust_id,
    name,
    address,
    phone_number,
    postal_code,
    country,
    email,
    father_name,
    mother_name,
    occupation,
    education,
    nationality,
    created_date,
    modified_date,
    temporary_address
from src