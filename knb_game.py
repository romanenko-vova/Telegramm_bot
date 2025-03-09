from telegram import (
    Update,
    ReplyKeyboardMarkup,
)
from telegram.ext import (
    ContextTypes,

)
import random


from states import KNB


async def knb_start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    Keyboard = [["камень", "ножницы", "бумага", "выход"]]
    markup = ReplyKeyboardMarkup(Keyboard)
    await context.bot.send_message(
        chat_id=update.effective_chat.id,
        text=f"{update.effective_user.first_name}! ты попал в игру камень ножницы бумагу",
        reply_markup=markup,
    )
    return KNB


async def knb_game(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text_user = update.effective_message.text
    comp_choise = ["бумага", "камень", "ножницы"]
    n = random.randint(0, 2)
    print(comp_choise[n])
    if text_user == "бумага" and comp_choise[n] == "ножницы":
        await context.bot.send_message(
            chat_id=update.effective_chat.id, text="ты проиграл ,я выбрал ножницы"
        )

    elif text_user == "бумага" and comp_choise[n] == "бумага":
        await context.bot.send_message(
            chat_id=update.effective_chat.id, text="ничья ,я выбрал бумагу"
        )
    elif text_user == "бумага" and comp_choise[n] == "камень":
        await context.bot.send_message(
            chat_id=update.effective_chat.id, text="ты выйграл ,я выбрал камень"
        )
    if text_user == "ножницы" and comp_choise[n] == "бумага":
        await context.bot.send_message(
            chat_id=update.effective_chat.id, text="ты выйграл ,я выбрал бумагу"
        )
    elif text_user == "ножницы" and comp_choise[n] == "ножницы":
        await context.bot.send_message(
            chat_id=update.effective_chat.id, text="ничья ,я выбрал ножницы"
        )
    elif text_user == "ножницы" and comp_choise[n] == "камень":
        await context.bot.send_message(
            chat_id=update.effective_chat.id, text="я выйграл ,я выбрал камень"
        )
    if text_user == "камень" and comp_choise[n] == "бумага":
        await context.bot.send_message(
            chat_id=update.effective_chat.id, text="я выйграл ,я выбрал бумагу"
        )
    elif text_user == "камень" and comp_choise[n] == "камень":
        await context.bot.send_message(
            chat_id=update.effective_chat.id, text="ничья ,я выбрал камень"
        )
    elif text_user == "камень" and comp_choise[n] == "ножницы":
        await context.bot.send_message(
            chat_id=update.effective_chat.id, text="я проиграл ,я выбрал ножницы"
        )