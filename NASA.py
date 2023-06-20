import requests
import telegram
import asyncio
import schedule
import time

# Define the NASA API URL and your API key
api_url = "https://api.nasa.gov/planetary/apod"
api_key = "f2D7dO4YdbQwSXdaW33QgajwjZghfKCUfDjj5Dgw"

# Define the Telegram bot token and chat ID
bot_token = "6177428008:AAEewf2ZGq657fvMqJ6oqH4tYoYvpaP68p8"
chat_id = "1285682450"

# Fetch the APOD from NASA API and send the message via Telegram bot
def get_apod_and_send_message():
    response = requests.get(f"{api_url}?api_key={api_key}")
    data = response.json()

    # Extract the necessary information from the response
    image_url = data["url"]
    title = data["title"]
    explanation = data["explanation"]

    # Create a message with the image URL and caption
    message = f"Title: {title}\n\nExplanation: {explanation}\n\nImage: {image_url}"

    # Send the message via Telegram bot
    bot = telegram.Bot(token=bot_token)
    bot.send_message(chat_id=chat_id, text=message)

# Schedule the job to run every 24 hours
schedule.every(24).hours.do(get_apod_and_send_message)

# Infinite loop to run the scheduled jobs
while True:
    schedule.run_pending()
    time.sleep(1)
