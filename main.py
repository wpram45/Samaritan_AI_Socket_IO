import speech_recognition as sr
from flask import  Flask
import _thread
from flask import Flask,render_template,redirect,request,url_for,session
r=sr.Recognizer()
import json
import random
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

from flask_socketio import SocketIO,send,emit
import time,queue


app=Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/19'
app.config["CACHE_TYPE"] = "null"
socketio = SocketIO(app)
thread_start = False
q=queue.Queue()
thinking=False
answer="..."
trained=False






def background_stuff(respond):
    global answer
    global thinking
    try:
    #respond=q.get()


        while True:
            time.sleep(2)
            t = str(time.clock())
            #print(answer)
            if thinking==True:
                socketio.emit('message', {'data': "this is data", 'time': "..."*random.randint(1,6)}, namespace='/test')
            else:
                socketio.emit('message', {'data': "this is data", 'time': str(answer)}, namespace='/test')

    except Exception:
        import traceback
        print(traceback.format_exc())

@app.route("/")
@app.route("/index")

def main():











    return render_template("index.html")









@app.route("/sendvoice",methods=['POST'])

def set_respond():
    respond="..."

    global thinking
    thinking=True


    data=request.data
    value_dict=json.loads(data.decode())
     #print(value_dict["value"])


    chatbot = ChatBot('Samaritan')

# Create a new trainer for the chatbot
    trainer = ChatterBotCorpusTrainer(chatbot)

# Train the chatbot based on the english corpus
    trainer.train("chatterbot.corpus.english")

# Get a response to an input statement
    text=chatbot.get_response(value_dict["value"])

 # print(text)


       # session["variable"]=text

    respond=text
    global answer
    answer=str(respond)


    set_cookie(key, value="", max_age=None)




       # q.put(respond)
    global thread_start
    if thread_start==False:
        thread_start=True
        _thread.start_new_thread( background_stuff,(respond,))





    thinking=False
    return render_template("index.html")







if __name__ =="__main__":

    socketio.run(app,host="0.0.0.0")




