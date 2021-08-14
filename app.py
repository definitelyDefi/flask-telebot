
from flask import Flask
from flask import render_template
import config
import telebot

apiToken = config.API_TOKEN
bot = telebot.TeleBot(apiToken, parse_mode=None)
app = Flask(__name__)

  
@app.route("/")
def index_page():
    return render_template('index.html')

@app.route("/send-message", methods=['GET']) 
def send_message():  
    bot.send_message(chat_id=config.id, text='some random text btw')
    return render_template('index.html')
    
    


        



    

        
       
    