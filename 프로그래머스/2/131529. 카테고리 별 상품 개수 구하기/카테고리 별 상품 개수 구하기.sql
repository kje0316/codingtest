# -- 코드를 입력하세요
# SELECT CASE WHEN product_id in (1, 2) THEN 'A1'
#     WHEN product_id in (3, 4, 5) THEN 'C3'
#     WHEN product_id in (6) THEN 'K1' 
#     ELSE ''
#     END AS CATEGORY, COUNT(*)
# FROM product GROUP BY CATEGORY ORDER BY ;
    
select LEFT(PRODUCT_CODE, 2) AS CATEGORY, COUNT(*) AS PRODUCTS from product group by CATEGORY order by category;