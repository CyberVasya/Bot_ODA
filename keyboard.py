from re import A
from tokenize import Name
from unicodedata import name
from telebot.types import KeyboardButton,ReplyKeyboardMarkup
from orm.controllers import get_regions,get_variants,get_sub_variants
from orm.models import Region,Payload
from orm.database import db_session


cat_menu = get_variants()

cities = get_regions()





medic_but = get_sub_variants("")

city_markup = ReplyKeyboardMarkup(row_width=2).add(*[KeyboardButton(city["name"]) for city in cities])
cat_markup = ReplyKeyboardMarkup(row_width=2).add(*[KeyboardButton(cat["name"]) for cat in cat_menu])
medic_markup = ReplyKeyboardMarkup(resize_keyboard=True).add(*[KeyboardButton(sub_m) for sub_m in medic_but])

print(get_sub_variants(variant_name="🎓ОСВІТА"))
print(next(filter(lambda region: region['name'][1:]=="Агрономічна", get_regions())))
print(Region.get(db_session,name="👪Агрономічна").id)

Payload.create(db_session,phone = "077",region_id = 1,variant_id = 1)





