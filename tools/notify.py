#!/usr/bin/env python3
import sys
import time
import requests


def telegram_bot_sendtext(bot_message):

    bot_token = '5563375516:AAEyLxo9pkMzFsct39igx8LbSC7E3fvmfkc'
    bot_chatID = '2005986039'

    send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + bot_chatID + '&parse_mode=Markdown&text=' + bot_message

    response = requests.get(send_text)

    return response.json()


def main():
    message = sys.stdin.readlines()
    for line in message:
        telegram_bot_sendtext(line)


main()
