WITH commodities AS (
    SELECT
        date,
        commodity,
        closing_value
    FROM {{ ref('stg_commodities') }}
),

trading AS (
    SELECT  
        date,
        commodity,
        action,
        quantity
    FROM {{ ref('stg_trading_data') }}
),

joined AS (
    SELECT 
        c.date,
        c.commodity,
        c.closing_value,
        t.action,
        t.quantity,
        (t.quantity * c.closing_value) AS price,
        CASE 
            WHEN t.action = 'sell' THEN (t.quantity * c.closing_value)
            ELSE -(t.quantity * c.closing_value)
        END AS earnings
    FROM commodities c
    INNER JOIN trading t
        ON c.date = t.date
        AND c.commodity = t.commodity
),

last_day AS (
    SELECT max(date) as max_date
    FROM joined
),

filtered AS (
    SELECT *
    FROM joined
    WHERE date = (SELECT max_date FROM last_day)
)

SELECT 
    date,
    commodity,
    closing_value,
    action,
    quantity,
    price,
    earnings
FROM filtered