WITH source AS (
    
    SELECT
        "Date",
        "Close",
        "symbol"
    
    FROM {{ source ('dbsales', 'commodities') }}
),

renamed AS (

    SELECT
        cast("Date" as date) as Date,
        "Close" as "Closing Value",
        "symbol" AS Commodity 

    FROM source
)

SELECT * FROM renamed