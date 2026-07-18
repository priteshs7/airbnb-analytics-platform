{{config(
    materialized='table',
)}}

with fct_reviews AS (
    select * from {{ ref('FCT_REVIEWS') }}
),
full_moon_dates AS(
    select * from {{ ref('seed_full_moon_dates') }}
)

SELECT 
   r.*,
   CASE
     when fm.full_moon_date is null then 'not full moon'
     else 'full moon'
     end as is_full_moon
from 
   fct_reviews
   r    
   left join full_moon_dates
   fm 
   on (to_date(review_date)  = dateadd(day, 1,fm.full_moon_date))