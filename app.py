#!/usr/bin/env python

from flask import Flask, render_template, redirect, url_for, request
from emo_bot import EmoBot

app = Flask(__name__)

@app.route('/', methods =['GET', 'POST'])
def home():
    if request.method == 'POST':
       text = request.form.get('text')
       bot = EmoBot(text)
       reply = bot.get_reply()

       if reply == 99:
           return render_template('error.html')

       result = str('result' + str(reply) + '.html')
       return render_template(result)
    return render_template('index.html')




if __name__ == '__main__':
    app.run()
