import logging
import environ
from telegram.ext import Updater, CommandHandler


# Setup logging
logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

env = environ.Env()
telegram_token = env('TELEGRAM_TOKEN')

updater = Updater(telegram_token, use_context=True)

# If there is a webhook, delete it now
updater.bot.deleteWebhook()

# Get the last update_id from Telegram's API
updates_found = updater.bot.getUpdates()
if not updates_found:
    print('Couldn\'t find any pending updates for your bot')
    exit()

last_update_id = updates_found[-1].to_dict().get('update_id')

# Make a new request for updates, but now use a offset
# This prompts Telegram to mark all messages as "confirmed"
updater.bot.getUpdates(offset=(last_update_id + 1))

# Make a final request for updates to check if we were successful
updates = updater.bot.getUpdates()

if len(updates) == 0:
    print(f'Webhooks and {len(updates_found)} updates cleared for your bot')
else:
    print(f'There was a problem clearing {len(updates_found)} updates for your bot')
