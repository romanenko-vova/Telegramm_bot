from telegram import (
    Update,
)
from telegram.ext import (
    ContextTypes,
    
)
import random

from states import BAK
from start import start 


def guess_number():
    comp_number= random.randint(1000,9999)
    otvet = check_num(comp_number)
    if otvet == None:
        return guess_number()
    else:
        return otvet

def check_num(num):
    lst = []
    for simvol in str(num):
        lst.appened(int(simvol))
        for i in range(len(lst) - 1):
            for j in range(i +  1, len(lst)):
                if lst[i] == lst[j]:
                    return None 
        return lst
    
def take_input():
    hod = int(input("введите число"))
    otvet = check_num(hod)
    if otvet == None:
        print("ты не прав")
        return take_input()
    else:
        return otvet

def count_bulls_and_cows(g_sp, u_sp):
    bulls = 0
    cows = 0
    for i in range (len(g_sp)):
        if g_sp[i] == u_sp[i]:
            bulls +=1
    for j in range (len(g_sp)):
        for i in range (len(u_sp)):
            pass
    return bulls , cows


async def bac_start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(
        chat_id=update.effective_chat.id,
        text=f"{update.effective_user.first_name}! ты попал в игру быки кровы , напиши четерех значное число",
    )
    g_sp = guess_number()
    context.user_data["g_sp"] = g_sp
    return BAK


async def bac_game(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_input = update.message.text
    update.message.reply_text(f"Вы ввели число: {user_input}")
    g_sp = context.user_update["g_sp"]
    num = int(update.effective_message.text)
    u_sp = check_num(num)
    if u_sp == None:
        await context.bot.send_message(
            chat_id=update.effective_chat.id,
            text="ты ошибаешся слова должны быть уникальны",
        )
        return BAK
    bulls, cows = count_bulls_and_cows(g_sp, u_sp)
    if bulls == 4:
        await context.bot.send_message(
            chat_id=update.effective_chat.id,
            text="Ты угадал.",
        )
        return await start(update, context)
    else:
        await context.bot.send_message(
            chat_id=update.effective_chat.id,
            text=f"быков: bulls\nкоров:{cows}\nНапиши следующее число пж",
        )


if __name__  == "__main__":
    g_sp = guess_number()
    print(g_sp)
    bulls = 0
    while bulls < 4 :
        u_sp = take_input()
        bulls, cows = count_bulls_and_cows(g_sp,u_sp)
        print(f'быков {bulls}\nКоров {cows}')


