TOTAL_CHARACTERS = 'SELECT  count(*) from charactercreator_character'

TOTAL_SUBCLASS = 'SELECT  count(*) from charactercreator_'

TOTAL_ITEMS = 'SELECT  count(*) from armory_item'

WEAPONS = 'SELECT count(*) from armory_weapon'

NON_WEAPONS = 'SELECT count(item_id) from armory_item   where item_id not in (select item_ptr_id from armory_weapon )'

CHARACTER_ITEMS = 'SELECT character_id, count(DISTINCT  item_id)  as num_items FROM charactercreator_character_inventory GROUP BY character_id'

CHARACTER_WEAPONS = 'SELECT character_id, count(DISTINCT  item_id)  as num_weapons FROM charactercreator_character_inventory WHERE item_id in (select item_ptr_id from armory_weapon) GROUP BY character_id'

AVG_CHARACTER_ITEMS = 'SELECT avg(num_items) FROM (' + CHARACTER_ITEMS + ')'

AVG_CHARACTER_WEAPONS = 'SELECT avg(num_weapons) FROM (' + CHARACTER_WEAPONS + ')'

CHARACTER_ITEMS_LIST = 'SELECT character_id, group_concat(DISTINCT  item_id)  as num_items FROM charactercreator_character_inventory GROUP BY character_id'

CHARACTER_WEAPONS_LIST = 'SELECT character_id, group_concat(DISTINCT  item_id)  as num_weapons FROM charactercreator_character_inventory WHERE item_id in (select item_ptr_id from armory_weapon) GROUP BY character_id'
