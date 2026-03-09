import telebot
import requests
import os

TOKEN = 'API'


API_URL = "http://127.0.0.1:8000/analyze"

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, "Привет! Пришли мне фото проростка, и я посчитаю площадь корней и листьев в мм².")

@bot.message_handler(content_types=['photo'])
def handle_photo(message):
    bot.send_message(message.chat.id, "Обрабатываю изображение... Подождите.")
    
    try:

        file_info = bot.get_file(message.photo[-1].file_id)
        downloaded_file = bot.download_file(file_info.file_path)
        

        files = {'file': ('image.jpg', downloaded_file, 'image/jpeg')}
        response = requests.post(API_URL, files=files)
        
        if response.status_code == 200:
            data = response.json()
            results = data.get('analysis', [])
            
            if not results:
                bot.reply_to(message, "Растения не найдены. Попробуй другое фото.")
            else:
                report = "📊 **Результаты анализа:**\n"
                for res in results:
                    report += f"🌱 {res['object'].capitalize()}: {res['area_mm2']} мм²\n"
                bot.reply_to(message, report, parse_mode="Markdown")
        else:
            bot.reply_to(message, "Ошибка сервера FastAPI.")
            
    except Exception as e:
        bot.reply_to(message, f"Произошла ошибка: {e}")

print("Бот запущен...")
bot.polling(none_stop=True)