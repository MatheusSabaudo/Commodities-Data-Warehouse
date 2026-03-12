WITH source AS (
    
    SELECT
        date,
        symbol,
        action,
        quantity
    
    FROM {{ source('dbsales', 'trading_data') }}
),

renamed AS (

    SELECT
        cast(date as date) as date,
        symbol as commodity,
        action as action,
        quantity as quantity

    FROM source
)

SELECT *
FROM renamed