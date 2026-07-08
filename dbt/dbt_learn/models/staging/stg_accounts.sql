{{config(
    materialized = 'incremental',
    incremental_strategy = 'merge',
    unique_key = 'account_id'
)}}

with src as (
    select * from {{ source(
        'postgres',
        'account'
    )}}
{% if is_incremental() %}
    where modified_date >= (select coalesce(max(modified_date), '1970-01-01') from {{ this }})
{% endif %}
)
select
    account_id,
    customer_id,
    branch_id,
    account_balance,
    lien_amt,
    acct_cls_flg,
    product_id,
    schm_type,
    schm_code,
    acct_crncy_code,
    acct_opn_date,
    created_date,
    modified_date
from 
    src