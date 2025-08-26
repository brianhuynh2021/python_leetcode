# EPAM SQL Interview Practice – E‑Commerce Backend

## Schema (assumed)

```sql
CREATE TABLE customers (
  id BIGINT PRIMARY KEY,
  name TEXT,
  created_at TIMESTAMP NOT NULL
);

CREATE TABLE orders (
  id BIGINT PRIMARY KEY,
  customer_id BIGINT REFERENCES customers(id),
  status TEXT,
  created_at TIMESTAMP NOT NULL
);

CREATE TABLE order_items (
  order_id BIGINT REFERENCES orders(id),
  product_id BIGINT REFERENCES products(id),
  qty INT NOT NULL,
  unit_price NUMERIC(12,2) NOT NULL
);

CREATE TABLE products (
  id BIGINT PRIMARY KEY,
  name TEXT,
  category TEXT
);

CREATE TABLE payments (
  id BIGINT PRIMARY KEY,
  order_id BIGINT REFERENCES orders(id),
  amount NUMERIC(12,2) NOT NULL,
  status TEXT,
  paid_at TIMESTAMP
);

CREATE TABLE refunds (
  id BIGINT PRIMARY KEY,
  order_id BIGINT REFERENCES orders(id),
  amount NUMERIC(12,2) NOT NULL,
  created_at TIMESTAMP
);
```

---

## 1) Total revenue per day (last 7 days)

```sql
SELECT
  DATE(o.created_at) AS order_day,
  SUM(oi.qty * oi.unit_price) AS revenue
FROM orders o
JOIN order_items oi ON oi.order_id = o.id
WHERE o.created_at >= CURRENT_DATE - INTERVAL '7 days'
GROUP BY order_day
ORDER BY order_day DESC;
```

---

## 2) Top 3 customers by lifetime spend

```sql
SELECT customer_id, SUM(oi.qty * oi.unit_price) AS total_spent
FROM orders o
JOIN order_items oi ON oi.order_id = o.id
GROUP BY customer_id
ORDER BY total_spent DESC
LIMIT 3;
```

---

## 3) First purchase date per customer

```sql
SELECT customer_id, MIN(created_at) AS first_purchase_at
FROM orders
GROUP BY customer_id;
```

---

## 4) New vs returning customers by day

```sql
WITH first_order AS (
  SELECT customer_id, MIN(created_at) AS first_at
  FROM orders
  GROUP BY customer_id
)
SELECT
  DATE(o.created_at) AS day,
  COUNT(*) FILTER (WHERE fo.first_at::date = o.created_at::date) AS new_customers_orders,
  COUNT(*) FILTER (WHERE fo.first_at::date <  o.created_at::date) AS returning_customers_orders
FROM orders o
JOIN first_order fo ON fo.customer_id = o.customer_id
GROUP BY day
ORDER BY day;
```

---

## 5) Average order value (AOV) per customer

```sql
WITH order_totals AS (
  SELECT o.id, o.customer_id, SUM(oi.qty * oi.unit_price) AS order_total
  FROM orders o
  JOIN order_items oi ON oi.order_id = o.id
  GROUP BY o.id, o.customer_id
)
SELECT customer_id,
       AVG(order_total) AS avg_order_value
FROM order_totals
GROUP BY customer_id
ORDER BY avg_order_value DESC;
```

---

## 6) Products never ordered (anti‑join)

```sql
SELECT p.*
FROM products p
LEFT JOIN order_items oi ON oi.product_id = p.id
WHERE oi.product_id IS NULL;
```

---

## 7) Best‑selling products (by revenue) with category

```sql
SELECT
  p.id, p.name, p.category,
  SUM(oi.qty) AS units_sold,
  SUM(oi.qty * oi.unit_price) AS revenue
FROM order_items oi
JOIN products p ON p.id = oi.product_id
GROUP BY p.id, p.name, p.category
ORDER BY revenue DESC;
```

---

## 8) Month‑over‑month revenue + growth %

```sql
WITH m AS (
  SELECT
    DATE_TRUNC('month', o.created_at) AS month,
    SUM(oi.qty * oi.unit_price) AS revenue
  FROM orders o
  JOIN order_items oi ON oi.order_id = o.id
  GROUP BY 1
)
SELECT
  month,
  revenue,
  LAG(revenue) OVER (ORDER BY month) AS prev_rev,
  CASE
    WHEN LAG(revenue) OVER (ORDER BY month) IS NULL OR LAG(revenue) OVER (ORDER BY month) = 0
      THEN NULL
    ELSE ROUND( (revenue - LAG(revenue) OVER (ORDER BY month))
                / LAG(revenue) OVER (ORDER BY month) * 100.0, 2)
  END AS mom_growth_percent
FROM m
ORDER BY month;
```

---

## 9) Running 7‑day rolling revenue

```sql
WITH daily AS (
  SELECT DATE(o.created_at) AS day,
         SUM(oi.qty * oi.unit_price) AS rev
  FROM orders o
  JOIN order_items oi ON oi.order_id = o.id
  GROUP BY 1
)
SELECT
  day,
  SUM(rev) OVER (
    ORDER BY day
    ROWS BETWEEN 6 PRECEDING AND CURRENT ROW
  ) AS rev_7d
FROM daily
ORDER BY day;
```

---

## 10) Latest status per order

```sql
WITH ranked AS (
  SELECT
    order_id, status, changed_at,
    ROW_NUMBER() OVER (PARTITION BY order_id ORDER BY changed_at DESC) AS rn
  FROM order_status_history
)
SELECT order_id, status AS latest_status, changed_at AS as_of
FROM ranked
WHERE rn = 1;
```

---

## 11) Detect duplicate payments

```sql
SELECT p1.order_id, p1.amount, p1.paid_at AS paid_at_1, p2.paid_at AS paid_at_2
FROM payments p1
JOIN payments p2
  ON p1.order_id = p2.order_id
 AND p1.amount   = p2.amount
 AND p1.id       < p2.id
 AND ABS(EXTRACT(EPOCH FROM (p1.paid_at - p2.paid_at))) <= 300;
```

---

## 12) Customers with no orders in the last 90 days

```sql
SELECT c.*
FROM customers c
LEFT JOIN LATERAL (
  SELECT MAX(o.created_at) AS last_order_at
  FROM orders o
  WHERE o.customer_id = c.id
) lo ON TRUE
WHERE lo.last_order_at IS NULL
   OR lo.last_order_at < CURRENT_DATE - INTERVAL '90 days';
```

---

## 13) Percent contribution of each product to total revenue

```sql
WITH prod AS (
  SELECT p.id, p.name, SUM(oi.qty * oi.unit_price) AS revenue
  FROM products p
  JOIN order_items oi ON oi.product_id = p.id
  GROUP BY p.id, p.name
),
tot AS (
  SELECT SUM(revenue) AS grand_total FROM prod
)
SELECT
  pr.id, pr.name, pr.revenue,
  ROUND(pr.revenue / NULLIF(t.grand_total, 0) * 100.0, 2) AS pct_of_total
FROM prod pr CROSS JOIN tot t
ORDER BY pct_of_total DESC;
```

---

## 14) N‑th highest order per customer

```sql
WITH ranked AS (
  SELECT
    o.customer_id,
    o.id AS order_id,
    SUM(oi.qty * oi.unit_price) AS order_total,
    DENSE_RANK() OVER (PARTITION BY o.customer_id ORDER BY SUM(oi.qty * oi.unit_price) DESC) AS rnk
  FROM orders o
  JOIN order_items oi ON oi.order_id = o.id
  GROUP BY o.customer_id, o.id
)
SELECT customer_id, order_id, order_total
FROM ranked
WHERE rnk = 2;
```

---

## 15) Low inventory alert

```sql
WITH sold AS (
  SELECT oi.product_id, COALESCE(SUM(oi.qty), 0) AS qty_sold
  FROM order_items oi
  GROUP BY oi.product_id
)
SELECT
  p.id, p.name,
  i.stock - COALESCE(s.qty_sold, 0) AS remaining
FROM products p
JOIN inventory i ON i.product_id = p.id
LEFT JOIN sold s ON s.product_id = p.id
WHERE (i.stock - COALESCE(s.qty_sold, 0)) < 10
ORDER BY remaining ASC;
```
