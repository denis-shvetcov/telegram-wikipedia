import re
import telebot
import wikipedia

# Token from @BotFather
API_TOKEN = 'YOUR_TOKEN'


class WikiBot:
    def __init__(self):
        self.wiki = wikipedia  # wikipedia object


def wikiparse(page):
    wikitext = page.content[:1000]  # message length limit
    wikimas = wikitext.split('.')
    wikimas = wikimas[:-1]
    wikitext2 = ''
    for x in wikimas:
        if not ('==' in x):
            if len((x.strip())) > 3:
                wikitext2 = wikitext2 + x + '.'
        else:
            break
    # Now, using regular expressions, we remove the markup
    wikitext2 = re.sub('\([^()]*\)', '', wikitext2)
    wikitext2 = re.sub('\([^()]*\)', '', wikitext2)
    wikitext2 = re.sub('\{[^\{\}]*\}', '', wikitext2)
    # Returning a text string
    return wikitext2


def getwiki(wiki, text):
    try:
        direct_search = wiki.page(text, auto_suggest=False)
        msg = wikiparse(direct_search)
        return msg
    # Handling an exception that the wikipedia module could return
    except wikipedia.exceptions.DisambiguationError as e:
        opt = e.options
        msg = "Sorry, your query is too ambiguous!\n" \
              "'{0}' may refer to:\n" \
              "\n<b>{1}</b>\n" \
              "<b>{2}</b>\n" \
              "<b>{3}</b>\n" \
              "<b>{4}</b>\n" \
              "<b>{5}</b>\n" \
              "\nTry searching one of the suggestions above.".format(e.title,
                                                                     opt[0],
                                                                     opt[1],
                                                                     opt[2],
                                                                     opt[3],
                                                                     opt[4])
        return msg
    except wikipedia.exceptions.PageError:
        try:
            suggest_search = wiki.page(text, auto_suggest=True)
            msg = wikiparse(suggest_search)
            return msg
        except wikipedia.exceptions.PageError:
            return 'Sorry, I can\'t find anything on the subject????.'


if __name__ == "__main__":
    # Creating the bot
    bot = telebot.TeleBot(token=API_TOKEN)
    # For multiuser support, will contain chat ids, as well as current wiki language
    current_chats = {}

    # Handling /start command
    @bot.message_handler(commands=['start'])
    def welcome(message):
        chat_id = message.chat.id  # Getting id of the chat

        wb = WikiBot()
        current_chats[chat_id] = wb
        current_chats[chat_id].wiki.set_lang("en")  # set default language

        # Welcome message
        bot.send_message(chat_id,
                         "Nice to meet you, {0.first_name}!\n"
                         "My name is TelepediaBot, I am a bot that lets you search wikipedia articles right in this "
                         "chat.\n"
                         "Consider me you personal wikipedia????.\n"
                         "\nType any word and let's start learning!"""
                         "\n\n<b>Available commands:</b>"
                         "\n/start - initialize the bot"
                         "\n/help - to see available commands"
                         "\n/eng - search articles in English"
                         "\n/rus - search articles in Russian".format(message.from_user, bot.get_me()),
                         parse_mode='html')

    # Handling /help command
    @bot.message_handler(commands=['help'])
    def command_help(message):
        chat_id = message.chat.id  # Getting id of the chat
        bot.send_message(chat_id, "\n\n<b>Available commands:</b>"
                                  "\n/start - initialize the bot"
                                  "\n/help - to see available commands"
                                  "\n/eng - search articles in English (default)"
                                  "\n/rus - search articles in Russian",
                         parse_mode='html')

    # Handling /ru command
    @bot.message_handler(commands=['rus'])
    def change_lang_ru(message):
        chat_id = message.chat.id  # Getting id of the chat
        if chat_id not in current_chats.keys():
            bot.send_message(chat_id, "Please initialize chat with /start")
        else:
            current_chats[chat_id].wiki.set_lang("ru")
            bot.send_message(chat_id, "Changed wikipedia language to Russian")

    # Handling /eng command
    @bot.message_handler(commands=['eng'])
    def change_lang_ru(message):
        chat_id = message.chat.id  # Getting id of the chat
        if chat_id not in current_chats.keys():
            bot.send_message(chat_id, "Please use the /start command to begin the chat")
        else:
            current_chats[chat_id].wiki.set_lang("en")
            bot.send_message(chat_id, "Changed wikipedia language to English")

    # Handling incoming messages
    @bot.message_handler(content_types=['text'])
    def get_text_messages(message):
        chat_id = message.chat.id  # Getting id of the chat
        if chat_id not in current_chats.keys():
            bot.send_message(chat_id, "Please use the /start command to begin the chat")
        else:
            msg = getwiki(current_chats[chat_id].wiki, message.text)
            bot.send_message(chat_id, msg, parse_mode='html')


    # Start
    bot.polling(none_stop=True)
