-- 코드를 입력하세요
# SELECT  *  from REST_INFO  join REST_REVIEW  on REST_INFO.REST_ID = REST_REVIEW.REST_ID;
-- 코드를 입력하세요

# # SELECT REST_INFO.REST_ID, REST_NAME, FOOD_TYPE, FAVORITES , ADDRESS, round(avg(REVIEW_SCORE),2) as SCORE   from REST_INFO  join REST_REVIEW  on REST_INFO.REST_ID = REST_REVIEW.REST_ID 
# # where ADDRESS like '서울%'
# # order by SCORE DESC, FAVORITES DESC;

# select * from REST_INFO;

select REST_INFO.REST_ID, REST_NAME, FOOD_TYPE, FAVORITES , ADDRESS, b.SCORE from REST_INFO
join (select REST_ID, round(avg(REVIEW_SCORE), 2) as SCORE from REST_REVIEW group by REST_ID) as b on  REST_INFO.REST_ID = b.REST_ID where ADDRESS like '서울%' 
order by SCORE DESC, FAVORITES DESC;
