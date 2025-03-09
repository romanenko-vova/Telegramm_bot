from telegram import (
    Update,
)
from telegram.ext import (
    ContextTypes,
    
)
from telegram.constants import ParseMode

from states import KNZ,MAINMENU


def get_board_st(board):
    st = "-" * 13
    for i in range(0, 7, 3):
        st += f"\n| {board[i]} | {board[i + 1]} | {board[i + 2]} |\n"
        st += "-" * 13
    return f"`{st}`"


async def knz_start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    board = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
    context.user_data["board"] = board
    hod = 1
    context.user_data["hod"] = hod
    await context.bot.send_message(
        chat_id=update.effective_chat.id,
        text="ты попал в игру крестики нолики!\n\nПРАВИЛА ИГРЫ\n\nвам отпровляется игровое поле с номерами в каждой клетке и вам нужно выбрать куда вы поставите крестик или нолик(для этого у вас будет клавиотура) выбрали, на клетке которую вы выбрали ставится крестик или нолик а дальше всё как в обычных крестиках и ноликах. кто первый поставит свои фигуры 3 в ряд тот и победил!\n\n удачи!",
    )
    await context.bot.send_message(
        chat_id=update.effective_chat.id,
        text=get_board_st(board),
        parse_mode=ParseMode.MARKDOWN_V2,
    )
    await context.bot.send_message(
        chat_id=update.effective_chat.id, text="куда вы хотите поставить крестик?"
    )

    return KNZ


async def knz_game(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text_user = int(update.effective_message.text)
    if text_user > 9 or text_user < 1:
        await context.bot.send_message(
            chat_id=update.effective_chat.id, text="ты выбрал плохое число"
        )
        return KNZ

    if context.user_data["hod"] % 2 == 0:
        figure = "O"
    else:
        figure = "X"

    if context.user_data["board"][text_user - 1] in "XO":
        await context.bot.send_message(
            chat_id=update.effective_chat.id, text="выбери заново пж"
        )
        return KNZ

    context.user_data["board"][text_user - 1] = figure
    await context.bot.send_message(
        chat_id=update.effective_chat.id,
        text=get_board_st(context.user_data["board"]),
        parse_mode=ParseMode.MARKDOWN_V2,
    )
    res = check_winner(context.user_data['board']) # None | 'X' | 'O'
    if res is not None:
        if res in "XO":
            await context.bot.send_message(
            chat_id=update.effective_chat.id, text=f"победил{res}\n  напиши /start чтобы выбрать другую игру "
        )
            return MAINMENU
    else:
        if context.user_data["hod"] == 9:
            await context.bot.send_message(
            chat_id=update.effective_chat.id, text="Ничья"
        )
            return MAINMENU
    context.user_data["hod"] += 1


def check_winner(board):
    if board[0] == board[1] == board[2]:
        return board[0]
    else:
        return None
        