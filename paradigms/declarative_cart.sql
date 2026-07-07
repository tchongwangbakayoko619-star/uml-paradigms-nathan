-- Declarative Version (SQL)

SELECT
    SUM(unit_price * quantity) AS subtotal,
    CASE
        WHEN SUM(unit_price * quantity) > 50000
        THEN SUM(unit_price * quantity) * 0.9
        ELSE SUM(unit_price * quantity)
    END AS total_price
FROM order_items
WHERE order_id = 1;  -- Example for a specific order
