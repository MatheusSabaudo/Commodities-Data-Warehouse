WITH source AS (
    
    SELECT
        "Date",
        "Close",
        "symbol"
    
    FROM {{ source('dbsales', 'commodities') }}
),

renamed AS (

    SELECT
        cast("Date" as date) as date,
        "symbol" as commodity,
        "Close" as closing_value

    FROM source
)

SELECT * 
FROM renamed