   # Telegram bot for Wi-Fi complaints
   from telegram import Update
   from telegram.ext import Application, CommandHandler

   async def start(update: Update, context):
       await update.message.reply_text("Wi-Fi Bot ready!")

   def main():
       app = Application.builder().token("TOKEN").build()
       app.add_handler(CommandHandler("start", start))
       app.run_polling()

   if __name__ == "__main__":
       main()
