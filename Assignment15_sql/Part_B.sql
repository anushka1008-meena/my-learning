use data_bank;

-- PART B  =  Customer Transactions 

-- Q1. What is the unique count and total amount for each transaction type?

select
txn_type,
count(*) as transaction_count,
sum(txn_amount) as total_amount
from customer_transactions
group by txn_type;

/* 
output :
txn_type                                           transaction_count total_amount
-------------------------------------------------- ----------------- ------------
purchase                                           1617              806537
withdrawal                                         1580              793003
deposit                                            2671              1359168
*/





-------------------------------------------------------------------------------

-- q2. What is the average total historical deposit counts and amounts for all customers?

select
avg(deposit_count) as avg_deposit_count,
avg(total_amount) as avg_deposit_amount

from (
       select
       customer_id,
       count(*) as deposit_count,
       sum(txn_amount) as total_amount
       from customer_transactions
       where txn_type = 'deposit'
       group by customer_id
     ) as deposits;

/* 
output :
avg_deposit_count avg_deposit_amount
----------------- ------------------
5                 2718
*/






----------------------------------------------------------------------

-- Q3. For each month - how many Data Bank customers make more than 1 deposit and either 1 purchase or 1 withdrawal in a single month? 

select
month_no, count(customer_id) as customer_count

from (

    select
    customer_id,
    month(txn_date) as month_no,

    sum(case when txn_type = 'deposit' then 1 else 0 end) as deposit_count,

    sum(case when txn_type = 'purchase' then 1 else 0 end) as purchase_count,

    sum(case when txn_type = 'withdrawal' then 1 else 0 end) as withdrawal_count

    from customer_transactions

    group by
    customer_id,
    month(txn_date)

) as monthly_data

where deposit_count > 1  and (purchase_count >= 1  or  withdrawal_count >= 1)

group by month_no
order by month_no;

/*
output :
month_no    customer_count
----------- --------------
1           168
2           181
3           192
4           70
*/
