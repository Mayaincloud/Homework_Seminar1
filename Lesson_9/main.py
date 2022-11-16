from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes


async def hello(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(f'Hello {update.effective_user.first_name}')


app = ApplicationBuilder().token("5723809096:AAHWVjbPmAiROfW3AFMEuJUgm-COI-Ot_uE").build()

app.add_handler(CommandHandler("hello", hello))
print ('server start')

app.run_polling()