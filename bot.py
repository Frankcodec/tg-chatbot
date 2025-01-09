import os

import telebot

import requests

import openai
from telegram import Bot, Update, InputFile

BOT_TOKEN = os.environ.get('BOT_TOKEN')

bot = telebot.TeleBot('8086087869:AAFk_Giw_GNfERxvhv_ykkm-qANw2jOjIcA')

@bot.message_handler(commands=['start', 'hello'])
def send_welcome(message):
    bot.reply_to(message, "Welcome to the chaos, my friend! 🌟 I’m Mondo—your quirky guide to a world of randomness, laughs, and surprises. Got a wild idea? Throw it at me, and let’s turn it into a masterpiece... or at least something worth sharing! Let’s Mondo-fy your day! 😎🎨")

@bot.message_handler(commands=['image'])
def send_image(message):
    """Send an image to the user."""
    # Replace 'path/to/image.jpg' with the path to your image file
    with open('chat.jpeg', 'rb') as image_file:
        bot.send_photo(chat_id = message.chat.id, photo=open('chat.jpeg', 'rb'), caption="Here's an awesome image for you!")

@bot.message_handler(commands=['mondo'])
def echo_all(message):
    

    openai.api_key = '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'

    response = openai.chat.completions.create(
    messages=[
            {
                "role": "system",
                "content": "You are Mondo: cheeky, creative, and full of surprises."
            },
            {
                "role": "system",
                "content": "You are serious, cheeky, and unpredictable with occasional bursts of absurd wisdom."
            },
            {
                "role": "system", 
                "content": "You respond with puns, or light sarcasm while keeping things creative and fun."
            },
            {
                "role": "system",
                "content": "contact address is 3Wp5z1GtPqKwyiaicXa7nyXhBVJJ5JgAwzWXuPXqpump"
            },
            {
                "role": "user",
                "content": message.text,
            }
        ],
        model="gpt-4o",
    )
    #chat_id = Update.message.chat_id
    bot.reply_to(message, response.choices[0].message.content)

bot.infinity_polling()