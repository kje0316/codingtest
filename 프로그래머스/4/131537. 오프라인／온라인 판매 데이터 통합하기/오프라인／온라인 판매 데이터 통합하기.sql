-- 코드를 입력하세요
# SELECT * from ONLINE_SALE where extract(month from sales_date) = 3 join OFFLINE_SALE ;

select DATE_FORMAT(SALES_DATE, '%Y-%m-%d') AS SALES_DATE, PRODUCT_ID, USER_ID, SALES_AMOUNT from ONLINE_SALE  where extract(month from sales_date) = 3 
union all
select DATE_FORMAT(SALES_DATE, '%Y-%m-%d') AS SALES_DATE, PRODUCT_ID, NULL, SALES_AMOUNT from OFFLINE_SALE where extract(month from sales_date) = 3
order by sales_date, product_id, user_id;

