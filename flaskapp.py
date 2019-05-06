from flask import Flask, render_template, request, redirect, url_for
#import sys 

#sys.path.insert(0,"./gpt2/src/") 
from controller import main 

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')


@app.route("/", methods = ["POST"])
def index_POST():
    text = request.form["prefix"]
    if len(text) <5:
        return render_template("index.html")
    '''
    text = text.split(" ") 
    text = " ".join(text) 
    text.replace("\n", " ")
    '''
    #text = " ".join(text)
    answer = main(text)
    #answer = answer.split(" ")i
    
    for x in answer:
        if x in dirtywords:
            answer =main(text)
    answer = " ".join(answer)
    answer.replace("\n"," ")
    #answer.append(len(answer))
    if answer:
        return render_template("index.html", answer = answer, yours = text)
    else:
        return render_template("index.html", answer = "Error!", yours= None)
    #send me over to the network, process, and print, 
    #then hand me back to the original page.



if __name__=="__main__":
    app.run(host="0.0.0.0",port=80)
