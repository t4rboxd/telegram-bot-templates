from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import json

# parse config.json
with open('config.json', 'r') as f:
    config = json.load(f)

# define a example command
async def hello(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(f'Hello {update.effective_user.first_name}')

app = ApplicationBuilder().token(config['token']).build()
# you add commands here
app.add_handler(CommandHandler("start", hello))
# starts the bot
app.run_polling()