import telebot                              
from keyboard import *

                        
TOKEN = "5343039631:AAE7AXTAvO2dVr5gFNwgAwp1yB0SKGAYFNY"
bot = telebot.TeleBot(TOKEN)
cat = "⬇️Оберіть Категорію⬇️ :"


@bot.message_handler(commands="start")
def start(message):

    
    bot.send_message(message.chat.id,
                     "Доброго дня,{0.first_name}👋\n🔍Оберіть Громаду 🏡 :".format(
                         message.from_user), reply_markup=city_markup)


@bot.message_handler(content_types=["text"])
def text(message):
    if message.chat.type == "private":
        if any(message.text == city["name"] for city in cities):
            variable(message)
def variable(message):
    bot.send_message(message.from_user.id,cat,reply_markup=cat_markup)
    bot.register_next_step_handler(message,cate)
    
def cate(message):
    if message.text in [cats['name'] for cats in cat_menu]: 
        if message.text == "↩ПОВЕРНУТИСЬ":
            start(message)
            return 
        elif message.text == "🎓ОСВІТА":
            sub_variants = get_sub_variants(message.text)
            education_markup = ReplyKeyboardMarkup(resize_keyboard=True).add(*[KeyboardButton(sub_e['name']) for sub_e in sub_variants])
            bot.send_message(message.from_user.id,text="Оберіть:",reply_markup=education_markup)
            bot.register_next_step_handler(message,educat)
        elif message.text == "❤МЕДИЦИНА":
            bot.send_message(message.from_user.id,text="Оберіть:",reply_markup=medic_markup)
            bot.register_next_step_handler(message,medic)
        elif message.text == "👵ПЕНСІЯ":
            bot.send_message(message.from_user.id,text="Контактна інформація:")
            bot.register_next_step_handler(message,cate)
        elif message.text == "💐ВПО":
            bot.send_message(message.from_user.id,text="Контактна інформація:")
            bot.register_next_step_handler(message,cate)
        elif message.text == "🙏ГУМАНІТАРКА":
            bot.send_message(message.from_user.id,text="Контактна інформація:")
            bot.register_next_step_handler(message,cate)
        elif message.text == "💆ПСИХОЛОГ":
            bot.send_message(message.from_user.id,text="Контактна інформація:")
            bot.register_next_step_handler(message,cate)
        elif message.text == "💼РОБОТА":
            bot.send_message(message.from_user.id,text="Контактна інформація:")
            bot.register_next_step_handler(message,cate)
        elif message.text == "🏢ЦНАП":
            bot.send_message(message.from_user.id,text="Контактна інформація:")
            bot.register_next_step_handler(message,cate)
    else:
        start(message)
        return
      
def educat(message):
    sub_variants = [sub_variant['name'] for sub_variant in  get_sub_variants(message.text)]
    print(sub_variants)
    if message.text in sub_variants:

            bot.send_message(message.from_user.id,text="Контактна інформація:")
            bot.register_next_step_handler(message,educat)
            
    else:
        start(message)
        return
        
def medic(message):
    if message.text in medic_but:
        if message.text == "🚑ПЕРВИНКА": 
            bot.send_message(message.from_user.id,text="Контактна інформація:")
            bot.register_next_step_handler(message,medic)
        elif message.text == "💊ВТОРИНКА":
            bot.send_message(message.from_user.id,text="Контактна інформація:")
            bot.register_next_step_handler(message,medic)
        elif message.text == "↩ПОВЕРНУТИСЬ":
            variable(message)
            return
    else:
        start(message)
        return
    


bot.polling(non_stop=True,timeout=150)
