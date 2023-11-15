import telebot

"""бот заказан компанией, обслуживающей лифты, логика работы простейшая - бот интегрируется в чаты жильцов 
многоквартирных домов, и как только в чате упоминается слово 'лифт' - пользователю по его id приходит
сообщение о том что слово 'лифт' обнаружено в 'таком-то' чате"""


# Замените 'YOUR_BOT_TOKEN' на токен вашего бота
bot_token = 'YOUR_BOT_TOKEN'
bot = telebot.TeleBot(bot_token)


@bot.message_handler(func=lambda message: True, content_types=['text'])
def handle_messages(message):
    # Проверяем, является ли сообщение из группового чата и содержит ли ключевое слово "лифт"
    # if message.chat.type == 'group' and 'лифт' in message.text.lower():
    if 'лифт' in message.text.lower():
        # Отправляем уведомление другому контакту
        send_notification(message)


@bot.message_handler()
def send_notification(message):
    try:
        # Получаем информацию о чате
        chat_info = bot.get_chat(message.chat.id)
        chat_title = chat_info.title

        # Формируем сообщение с информацией о чате
        notification_text = f"Обнаружено ключевое слово 'лифт' в чате '{chat_title}' ({message.chat.id})."

        # Замените 'TARGET_USER_ID' на ID пользователя (просто число, без кавычек!),
        # которому будет отправлено уведомление
        target_user_id = 'TARGET_USER_ID'

        # Отправляем уведомление целевому пользователю
        bot.send_message(target_user_id, notification_text)
    except Exception as e:
        print(f"Ошибка при отправке уведомления: {e}")


if __name__ == "__main__":
    # Запускаем бота
    bot.polling(none_stop=True)



