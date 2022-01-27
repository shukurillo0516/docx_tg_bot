'''
1. Telegram bot that takes data
saves to the db if data is not in it already.
2. Also sends to docx formatter if it is unique.
'''

import logging

from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext

from models.model import save_data_if_unique


logging.basicConfig(
	format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)

logger = logging.getLogger(__name__)


def start(update: Update, context: CallbackContext) -> None:
	user = update.effective_user
	update.message.reply_text(fr"Hi {user}\!")


def help_command(update: Update, context: CallbackContext) -> None:
	update.message.reply_text("Send message. \n \
							   Format docx as you want with the help of this bot. \n \
							   Good luck!.")


def accept_message(update: Update, context: CallbackContext) -> None:
	try:
		resp = save_data_if_unique(update.message.text)	
	except Exception as e:
		print(e)
		
	if resp == 'success':
		update.message.reply_text("Thanks")
	elif resp == 'duplicate':
		update.message.reply_text("duplicate")


def main() -> None:
	"""Start the bot."""
	# Make the Updater and pass it your bot's token.
	updater = Updater("5057207474:AAHpi_UUlpMhb09smsMAPJ76JshAlby5x-w")
	dispatcher = updater.dispatcher

	dispatcher.add_handler(CommandHandler('start', start))
	dispatcher.add_handler(CommandHandler('help', help_command))

	dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, accept_message))

	updater.start_polling()


	updater.idle()


if __name__  == "__main__":
	main()  