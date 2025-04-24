# select * from item_info where item_id not in (select PARENT_TIME_ID from ITEM_TREE is not null)

select item_info.item_id, item_name, rarity from item_info where item_id not in (select PARENT_ITEM_ID from ITEM_TREE where PARENT_ITEM_ID is not null) order by item_id desc;