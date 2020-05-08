from django.conf import settings

import telegram as tg
import telegram.ext as tg_ext

import requests

from django.core.management.base import BaseCommand, CommandError
from django.template.loader import render_to_string

from statistics.models import CountryStatistic
from countries.models import Country


def get_statistics_view(search_text):
    print(search_text)
    country = Country.objects.filter(name=search_text).first()
    print(country)
    if not country:
        return "Perhaps you did mistake.\n" \
               "Please, resend a country name in English"

    statistic = CountryStatistic.objects.filter(
        country=country,
    ).order_by('-date')[0:2:1]

    statistic = statistic[-1:]

    if not statistic:
        return 'Not Found!'

    statistic = statistic[0]
    print(statistic)

    text = render_to_string('tg_response_message.txt', {'statistic': statistic})
    print(text)
    return text


def message_handler(bot: tg.Bot, update: tg.Update):
    user = update.effective_user
    message = update.effective_message.text
    message = message.strip()

    user_name = user.username if user else 'anon'
    print(user_name, message)

    response_message = None

    if message == '/start':
        response_message = f'Hello, {user_name}!'
    else:
        response_message = get_statistics_view(message)

    print(response_message)

    if response_message:
        bot.send_message(
            chat_id=update.effective_message.chat_id,
            text=response_message
        )
        print(response_message)

    print('------------')


def main():
    bot = tg.Bot(token=settings.TG_BOT_TOKEN, base_url=settings.TG_BOT_PROXY)
    updater = tg_ext.Updater(bot=bot)
    handler = tg_ext.MessageHandler(tg_ext.Filters.all, message_handler)
    updater.dispatcher.add_handler(handler)
    updater.start_polling()
    updater.idle()


class Command(BaseCommand):
    help = 'Closes the specified poll for voting'

    def add_arguments(self, parser):
        # parser.add_argument('poll_ids', nargs='+', type=int)
        pass

    def handle(self, *args, **options):
        main()
