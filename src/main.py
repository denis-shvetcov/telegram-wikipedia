import telebot


# Token from @BotFather
API_TOKEN = 'YOUR_TOKEN'

if __name__ == "__main__":
    # Creating the bot
    bot = telebot.TeleBot(token=API_TOKEN)

    # Handling /start command
    @bot.message_handler(commands=['start'])
    def welcome(message):
        chat_id = message.chat.id  # Getting id of the chat

        # Welcome message
        bot.send_message(chat_id,
                         "Nice to meet you, {0.first_name}!\n"
                         "My name is TelepediaBot, I am a bot that lets you search wikipedia articles right in this "
                         "chat.\n"
                         "Consider me you personal wikipedia😉.\n"
                         "\nType any word and let's start learning!"""
                         "\n\n<b>Available commands:</b>"
                         "\n/start - initialize the bot".format(message.from_user, bot.get_me()),
                         parse_mode='html')

    # Start
    bot.polling(none_stop=True)
