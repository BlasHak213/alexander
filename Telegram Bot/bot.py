import telebot
from config import keys, TOKEN
from utils import ConvertionException, CryptoConverter


bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start', 'help'])
def start_help(message: telebot.types.Message):
    text = f'Приветствую,  {message.chat.username}. \nЧтобы начать работу, введите команду в формате: \
\n<конвертируемая валюта> <требуемая валюта> <сумма> \
\nДля просмотра доступных валют введите команду /values'
    bot.reply_to(message, text)

@bot.message_handler(commands=['values'])
def values(message: telebot.types.Message):
    text = 'Доступные валюты:'
    for key in keys.keys():
        text = '\n'.join((text, key))
    bot.reply_to(message, text)

@bot.message_handler(content_types=['text'])
def convert(message: telebot.types.Message):
    try:
        values = message.text.split(' ')

        if len(values) != 3:
            raise ConvertionException('Укажите три параметра')

        quote, base, amount = values
        total_base = CryptoConverter.convert(quote, base, amount)
    except ConvertionException as e:
        bot.reply_to(message, f'Ошибка пользователя \n{e}')
    except Exception as e:
        bot.reply_to(message, f'Не удалось обработать команду \n{e}')
    else:
        text = f'Цена {amount} {quote} в {base} - {total_base*float(amount)}'
        bot.send_message(message.chat.id, text)


bot.polling()