from telegram import (
    Update,
    ReplyKeyboardRemove,
    InlineKeyboardButton,
    InlineKeyboardMarkup,
)
from telegram.ext import (
    ContextTypes,

)


from states import MAINMENU

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    Keyboard = [
        [InlineKeyboardButton("камнь ножницы бумгага", callback_data="knb")],
        [InlineKeyboardButton("крестики нолики", callback_data="knz")],
        [InlineKeyboardButton("статистика", callback_data="state")],
        [InlineKeyboardButton("быки коровы ", callback_data="bak")]
    ]
    markup = InlineKeyboardMarkup(Keyboard)
    query = update.callback_query
    if query:
        await query.edit_message_text(
            text=f"Привет,{update.effective_user.first_name}!Давай поиграем в камень ножницы бумагу , ты первый, кстати я о тебе многое знаю твое ади:{update.effective_user.id}твое имя:{update.effective_user.first_name}твоя иконка:{update.effective_user.get_profile_photos}твой язык:{update.effective_user.language_code}  твое последнее имя:{update.effective_user.last_name}  ну так что ходишь?",
            reply_markup=markup,
        )
    else:
        await context.bot.send_message(
            chat_id=update.effective_chat.id,
            text=f"Привет,{update.effective_user.first_name}!Давай поиграем в камень ножницы бумагу , ты первый, кстати я о тебе многое знаю твое ади:{update.effective_user.id}твое имя:{update.effective_user.first_name}твоя иконка:{update.effective_user.get_profile_photos}твой язык:{update.effective_user.language_code}  твое последнее имя:{update.effective_user.last_name}  ну так что ходишь?",
            reply_markup=markup,
        )
        message = await context.bot.send_message(
            chat_id=update.effective_chat.id, text="a", reply_markup=ReplyKeyboardRemove()
        )
        await context.bot.delete_message(
            chat_id=update.effective_chat.id, message_id=message.id
        )
    return MAINMENU

