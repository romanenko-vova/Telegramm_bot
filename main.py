import logging
from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    MessageHandler,
    filters,
    ConversationHandler,
    CallbackQueryHandler,
)


from inline_button_proc import inline_button_proc
from knz_game import knz_game
from bac_game import bac_game, bac_start
from knb_game import knb_start, knb_game
from rate import my_stat, knb_stat
from states import MAINMENU, KNB, BAK, KNZ, RATE
from start import start


logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)


if __name__ == "__main__":
    application = (
        ApplicationBuilder()
        .token("7731212121:AAE07DCkD3hJKCeViA4qjauqBh2MN6Zp8eA")
        .build()
    )
    conv_handler = ConversationHandler(
        entry_points=[CommandHandler("start", start)],
        states={
            MAINMENU: [
                CommandHandler("knb", knb_start),
                CommandHandler("bac", bac_start),
                CallbackQueryHandler(my_stat, pattern="^state$"),
                CallbackQueryHandler(inline_button_proc),
            ],
            KNB: [
                MessageHandler(
                    filters.TEXT & ~filters.COMMAND,
                    knb_game,
                )
            ],
            BAK: [MessageHandler(filters.TEXT & ~filters.COMMAND, bac_game)],
            KNZ: [MessageHandler(filters.TEXT & ~filters.COMMAND, knz_game)],
            RATE: [
                CallbackQueryHandler(knb_stat, pattern="^knb_state$"),
                CallbackQueryHandler(start, pattern="^back$"),
            ],
        },
        fallbacks=[CommandHandler("start", start)],
    )
    application.add_handler(conv_handler)
    application.run_polling()
