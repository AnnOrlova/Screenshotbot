import telebot
from telebot import types
import random
from random import choice


bot = telebot.TeleBot('6241785570:AAEDRkG-3S3U9fiKqrhGi7ocwZuPnloOJF0')

@bot.message_handler(commands=['start'])
def start(message):

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("Профиль и регистрация")
    btn2 = types.KeyboardButton('Меню')
    btn3 = types.KeyboardButton('Адрес')
    btn4 = types.KeyboardButton('Корзина')
    btn5 = types.KeyboardButton('Заказ')
    btn6 = types.KeyboardButton('Скидка сотрудника')
    btn7 = types.KeyboardButton('Тестовая группа')
    btn8 = types.KeyboardButton('Замены')
    markup.add(btn1, btn2, btn3, btn4, btn5, btn6, btn7, btn8)
    bot.send_message(message.from_user.id, 'Йоу! Какой скрин нужен?', reply_markup=markup)

@bot.message_handler(content_types=['text'])
def get_text_messages(message):

    if message.text == 'Профиль и регистрация':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Бонусы при регистрации")
        btn2 = types.KeyboardButton('Выход')
        btn3 = types.KeyboardButton('Изменить промик')
        btn4 = types.KeyboardButton('Имя')
        btn5 = types.KeyboardButton('Заказы')
        btn6 = types.KeyboardButton('Пропустить номер при регистрации')
        btn7 = types.KeyboardButton('Кол-во бонусов')
        btn8 = types.KeyboardButton('Личный промик')
        btn9 = types.KeyboardButton('Оферта')
        btn10 = types.KeyboardButton('Сколько сделать заказов по КМ')
        btn11 = types.KeyboardButton('Способы оплаты')
        btn12 = types.KeyboardButton('Удалить аккаунт')
        btn13 = types.KeyboardButton('Удалить карту')
        btn14 = types.KeyboardButton('Фото')
        btn15 = types.KeyboardButton('Вернуться на главную')
        markup.add(btn1, btn2, btn3, btn4, btn5, btn6, btn7, btn8, btn9, btn10, btn11, btn12, btn13, btn14, btn15)
        bot.send_message(message.from_user.id, "Выбери скрин", reply_markup=markup)

    elif message.text == 'Вернуться на главную':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Профиль и регистрация")
        btn2 = types.KeyboardButton('Меню')
        btn3 = types.KeyboardButton('Адрес')
        btn4 = types.KeyboardButton('Корзина')
        btn5 = types.KeyboardButton('Заказ')
        btn6 = types.KeyboardButton('Скидка сотрудника')
        btn7 = types.KeyboardButton('Тестовая группа')
        btn8 = types.KeyboardButton('Замены')
        markup.add(btn1, btn2, btn3, btn4, btn5, btn6, btn7, btn8)
        bot.send_message(message.from_user.id, 'Йоу! Какой скрин нужен?', reply_markup=markup)

    elif message.text == 'Бонусы при регистрации':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('Назад')
        markup.add(btn1)

    elif message.text == 'Выход':
        bot.send_message(message.from_user.id, 'Нажать на изображение профиля или значок человечка/фотоаппарата в левом верхнем углу → экран личного профиля → раздел Настройки → кнопка Выйти')
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('Назад')
        markup.add(btn1)

    elif message.text == 'Изменить промик':
        bot.send_message(message.from_user.id, 'Нужно нажать на изображение профиля или значок человечка/фотоаппарата в левом верхнем углу → экран личного профиля → раздел Бонусы → рядом с названием промокода нажать на карандашик')
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('Назад')
        markup.add(btn1)

    elif message.text == 'Имя':
        bot.send_message(message.from_user.id, 'Нужно нажать на изображение профиля или значок человечка/фотоаппарата, чтобы перейти в Профиль. Затем нажать на имя или Настройки → добавить или изменить имя в поле «Как вас зовут»')
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('Назад')
        markup.add(btn1)

    elif message.text == 'Заказы':
        bot.send_message(message.from_user.id, 'Нужно нажать на изображение профиля или значок человечка/фотоаппарата, чтобы перейти в Профиль. Далее выбрать раздел Заказы')
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('Назад')
        markup.add(btn1)

    elif message.text == 'Пропустить номер при регистрации':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('Назад')
        markup.add(btn1)

    elif message.text == 'Кол-во бонусов':
        bot.send_message(message.from_user.id, 'Нажать на изображение профиля или значок человечка/фотоаппарата в левом верхнем углу и перейти в раздел Бонусы')
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('Назад')
        markup.add(btn1)

    elif message.text == 'Личный промик':
        bot.send_message(message.from_user.id, 'Нужно нажать на изображение профиля или значок человечка/фотоаппарата в левом верхнем углу → экран личного профиля → раздел Бонусы → А вот ваш код')
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('Назад')
        markup.add(btn1)

    elif message.text == 'Оферта':
        bot.send_message(message.from_user.id, 'Нужно нажать на изображение профиля или значок человечка/фотоаппарата, чтобы перейти в Профиль. В нижнем правом углу будет ссылка на Оферту ')
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('Назад')
        markup.add(btn1)

    elif message.text == 'Сколько сделать заказов по КМ':
        bot.send_message(message.from_user.id, 'Нужно нажать на изображение профиля или значок человечка/фотоаппарата, чтобы перейти в Профиль.')
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('Назад')
        markup.add(btn1)

    elif message.text == 'Способы оплаты':
        bot.send_message(message.from_user.id, 'Нужно нажать на изображение профиля или значок человечка/фотоаппарата → Способы оплаты внизу экрана')
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('Назад')
        markup.add(btn1)

    elif message.text == 'Удалить аккаунт':
        bot.send_message(message.from_user.id, 'Нужно нажать на изображение профиля или значок человечка/фотоаппарата, чтобы перейти в профиль. Затем Настройки → Удалить аккаунт')
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('Назад')
        markup.add(btn1)

    elif message.text == 'Удалить карту':
        bot.send_message(message.from_user.id, 'Нажать на изображение профиля или значок человечка/фотоаппарата в левом верхнем углу → экран личного профиля → Способы оплаты. Далее нужно выбрать карту, свайпнуть ее влево и нажать на значок с корзиной')
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('Назад')
        markup.add(btn1)

    elif message.text == 'Фото':
        bot.send_message(message.from_user.id, 'Нужно нажать на изображение профиля или значок человечка/фотоаппарата → нажать на имя или Настройки → нажать на фото → сделать снимок или выбрать из галереи')
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('Назад')
        markup.add(btn1)

    elif message.text == 'Назад':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('Бонусы при регистрации')
        btn2 = types.KeyboardButton('Выход')
        btn3 = types.KeyboardButton('Изменить промик')
        btn4 = types.KeyboardButton('Имя')
        btn5 = types.KeyboardButton('Заказы')
        btn6 = types.KeyboardButton('Пропустить номер при регистрации')
        btn7 = types.KeyboardButton('Кол-во бонусов')
        btn8 = types.KeyboardButton('Личный промик')
        btn9 = types.KeyboardButton('Оферта')
        btn10 = types.KeyboardButton('Сколько сделать заказов по КМ')
        btn11 = types.KeyboardButton('Способы оплаты')
        btn12 = types.KeyboardButton('Удалить аккаунт')
        btn13 = types.KeyboardButton('Удалить карту')
        btn14 = types.KeyboardButton('Фото')
        btn15 = types.KeyboardButton('Вернуться на главную')
        markup.add(btn1, btn2, btn3, btn4, btn5, btn6, btn7, btn8, btn9, btn10, btn11, btn12, btn13, btn14, btn15)
        bot.send_message(message.from_user.id, "Выбери скрин", reply_markup=markup)

    elif message.text == 'Меню':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('КБЖУ блюда')
        btn2 = types.KeyboardButton('Состав')
        btn3 = types.KeyboardButton('Теги')
        btn4 = types.KeyboardButton('Добавить к завтраку')
        btn5 = types.KeyboardButton('Соусы')
        btn6 = types.KeyboardButton('Раздел Вы заказывали')
        btn7 = types.KeyboardButton('Верхняя навигация')
        btn8 = types.KeyboardButton('Вернуться на главную')
        markup.add(btn1, btn2, btn3, btn4, btn5, btn6, btn7, btn8)
        bot.send_message(message.from_user.id, "Выбери скрин", reply_markup=markup)

    elif message.text == 'Вернуться на главную':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('Профиль и регистрация')
        btn2 = types.KeyboardButton('Меню')
        btn3 = types.KeyboardButton ('Адрес')
        btn4 = types.KeyboardButton ('Корзина')
        btn5 = types.KeyboardButton ('Заказ')
        btn6 = types.KeyboardButton ('Скидка сотрудника')
        btn7 = types.KeyboardButton ('Тестовая группа')
        btn8 = types.KeyboardButton ('Замены')
        markup.add(btn1, btn2, btn3, btn4, btn5, btn6, btn7, btn8)
        bot.send_message(message.from_user.id, 'Йоу! Какой скрин нужен?', reply_markup=markup)
        
    elif message.text == 'КБЖУ блюда':
        bot.send_message(message.from_user.id, 'Нужно нажать на блюдо, откроется карточка с информацией. КБЖУ указан под составом')
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('Назад')
        markup.add(btn1)

    elif message.text == 'Состав':
        bot.send_message(message.from_user.id, 'Нужно нажать на блюдо и пролистать экран вниз')
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('Назад')
        markup.add(btn1)

    elif message.text == 'Теги':
        bot.send_message(message.from_user.id, 'Нужно нажать на блюдо. Под названием указан тег: 🌱 — веганское, 🥦 — вегетарианское, 🐧 — холодное, 🌶 — острое')
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('Назад')
        markup.add(btn1)

    elif message.text == 'Добавить к завтраку':
        bot.send_message(message.from_user.id, 'Пролистать верхнюю навигацию с разделами меню влево, найти и нажать на кнопку «Добавить к завтраку». Затем в одноименном разделе выбрать нужную позицию')
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('Назад')
        markup.add(btn1)

    elif message.text == 'Соусы':
        bot.send_message(message.from_user.id, 'Пролистать верхнюю навигацию с разделами меню влево, найти и нажать на кнопку «Соусы». Затем в одноименном разделе выбрать нужный')
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('Назад')
        markup.add(btn1)

    elif message.text == 'Раздел Вы заказывали':
        bot.send_message(message.from_user.id, 'Раздел находится на экране с меню под адресом')
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('Назад')
        markup.add(btn1)

    elif message.text == 'Верхняя навигация':
        bot.send_message(message.from_user.id, 'Чтобы появилась навигация, нужно опустить экран меню чуть ниже')
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('Назад')
        markup.add(btn1)

    elif message.text == 'Назад':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('КБЖУ блюда')
        btn2 = types.KeyboardButton('Состав')
        btn3 = types.KeyboardButton('Теги')
        btn4 = types.KeyboardButton('Добавить к завтраку')
        btn5 = types.KeyboardButton('Соусы')
        btn6 = types.KeyboardButton('Раздел Вы заказывали')
        btn7 = types.KeyboardButton('Верхняя навигация')
        btn8 = types.KeyboardButton('Вернуться на главную')
        markup.add(btn1, btn2, btn3, btn4, btn5, btn6, btn7, btn8)
        bot.send_message(message.from_user.id, "Выбери скрин", reply_markup=markup)

    elif message.text == 'Адрес':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('Первый адрес')
        btn2 = types.KeyboardButton('Изменить адрес')
        btn3 = types.KeyboardButton('Добавить еще один адрес')
        btn4 = types.KeyboardButton('Изменить комментарий(один адрес)')
        btn5 = types.KeyboardButton('Изменить комментарий (2 и более адресов)')
        btn6 = types.KeyboardButton('Удалить адрес')
        btn7 = types.KeyboardButton('Вернуться на главную')
        markup.add(btn1, btn2, btn3, btn4, btn5, btn6, btn7)
        bot.send_message(message.from_user.id, "Выбери скрин", reply_markup=markup)

    elif message.text == 'Вернуться на главную':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('Профиль и регистрация')
        btn2 = types.KeyboardButton('Меню')
        btn3 = types.KeyboardButton ('Адрес')
        btn4 = types.KeyboardButton ('Корзина')
        btn5 = types.KeyboardButton ('Заказ')
        btn6 = types.KeyboardButton ('Скидка сотрудника')
        btn7 = types.KeyboardButton ('Тестовая группа')
        btn8 = types.KeyboardButton ('Замены')
        markup.add(btn1, btn2, btn3, btn4, btn5, btn6, btn7, btn8)
        bot.send_message(message.from_user.id, 'Йоу! Какой скрин нужен?', reply_markup=markup)
        
    elif message.text == 'Первый адрес':
        bot.send_message(message.from_user.id, 'Значок карандаша → поле ввода → кнопка «Везите сюда»')
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('Назад')
        markup.add(btn1)

    elif message.text == 'Изменить адрес':
        bot.send_message(message.from_user.id, 'Нажать на значок карандаша на главном экране → выбрать нужный адрес из списка')
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('Назад')
        markup.add(btn1)
        
    elif message.text == 'Добавить еще один адрес':
        bot.send_message(message.from_user.id, 'Экран меню → значок карандаша → кнопка «Новый адрес» → кнопка «Везите сюда»')
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('Назад')
        markup.add(btn1)
        
    elif message.text == 'Изменить комментарий(один адрес)':
        bot.send_message(message.from_user.id, 'Дважды нажать на значок карандаша в правом верхнем углу → поле комментария → Готово')
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('Назад')
        markup.add(btn1)

    elif message.text == 'Изменить комментарий (2 и более адресов)':
        bot.send_message(message.from_user.id, 'Дважды нажать на значок карандаша в правом верхнем углу → поле комментария → Готово')
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('Назад')
        markup.add(btn1)

    elif message.text == 'Удалить адрес':
        bot.send_message(message.from_user.id, 'Нажать на изображение профиля или значок человечка/фотоаппарата в левом верхнем углу → экран личного профиля → раздел Адреса → значок карандаша → нажать на минус рядом с адресом, который хотите удалить → затем «Готово»')
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('Назад')
        markup.add(btn1)
 
    elif message.text == 'Назад':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('Первый адрес')
        btn2 = types.KeyboardButton('Изменить адрес')
        btn3 = types.KeyboardButton('Добавить еще один адрес')
        btn4 = types.KeyboardButton('Изменить комментарий(один адрес)')
        btn5 = types.KeyboardButton('Изменить комментарий (2 и более адресов)')
        btn6 = types.KeyboardButton('Удалить адрес')
        btn7 = types.KeyboardButton('Вернуться на главную')
        markup.add(btn1, btn2, btn3, btn4, btn5, btn6, btn7)
        bot.send_message(message.from_user.id, "Выбери скрин", reply_markup=markup)

    elif message.text == 'Корзина':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('Добавить приборы')
        btn2 = types.KeyboardButton('Изменить кол-во приборов')
        btn3 = types.KeyboardButton('Оставить у двери')
        btn4 = types.KeyboardButton('Скидка в корзине')
        btn5 = types.KeyboardButton('Сколько оплачено деньгами/бонусами')
        btn6 = types.KeyboardButton('Оплата бонусами')
        btn7 = types.KeyboardButton('Привязать карту')
        btn8 = types.KeyboardButton('Добавить к заказу')
        btn9 = types.KeyboardButton('Вернуться на главную')
        markup.add(btn1, btn2, btn3, btn4, btn5, btn6, btn7, btn8, btn9)
        bot.send_message(message.from_user.id, "Выбери скрин", reply_markup=markup)

    elif message.text == 'Вернуться на главную':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('Профиль и регистрация')
        btn2 = types.KeyboardButton('Меню')
        btn3 = types.KeyboardButton ('Адрес')
        btn4 = types.KeyboardButton ('Корзина')
        btn5 = types.KeyboardButton ('Заказ')
        btn6 = types.KeyboardButton ('Скидка сотрудника')
        btn7 = types.KeyboardButton ('Тестовая группа')
        btn8 = types.KeyboardButton ('Замены')
        markup.add(btn1, btn2, btn3, btn4, btn5, btn6, btn7, btn8)
        bot.send_message(message.from_user.id, 'Йоу! Какой скрин нужен?', reply_markup=markup)

    elif message.text == 'Добавить приборы':
        bot.send_message(message.from_user.id, 'Нажать темносерую плашку внизу экрана → «+» около позиции «Приборы» после списка блюд ')
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('Назад')
        markup.add(btn1)

    elif message.text == 'Изменить кол-во приборов':
        bot.send_message(message.from_user.id, 'Нажать темносерую плашку внизу экрана → «+» или «-» около позиции «Приборы» после списка блюд ')
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('Назад')
        markup.add(btn1)
 
    elif message.text == 'Оставить у двери':
        bot.send_message(message.from_user.id, 'В корзине нужно сдвинуть ползунок «Оставить у двери»')
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('Назад')
        markup.add(btn1)

    elif message.text == 'Скидка в корзине':
        bot.send_message(message.from_user.id, 'В корзине, над кнопкой «Заказать на», будет указана скидка, ее номинал и стоимость в рублях, которую покрывает ')
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('Назад')
        markup.add(btn1)

    elif message.text == 'Сколько оплачено деньгами/бонусами':
        bot.send_message(message.from_user.id, 'В корзине, над кнопкой «Заказать на», указано, сколько у вас бонусов, какая часть будет оплачена деньгами с их учетом')
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('Назад')
        markup.add(btn1)

    elif message.text == 'Оплата бонусами':
        bot.send_message(message.from_user.id, 'В корзине включить ползунок «Оплатить бонусами»')
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('Назад')
        markup.add(btn1)

    elif message.text == 'Привязать карту':
        bot.send_message(message.from_user.id, 'В корзине нажать на «Заказать на» → Ввести реквизиты → Нажать «Оплатить»')
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('Назад')
        markup.add(btn1)

    elif message.text == 'Добавить к заказу':
        bot.send_message(message.from_user.id, 'Нужно перейти в корзину и нажать на нужную позицию в разделе Добавить к заказу')
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('Назад')
        markup.add(btn1)

    elif message.text == 'Назад':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('Первый адрес')
        btn2 = types.KeyboardButton('Изменить адрес')
        btn3 = types.KeyboardButton('Добавить еще один адрес')
        btn4 = types.KeyboardButton('Изменить комментарий(один адрес)')
        btn5 = types.KeyboardButton('Изменить комментарий (2 и более адресов)')
        btn6 = types.KeyboardButton('Удалить адрес')
        btn7 = types.KeyboardButton('Вернуться на главную')
        markup.add(btn1, btn2, btn3, btn4, btn5, btn6, btn7)
        bot.send_message(message.from_user.id, "Выбери скрин", reply_markup=markup)

    elif message.text == 'Заказ':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('Приборы после заказа')
        btn2 = types.KeyboardButton('Сколько оплачено деньгами/бонусами')
        btn3 = types.KeyboardButton('Отменить заказ')
        btn4 = types.KeyboardButton('Донатсы')
        btn5 = types.KeyboardButton('Чек заказа')
        btn6 = types.KeyboardButton('Трекер со статусом заказа')
        btn7 = types.KeyboardButton('Вернуться на главную')
        markup.add(btn1, btn2, btn3, btn4, btn5, btn6, btn7)
        bot.send_message(message.from_user.id, "Выбери скрин", reply_markup=markup)

    elif message.text == 'Вернуться на главную':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('Профиль и регистрация')
        btn2 = types.KeyboardButton('Меню')
        btn3 = types.KeyboardButton ('Адрес')
        btn4 = types.KeyboardButton ('Корзина')
        btn5 = types.KeyboardButton ('Заказ')
        btn6 = types.KeyboardButton ('Скидка сотрудника')
        btn7 = types.KeyboardButton ('Тестовая группа')
        btn8 = types.KeyboardButton ('Замены')
        markup.add(btn1, btn2, btn3, btn4, btn5, btn6, btn7, btn8)
        bot.send_message(message.from_user.id, 'Йоу! Какой скрин нужен?', reply_markup=markup)

    elif message.text == 'Приборы после заказа':
        bot.send_message(message.from_user.id, 'Нажать на желтую плашку внизу экрана → Под списком блюд в заказе нажать на «+» справа от приборов → добавить нужное количество → нажать кнопку «Сохранить»')
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('Назад')
        markup.add(btn1)

    elif message.text == 'Сколько оплачено деньгами/бонусами':
        bot.send_message(message.from_user.id, 'Нажать на значок человечка в левом верхнем углу → экран личного профиля → раздел Заказы → выбрать нужный. В его карточке будет указано, какая сумма была оплачена деньгами и бонусами ')
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('Назад')
        markup.add(btn1)

    elif message.text == 'Отменить заказ':
        bot.send_message(message.from_user.id, 'Нажать на желтый трекер заказа в статусе Оплачен, а далее на кнопку «Отменить заказ»')
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('Назад')
        markup.add(btn1)

    if message.text == 'Донатсы':
        bot.send_message(message.from_user.id, 'Нажать на изображение профиля или значок человечка/фотоаппарата в левом верхнем углу → раздел Заказы → выбрать нужный → на баннере оценки заказа поставить палец вверх → выбрать или указать сумму → нажать «Отправить»')
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('Назад')
        markup.add(btn1)

    elif message.text == 'Чек заказа':
        bot.send_message(message.from_user.id, 'Нажать на изображение профиля или значок человечка/фотоаппарата в левом верхнем углу → раздел Заказы → выбрать нужный → нажать на значок чека в правом верхнем углу')
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('Назад')
        markup.add(btn1)

    elif message.text == 'Трекер со статусом заказа':
        bot.send_message(message.from_user.id, 'Желтая плашки внизу экрана')
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('Назад')
        markup.add(btn1)

    elif message.text == 'Назад':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('Первый адрес')
        btn2 = types.KeyboardButton('Изменить адрес')
        btn3 = types.KeyboardButton('Добавить еще один адрес')
        btn4 = types.KeyboardButton('Изменить комментарий(один адрес)')
        btn5 = types.KeyboardButton('Изменить комментарий (2 и более адресов)')
        btn6 = types.KeyboardButton('Удалить адрес')
        btn7 = types.KeyboardButton('Вернуться на главную')
        markup.add(btn1, btn2, btn3, btn4, btn5, btn6, btn7)
        bot.send_message(message.from_user.id, "Выбери скрин", reply_markup=markup)

    elif message.text == 'Скидка сотрудника':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('Вкл/выкл скидку')
        btn2 = types.KeyboardButton('Сколько оплачено компанией')
        btn3 = types.KeyboardButton('Вернуться на главную')
        markup.add(btn1, btn2, btn3)
        bot.send_message(message.from_user.id, "Выбери скрин", reply_markup=markup)

    elif message.text == 'Вернуться на главную':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('Профиль и регистрация')
        btn2 = types.KeyboardButton('Меню')
        btn3 = types.KeyboardButton ('Адрес')
        btn4 = types.KeyboardButton ('Корзина')
        btn5 = types.KeyboardButton ('Заказ')
        btn6 = types.KeyboardButton ('Скидка сотрудника')
        btn7 = types.KeyboardButton ('Тестовая группа')
        btn8 = types.KeyboardButton ('Замены')
        markup.add(btn1, btn2, btn3, btn4, btn5, btn6, btn7, btn8)
        bot.send_message(message.from_user.id, 'Йоу! Какой скрин нужен?', reply_markup=markup)

    elif message.text == 'Вкл/выкл скидку':
        bot.send_message(message.from_user.id, 'Нужно выбрать Способы оплаты в Корзине или Профиле и переключить тумблер')
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('Назад')
        markup.add(btn1)

    elif message.text == 'Сколько оплачено компанией':
        bot.send_message(message.from_user.id, 'Информация отображается в Корзине, сразу под блоком «Добавить к заказу». Там указываем, какую сумму взяла на себя компания, и какую спишем с карты. После оплаты это можно проверить в разделе Заказы')
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('Назад')
        markup.add(btn1)

    elif message.text == 'Назад':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('Первый адрес')
        btn2 = types.KeyboardButton('Изменить адрес')
        btn3 = types.KeyboardButton('Добавить еще один адрес')
        btn4 = types.KeyboardButton('Изменить комментарий(один адрес)')
        btn5 = types.KeyboardButton('Изменить комментарий (2 и более адресов)')
        btn6 = types.KeyboardButton('Удалить адрес')
        btn7 = types.KeyboardButton('Вернуться на главную')
        markup.add(btn1, btn2, btn3, btn4, btn5, btn6, btn7)
        bot.send_message(message.from_user.id, "Выбери скрин", reply_markup=markup)

    elif message.text == 'Тестовая группа':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('Виджеты бонусов')
        btn2 = types.KeyboardButton('Скидки и бонусы')
        btn3 = types.KeyboardButton('Вернуться на главную')
        markup.add(btn1, btn2, btn3)
        bot.send_message(message.from_user.id, "Выбери скрин", reply_markup=markup)

    elif message.text == 'Вернуться на главную':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('Профиль и регистрация')
        btn2 = types.KeyboardButton('Меню')
        btn3 = types.KeyboardButton ('Адрес')
        btn4 = types.KeyboardButton ('Корзина')
        btn5 = types.KeyboardButton ('Заказ')
        btn6 = types.KeyboardButton ('Скидка сотрудника')
        btn7 = types.KeyboardButton ('Тестовая группа')
        btn8 = types.KeyboardButton ('Замены')
        markup.add(btn1, btn2, btn3, btn4, btn5, btn6, btn7, btn8)
        bot.send_message(message.from_user.id, 'Йоу! Какой скрин нужен?', reply_markup=markup)

    elif message.text == 'Виджеты бонусов':
        bot.send_message(message.from_user.id, 'На левом верхнем виджете показываем, сколько бонусов начисляем. По нажатию на виджет можно перейти на лендинг с условиями. На правом верхнем виджете показываем количество бонусов на счете. По нажатию можно перейти в раздел Бонусы')
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('Назад')
        markup.add(btn1)

    elif message.text == 'Скидки и бонусы':
        bot.send_message(message.from_user.id, 'Скидка в корзине и Сумма заказа с учетом скидки')
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('Назад')
        markup.add(btn1)

    elif message.text == 'Назад':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('Первый адрес')
        btn2 = types.KeyboardButton('Изменить адрес')
        btn3 = types.KeyboardButton('Добавить еще один адрес')
        btn4 = types.KeyboardButton('Изменить комментарий(один адрес)')
        btn5 = types.KeyboardButton('Изменить комментарий (2 и более адресов)')
        btn6 = types.KeyboardButton('Удалить адрес')
        btn7 = types.KeyboardButton('Вернуться на главную')
        markup.add(btn1, btn2, btn3, btn4, btn5, btn6, btn7)
        bot.send_message(message.from_user.id, "Выбери скрин", reply_markup=markup)

    elif message.text == 'Замены':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('Выбрать блюдо')
        btn2 = types.KeyboardButton('Сбросить блюдо')
        btn3 = types.KeyboardButton('Выбрать бонусы')
        btn4 = types.KeyboardButton('Вернуться на главную')
        markup.add(btn1, btn2, btn3, btn4)
        bot.send_message(message.from_user.id, "Выбери скрин", reply_markup=markup)

    elif message.text == 'Вернуться на главную':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('Профиль и регистрация')
        btn2 = types.KeyboardButton('Меню')
        btn3 = types.KeyboardButton ('Адрес')
        btn4 = types.KeyboardButton ('Корзина')
        btn5 = types.KeyboardButton ('Заказ')
        btn6 = types.KeyboardButton ('Скидка сотрудника')
        btn7 = types.KeyboardButton ('Тестовая группа')
        btn8 = types.KeyboardButton ('Замены')
        markup.add(btn1, btn2, btn3, btn4, btn5, btn6, btn7, btn8)
        bot.send_message(message.from_user.id, 'Йоу! Какой скрин нужен?', reply_markup=markup)

    elif message.text == 'Скидки и бонусы':
        bot.send_message(message.from_user.id, 'Нажать «Выбрать замену» → затем «На это» справа от блюда → «Готово» в правом верхнем углу')
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('Назад')
        markup.add(btn1)

    elif message.text == 'Сбросить блюдо':
        bot.send_message(message.from_user.id, 'Нажать на кнопку «Сбросить» в левом верхнем углу. После этого снова можно будет выбрать любое блюдо')
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('Назад')
        markup.add(btn1)

    elif message.text == 'Выбрать бонусы':
        bot.send_message(message.from_user.id, 'Под кнопкой «Выбрать замену» нажать на «Вернуть стоимость блюда». Она вернется на бонусный счет')
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('Назад')
        markup.add(btn1)

    elif message.text == 'Назад':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('Первый адрес')
        btn2 = types.KeyboardButton('Изменить адрес')
        btn3 = types.KeyboardButton('Добавить еще один адрес')
        btn4 = types.KeyboardButton('Изменить комментарий(один адрес)')
        btn5 = types.KeyboardButton('Изменить комментарий (2 и более адресов)')
        btn6 = types.KeyboardButton('Удалить адрес')
        btn7 = types.KeyboardButton('Вернуться на главную')
        markup.add(btn1, btn2, btn3, btn4, btn5, btn6, btn7)
        bot.send_message(message.from_user.id, "Выбери скрин", reply_markup=markup)

bot.polling(none_stop=True, interval=0) 