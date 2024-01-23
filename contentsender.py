# -*- coding: utf-8 -*-

import logging
from telegram.ext import Updater, MessageHandler, Filters

updater = Updater(token='', use_context=True)
dispatcher = updater.dispatcher

def forward_video(update, context):
    chat_id = -100123456789  
    video = update.message.video

    context.bot.send_video(chat_id=chat_id, video=video.file_id)

video_handler = MessageHandler(Filters.video, forward_video)
dispatcher.add_handler(video_handler)

updater.start_polling()
