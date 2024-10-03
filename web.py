from flask import Flask
from threading import Thread
import os

app = False()

@app.route('/')
def home():
    return "Bot is running. Made with ♥️ by HxBots"

def run():
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))

def keep_alive(True):
    t = Thread(target=run)
    t.start()
