from telegram.ext import Updater, Dispatcher, CommandHandler, Filters, CallbackContext, MessageHandler, \
    ConversationHandler
from telegram import Update, ReplyKeyboardMarkup, MessageEntity, KeyboardButton, ReplyKeyboardRemove

updater: Updater = Updater(token='5582148162:AAG2UfkVqJOGE-3BAAUfW-DbD1ryZIQ13mg')
dispatcher = updater.dispatcher

MONDAY = (
    '\nMathematics---9AM to 11AM\n'
    '\nEnglish---12AM to 1PM\n'
    '\nHistory---1PM to 2PM\n'
    '\nPsychology---2PM to 3PM'
)

TUESDAY = (
    '\nEnglish---9AM to 11AM\n'
    '\nPublic Speaking---12AM to 1PM\n'
    '\nInternational Relations---1PM to 2PM\n'
    '\nPsychology---2PM to 3PM'
)

WEDNESDAY = (
    '\nAccounting---9AM to 11AM\n'
    '\nStatistics---12AM to 1PM\n'
    '\nEthics---1PM to 2PM\n'
    '\nCyber Security---2PM to 3PM'
)

THURSDAY = (
    '\nMathematics---9AM to 11AM\n'
    '\nMedia---12AM to 1PM\n'
    '\nLiterature---1PM to 2PM\n'
    '\nPsychology---2PM to 3PM'
)
FRIDAY = (
    '\nWriting 2090---9AM to 11AM\n'
    '\nManagerial Acc---12AM to 1PM\n'
    '\nPhysics---1PM to 2PM\n'
    '\nComputer Programming---2PM to 3PM'
)


def menu_keyboard():
    return ReplyKeyboardMarkup([
        [KeyboardButton('Monday'), KeyboardButton('Tuesday')],
        [KeyboardButton('Wednesday'), KeyboardButton('Thursday')],
        [KeyboardButton('Friday')],
    ], resize_keyboard=True, one_time_keyboard=True)


def start_handler(update: Update, context: CallbackContext):
    user = update.effective_user
    update.message.reply_markdown_v2(
        f"Hi \!, Welcome back\! {user.mention_markdown_v2()}", reply_markup=menu_keyboard()
    )


def Monday(update: Update, context: CallbackContext):
    update.message.reply_text(f"Classes on Monday:\n {MONDAY}")


def Tuesday(update: Update, context: CallbackContext):
    update.message.reply_text(f"Classes on Tuesday:\n {TUESDAY}")


def wednesday(update: Update, context: CallbackContext):
    update.message.reply_text(f"Classes on Wednesday:\n {WEDNESDAY}")


def thursday(update: Update, context: CallbackContext):
    update.message.reply_text(f"Classes on Thursday:\n {THURSDAY}")


def friday(update: Update, context: CallbackContext):
    update.message.reply_text(f"Classes on Friday:\n {FRIDAY}")


dispatcher.add_handler(CommandHandler('start', start_handler))
dispatcher.add_handler(MessageHandler(Filters.regex(r"^Monday$"), Monday))
dispatcher.add_handler(MessageHandler(Filters.regex(r"^Tuesday$"), Tuesday))
dispatcher.add_handler(MessageHandler(Filters.regex(r"^Wednesday$"), wednesday))
dispatcher.add_handler(MessageHandler(Filters.regex(r"^Thursday$"), thursday))
dispatcher.add_handler(MessageHandler(Filters.regex(r"^Friday$"), friday))

updater.start_polling()
updater.idle()
