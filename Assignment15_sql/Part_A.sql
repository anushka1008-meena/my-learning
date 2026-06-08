use data_bank;

/* we have create the table name regions , execute it -> now table is created successfully....so we comment it 
CREATE TABLE regions (
  region_id INTEGER,
  region_name VARCHAR(9)
);

INSERT INTO regions
  (region_id, region_name)
VALUES
  ('1', 'Australia'),
  ('2', 'America'),
  ('3', 'Africa'),
  ('4', 'Asia'),
  ('5', 'Europe'); 
*/

-- we have converted the data of customer_transaction & customer_nodes into CSV file & imported it


SELECT COUNT(*) FROM regions;   
-- output = 5

SELECT COUNT(*) FROM customer_nodes;
-- output = 3500

SELECT COUNT(*) FROM customer_transactions;
-- output = 5868


-- PART A  =  Customer Nodes Exploration


-- Q1. How many unique nodes are there on the Data Bank system?

select count(distinct node_id) as unique_nodes
from customer_nodes;

/* 
output
unique_nodes
------------
5
*/





--------------------------------------------------------------------------------

-- Q2. What is the number of nodes per region?

select
r.region_name, count(distinct c.node_id) as total_nodes
from customer_nodes c
inner join regions r
on c.region_id = r.region_id
group by r.region_name;

/*
output 
region_name total_nodes
----------- -----------
Africa      5
America     5
Asia        5
Australia   5
Europe      5
*/




---------------------------------------------------------------------
-- Q3. How many customers are allocated to each region?

select
r.region_name, count(distinct c.customer_id) as total_customers 
from customer_nodes c
inner join regions r
on c.region_id = r.region_id
group by r.region_name;

/* 
output
region_name total_customers
----------- ---------------
Africa      102
America     105
Asia        95
Australia   110
Europe      88
*/




------------------------------------------------------------------------

-- Q4. How many days on average are customers reallocated to a different node?

select
avg(datediff(day, start_date, end_date)) as avg_reallocation_days  -- datediff = gives date difference 
from customer_nodes
where end_date != '9999-12-31';            -- -- removing customers still on same node

/*
output 
avg_reallocation_days
---------------------
14
*/





---------------------------------------------------------------------------------------------------------

-- q5. What is the median, 80th and 95th percentile for this same reallocation days metric for each region

select distinct
r.region_name,

    percentile_cont(0.5)
    within group (order by datediff(day, c.start_date, c.end_date))
    over(partition by r.region_name) as median,

    percentile_cont(0.8)
    within group (order by datediff(day, c.start_date, c.end_date))
    over(partition by r.region_name) as percentile_80,

    percentile_cont(0.95)
    within group (order by datediff(day, c.start_date, c.end_date))
    over(partition by r.region_name) as percentile_95

from customer_nodes c
inner join regions r
on c.region_id = r.region_id

where end_date != '9999-12-31';

/*
output
region_name median                 percentile_80          percentile_95
----------- ---------------------- ---------------------- ----------------------
Australia   15                     23                     28
Africa      15                     24                     28
Asia        15                     23                     28
America     15                     23                     28
Europe      15                     24                     28
*/

