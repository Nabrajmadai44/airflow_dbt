{{ config(
    materialized='incremental',
    incremental_strategy='merge',
    unique_key='tran_id'
) }}

with src as (
    select * from {{ source(
        'postgres',
        'hist_transactional'
    )}}
    {% if is_incremental() %}
where modified_date >
(
    select coalesce(max(modified_date),'1970-01-01')
    from {{ this }}
)
{% endif %}
)
select
    {{ dbt_utils.generate_surrogate_key(['tran_id', 'modified_date']) }} AS tran_sk,
    tran_id,
    account_id,
    tran_amount,
    tran_date,
    tran_crncy,
    branch_id,
    tran_particular,
    tran_remarks,
    created_date,
    modified_date
from 
    src