-- 코드를 작성해주세요
# SELECT A.ITEM_ID, A.ITEM_NAME, A.RARITY
# FROM ITEM_INFO AS A
# JOIN (select PARENT_ITEM_ID from ITEM_TREE where is not null) AS B ON A.ITEM_ID = B.ITEM_ID
# WHERE A.RARITY = 'RARE'


# SELECT ITEM_ID, ITEM_NAME, RARITY
# from ITEM_INFO where ITEM_ID in   (select ITEM_ID from ITEM_TREE where PARENT_ITEM_ID is not null) and RARITY = 'RARE' order by ITEM_ID;
# select PARENT_ITEM_ID from ITEM_TREE where PARENT_ITEM_ID is not null;

# select * from ITEM_INFO where RARITY = 'RARE' join ITEM_TREE on ITEM_TREE.ITEM_ID = ITEM_INFO.ITEM_ID;

# select * from ITEM_INFO where ITEM_ID in (select PARENT_ITEM_ID from ITEM_INFO join ITEM_TREE on ITEM_INFO.ITEM_ID = PARENT_ITEM_ID where RARITY = 'RARE');

# select * from ITEM_INFO where RARITY='RARE' ;

# select ITEM_ID, PARENT_ITEM_ID from ITEM_TREE where parent_item_id is not null



# select * from item_tree;

# select i.item_id, 
#     item_name, rarity
# from item_info i
# join item_tree t
# on i.item_id = t.item_id
# where parent_item_id is not null
# order by item_id DESC;

# select i.item_id, item_name, rarity from item_info i join (select * from item_tree where parent_item_id is not null) as t on i.item_id = t.item_id order by item_id desc;

# select * from item_tree t join (select * from item_info where rarity='rare') as i on i.item_id = t.item_id; 
# # where parent_item_id is not null;


# select * from ITEM_INFO where rarity = 'rare';
# select * from ITEM_INFO where ITEM_ID in (select ITEM_ID from ITEM_TREE where PARENT_ITEM_ID is not null) 
# select ITEM_ID from ITEM_TREE where PARENT_ITEM_ID is not null

# select * from ITEM_INFO where rarity = 'rare';
# select ITEM_ID from ITEM_TREE where PARENT_ITEM_ID is not null;
# select * from (select * from ITEM_INFO where rarity = 'rare') as i where item_id in (select PARENT_ITEM_ID from ITEM_TREE where PARENT_ITEM_ID is not null) join item_tree on ITEM_INFO.itme_id= ITEM_TREE.PARENT_ITEM_ID
# outer join 
# item_tree on ITEM_INFO.itme_id= ITEM_TREE.PARENT_ITEM_ID
# ;
# select * from (select * from ITEM_INFO where rarity = 'rare') as i where item_id in (select PARENT_ITEM_ID from ITEM_TREE where PARENT_ITEM_ID is not null) as table_info left join ITEM_TREE 
# on table_info.item_id = ITEM_TREE.PARENT_ITEM_ID;

# select * from (select * from ITEM_INFO where rarity = 'rare') as i where item_id in (select PARENT_ITEM_ID from ITEM_TREE where PARENT_ITEM_ID is not null);
# join ITEM_TREE
# on info.ITEM_ID = ITEM_TREE.PARENT_ITEM_ID
select item_id, item_name, rarity from item_info where item_id in (select ITEM_TREE.ITEM_ID from (select * from (select * from ITEM_INFO where rarity = 'rare') as i where item_id in (select PARENT_ITEM_ID from ITEM_TREE where PARENT_ITEM_ID is not null)) as info 
join ITEM_TREE 
on info.ITEM_ID = ITEM_TREE.PARENT_ITEM_ID) order by item_id desc