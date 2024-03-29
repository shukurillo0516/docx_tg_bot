'''
1. Telegram bot that takes data
saves to the db if data is not in it already.
2. Also sends to docx formatter if it is unique.
'''

import logging

from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext

from models.model import save_data_if_unique
from docx_formatter.main import make_docx, save_docx


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


def save(update: Update, context: CallbackContext) -> None:
	save_docx()
	update.message.reply_text("Saved")


i = 1
def accept_message(update: Update, context: CallbackContext) -> None:
	global i
	message = str()
	if(update.message.caption):
		message = update.message.caption
	else:
		message = update.message.text
	
	try:
		resp = save_data_if_unique(message)	
	except Exception as e:
		print(e)
		
	# Just testing
	if resp == 'success':
		make_docx(message)
		update.message.reply_text("Thanks")
		print(i)
		i += 1
	elif resp == 'duplicate':
		update.message.reply_text("duplicate")


def main() -> None:
	"""Start the bot."""
	# Make the Updater and pass it your bot's token.
	updater = Updater("5057207474:AAHpi_UUlpMhb09smsMAPJ76JshAlby5x-w")
	dispatcher = updater.dispatcher

	dispatcher.add_handler(CommandHandler('start', start))
	dispatcher.add_handler(CommandHandler('help', help_command))
	dispatcher.add_handler(CommandHandler('save', save))

	dispatcher.add_handler(MessageHandler(Filters.update, accept_message))
	#Filters.text & ~Filters.command
	updater.start_polling()


	updater.idle()


if __name__  == "__main__":
	main()  
