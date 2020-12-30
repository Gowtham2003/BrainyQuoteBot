from telegram.ext import Updater, CommandHandler,MessageHandler,Filters
import re
import logging
logging.basicConfig(level=logging.WARNING)
import telegram
from BrainyQuotes import getQuotes
import os


def get_quote(query):
    try:
        data = getQuotes(query)
        quote = data["quote"]
    except:
        return 'Invalid Query , Try Others....\n What About "Technology" ,"Nature" ,"Love" 🙂 '
    author = data["author"]
    qt_link = data["quotelink"]
    auth_link = data["authorlink"]
    quoteImage = data["quoteImage"]

    message = f"{quote} \n {author}"
    dataDict = {"message":message,"img":quoteImage}

    return dataDict


def unknown(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Sorry, I didn't understand that command.")

def quote(update,context):

# if the User Is not A Member of The Channel 
# Bot will not work
# Uncomment to Implement This Feature
#   user=context.bot.get_chat_member(chat_id='-1001497612811',user_id=update.message.chat_id)
#   mem = user["status"]
#   if(mem=='left'):
#       notinChannel = """
#To use to bot you need to be a member of @AlphaProjects in order to stay updated with the latest developments.
#"""
#        context.bot.send_message(chat_id=update.message.chat_id,text=notinChannel)
#        return
    chat_id = update.message.chat_id
    if update.message:  # your bot can receive updates without messages
            # Reply to the message
            query = update.message.text
            data = get_quote(query)
            context.bot.send_message(chat_id=update.effective_chat.id,parse_mode=telegram.ParseMode.MARKDOWN, text=str(data["message"]))
            context.bot.sendPhoto(chat_id=update.effective_chat.id,photo=data["img"])



def start(update,context):
    inf = context.bot.get_chat_member(chat_id='-1001497612811',user_id=update.message.chat_id)
    user = inf["user"]
    first_name = user['first_name']
    last_name = user['last_name']
    if last_name is None:
        last_name = " "
    name =f"Hi! {first_name} {last_name} "
    context.bot.send_message(chat_id=update.effective_chat.id,text=name)

    welcome = """
Hi I'm Brainy Quote Bot

Send /help for Help 

Made With ❤️ In India By @Gowtham_2003

Join @AlphaProjects for More Projects and Updates
"""
    context.bot.send_message(chat_id=update.effective_chat.id,text=
welcome)
#   cht = telegram.Bot.get_chat_member("-1001497612811",chat_id,timeout=None)
    user=context.bot.get_chat_member(chat_id='-1001497612811',user_id=update.message.chat_id)


def help(update,context):
    helpmessage = '''
Send Me Any Topic or Word to Me 

I'll Send You A Quote based On Your Query

For Example : "Nature" , "Tech" , "Alone"   and Even "Hi" and "Hello" 😁 

Type

/help to Get this Message 

/donate To Donate Me (Still Not Added)

if Any Issues Contact : @Gowtham_2003

A Part of @AlphaProjects 

'''
    context.bot.send_message(chat_id=update.effective_chat.id,text=helpmessage)

def donate(update,context):
    donate = '''
Donate Feature Haven't Added Yet 

If You Want to Donate My Works 
Contact Me :
    Telegram : @Gowtham_2003 or @Gowtham2003
'''
    context.bot.send_message(chat_id=update.effective_chat.id,text=donate )

def main():
    updater = Updater(os.environ.get("BOT_TOKEN", ""), use_context=True)
    dp = updater.dispatcher
    start_handler = CommandHandler("start",start)
    dp.add_handler(start_handler)

    help_handler = CommandHandler("help",help)
    dp.add_handler(help_handler)

    donate_handler = CommandHandler("donate",donate)
    dp.add_handler(donate_handler)

    unknown_handler = MessageHandler(Filters.command, unknown)
    dp.add_handler(unknown_handler)

    quote_msg = MessageHandler(Filters.text,quote)
    dp.add_handler(quote_msg)

    updater.start_polling()
    updater.idle()
main()
