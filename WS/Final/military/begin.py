from scrapy import cmdline

#which spider to execute
#weapons from 中华武器库: 'craft', 'ship', 'weapon', 'tank', 'cannon', 'missile', 'space', 'explosive'
#weapons from 环球军事网: 'craft_2', 'ship_2', 'weapon_2', 'tank_2', 'cannon_2', 'missile_2', 'space_2', 'explosive_2'
#person:
#affair:
cmdline.execute('scrapy crawl weapon_2'.split())