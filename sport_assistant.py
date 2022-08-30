import telebot
from telebot import types
import psycopg2
from config import host, user, password, db_name, token


bot = telebot.TeleBot(token)


try:
    connection = psycopg2.connect(
        host=host,
        user=user,
        password=password,
        database=db_name
    )
    connection.autocommit = True

    # Реакция на сообщение старт. Отображает кнопки.


    @bot.message_handler(commands=['start'])
    def star_menu(m):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        item1 = types.KeyboardButton("🏋️‍♀️Посмотреть данные о последних тренировках")
        item2 = types.KeyboardButton("📝 Внести данные тренировки")
        markup.add(item1)
        markup.add(item2)
        bot.send_message(m.chat.id, 'Выберите подходящую опцию', reply_markup=markup)

    # Реакция на текстовые сообщения

    @bot.message_handler(content_types=["text"])
    def start_message(message):
        with connection.cursor() as cursor:
            if message.text.strip() == '🏋️‍♀️Посмотреть данные о последних тренировках':
                markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
                item1 = types.KeyboardButton("🏋️‍♂️Последняя тренировка на трицепс и грудь")
                item2 = types.KeyboardButton("🏋️‍♂️Последняя тренировка на бицепс и спину")
                item3 = types.KeyboardButton("🏋️‍♂️Последняя тренировка на плечи")
                item5 = types.KeyboardButton("🏋️‍♂️Последняя тренировка ")
                item4 = types.KeyboardButton("🔙 Назад")
                markup.add(item1)
                markup.add(item2)
                markup.add(item3)
                markup.add(item5, item4)

                bot.send_message(message.chat.id, 'Нажмите кнопку для получения актуальной информации',
                                 reply_markup=markup)
            if message.text.strip() == "🏋️‍♂️Последняя тренировка":
                cursor.execute(
                    '''select name_of_training
                    from training t inner join exercises e2 on t.id = e2.id_training 
                    where e2.date_of_training =  (select max(date_of_training) from exercises e);                                  
                    '''
                )

                bot.send_message(message.chat.id, f'Последняя тренировка: {cursor.fetchone()[0]}\n')

            if message.text.strip() == '🏋️‍♂️Последняя тренировка на трицепс и грудь':
                bot.send_message(message.chat.id, 'Последняя тренировка на трицепс и грудь')
                cursor.execute(
                    '''select  name_of_exercises,
                    date_of_training,
                    operating_weight,
                    number_of_repetitions
                    from 
                    public.exercises 
                    where id_training = 1 and date_of_training = (select date_of_training from exercises 
                    where id_training = '1' 
                    group by date_of_training 
                    order by 1 desc 
                    limit 1);               
                    '''
                )
                query = cursor.fetchall()
                for i in range(len(query)):
                    bot.send_message(message.chat.id, f'Упражнение: {query[i][0]}\n'
                                                      f'Дата: {query[i][1]}\n'
                                                      f'Рабочий вес: {query[i][2]}\n'
                                                      f'Количество повторений: {query[i][3]}')
            if message.text.strip() == '🏋️‍♂️Последняя тренировка на бицепс и спину':
                bot.send_message(message.chat.id, 'Последняя тренировка на бицепс и спину')
                cursor.execute(
                    '''select  name_of_exercises,
                    date_of_training,
                    operating_weight,
                    number_of_repetitions
                    from 
                    public.exercises 
                    where id_training = 2 and date_of_training = (select date_of_training from exercises 
                    where id_training = '2' 
                    group by date_of_training 
                    order by 1 desc 
                    limit 1);               
                    '''
                )
                query = cursor.fetchall()
                for i in range(len(query)):
                    bot.send_message(message.chat.id, f'Упражнение: {query[i][0]}\n'
                                                      f'Дата: {query[i][1]}\n'
                                                      f'Рабочий вес: {query[i][2]}\n'
                                                      f'Количество повторений: {query[i][3]}')
            if message.text.strip() == '🏋️‍♂️Последняя тренировка на плечи':
                bot.send_message(message.chat.id, 'Последняя тренировка на плечи')
                cursor.execute(
                    '''select  name_of_exercises,
                    date_of_training,
                    operating_weight,
                    number_of_repetitions
                    from 
                    public.exercises 
                    where id_training = 3 and date_of_training = (select date_of_training from exercises 
                    where id_training = '3' 
                    group by date_of_training 
                    order by 1 desc 
                    limit 1);               
                    '''
                )
                query = cursor.fetchall()
                for i in range(len(query)):
                    bot.send_message(message.chat.id, f'Упражнение: {query[i][0]}\n'
                                                      f'Дата: {query[i][1]}\n'
                                                      f'Рабочий вес: {query[i][2]}\n'
                                                      f'Количество повторений: {query[i][3]}')
            if message.text.strip() == '🔙 Назад':
                markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
                item1 = types.KeyboardButton("🏋️‍♀️Посмотреть данные о последних тренировках")
                item2 = types.KeyboardButton("📝 Внести данные тренировки")
                markup.add(item1)
                markup.add(item2)
                bot.send_message(message.chat.id, 'Выберите подходящую опцию', reply_markup=markup)
            if message.text.strip() == '📝 Внести данные тренировки':
                markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
                item1 = types.KeyboardButton("🏋️‍♂️Тренировка на трицепс и грудь")
                item2 = types.KeyboardButton("🏋️‍♂️Тренировка на бицепс и спину")
                item3 = types.KeyboardButton("🏋️‍♂️Тренировка на плечи")
                item4 = types.KeyboardButton("🔙 Назад")
                markup.add(item1)
                markup.add(item2)
                markup.add(item3)
                markup.add(item4)
                bot.send_message(message.chat.id, 'Выберите подходящий вариант', reply_markup=markup)
            if message.text.strip() == "🏋️‍♂️Тренировка на трицепс и грудь":
                markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
                item1 = types.KeyboardButton("🏋️‍♂️Разгибание гантели из-за головы")
                item2 = types.KeyboardButton("🏋️‍♂️Жим гантелей")
                item3 = types.KeyboardButton("🏋️‍♂️Разгибание рук в наклоне")
                item4 = types.KeyboardButton("🏋️‍♂️Разведение гантелей")
                item5 = types.KeyboardButton("🏋️‍♂️Обратные отжимания от скамьи")
                item6 = types.KeyboardButton("🏋️‍♂️Отжимания от пола")
                item7 = types.KeyboardButton("🔙 Назад")
                markup.add(item1)
                markup.add(item2)
                markup.add(item3)
                markup.add(item4)
                markup.add(item5)
                markup.add(item6)
                markup.add(item7)
                id_training = 1
                name_of_exercises = bot.send_message(message.chat.id, 'Выберите название упражнения',
                                                     reply_markup=markup)
                bot.register_next_step_handler(name_of_exercises, start_3, id_training)
            if message.text.strip() == "🏋️‍♂️Тренировка на бицепс и спину":
                markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
                item1 = types.KeyboardButton("🏋️‍♂️Тяга гантелей в наклоне")
                item2 = types.KeyboardButton("🏋️‍♂️Подъем на бицепс стоя")
                item3 = types.KeyboardButton("🏋️‍♂️Подъем веса к груди с опорой на скамью")
                item4 = types.KeyboardButton("🏋️‍♂️Концентрированный подъем на бицепс сидя")
                item5 = types.KeyboardButton("🏋️‍♂️Тяга + подъем гантель")
                item6 = types.KeyboardButton("🏋️‍♂️Подъемы на бицепс «молот»")
                item7 = types.KeyboardButton("🔙 Назад")
                markup.add(item1)
                markup.add(item2)
                markup.add(item3)
                markup.add(item4)
                markup.add(item5)
                markup.add(item6)
                markup.add(item7)
                id_training = 2
                name_of_exercises = bot.send_message(message.chat.id, 'Выберите название упражнения',
                                                     reply_markup=markup)
                bot.register_next_step_handler(name_of_exercises, start_3, id_training)
            if message.text.strip() == "🏋️‍♂️Тренировка на плечи":
                markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
                item1 = types.KeyboardButton("🏋️‍♂️Жим гантель стоя")
                item2 = types.KeyboardButton("🏋️‍♂️Подъем гантелей перед собой")
                item3 = types.KeyboardButton("🏋️‍♂️Разведение гантелей в стороны")
                item4 = types.KeyboardButton("🏋️‍♂️Тяга веса к подбородку")
                item5 = types.KeyboardButton("🏋️‍♂️Параллельный жим стоя")
                item6 = types.KeyboardButton("🏋️‍♂️Разведение гантелей в наклоне")
                item7 = types.KeyboardButton("🔙 Назад")
                markup.add(item1)
                markup.add(item2)
                markup.add(item3)
                markup.add(item4)
                markup.add(item5)
                markup.add(item6)
                markup.add(item7)
                id_training = 3
                name_of_exercises = bot.send_message(message.chat.id, 'Выберите название упражнения',
                                                     reply_markup=markup)
                bot.register_next_step_handler(name_of_exercises, start_3, id_training)

    # Если пользователь хочет внести данные в БД, то дальнейшие функции Start 2-6,
    # позволяют перехватывать сообщение от пользователя и в конце запросом к БД добавляет данные одной записью.
    def start_3(name_of_exercises, id_training):
        date_of_training = bot.send_message(name_of_exercises.chat.id, 'Введите дату в формате дд-мм-гггг')
        bot.register_next_step_handler(date_of_training, start_4, name_of_exercises.text, id_training)

    def start_4(date_of_training, name_of_exercises, id_training):
        operating_weight = bot.send_message(date_of_training.chat.id, 'Введите рабочий вес( в кг)')
        bot.register_next_step_handler(operating_weight, start_5, date_of_training.text, name_of_exercises, id_training)

    def start_5(operating_weight, date_of_training, name_of_exercises, id_training):
        number_of_repetitions = bot.send_message(operating_weight.chat.id, 'Введите количество повторов')
        bot.register_next_step_handler(number_of_repetitions, start_6, operating_weight.text, date_of_training,
                                       name_of_exercises, id_training)

    def start_6(number_of_repetitions, operating_weight, date_of_training, name_of_exercises, id_training):
        try:
            with connection.cursor() as cursor:
                cursor.execute(
                    f'''insert into exercises (
                    id_training,
                    name_of_exercises,
                    date_of_training,
                    operating_weight,
                    number_of_repetitions) 
                    values ({id_training},
                            '{name_of_exercises}',
                            '{date_of_training}',
                            {operating_weight},
                            {number_of_repetitions.text});               
                    '''
                )

            bot.send_message(number_of_repetitions.chat.id, f'Упражнение: {name_of_exercises}\n'
                                                            f'Дата: {date_of_training}\n'
                                                            f'Рабочий вес: {operating_weight}\n'
                                                            f'Количество повторений: {number_of_repetitions.text}\n'
                                                            f'id_training:{id_training}')
            bot.send_message(number_of_repetitions.chat.id, 'Данные добавлены!')

            bot.register_next_step_handler(number_of_repetitions, star_menu)
        except Exception as exce:
            print('Ошибка! Данные не добавлены!', exce)
            bot.send_message(number_of_repetitions.chat.id, 'Ошибка! Данные не добавлены!')
            bot.register_next_step_handler(number_of_repetitions, star_menu)

    bot.infinity_polling(none_stop=True, interval=0)
except Exception as ex:
    print("Ошибка при работе с postgresql", ex)
finally:
    if connection:
        connection.close()
        print('Подключение к Postresql остановлено')
