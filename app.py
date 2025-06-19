from flask import Flask 

app=Flask(__name__)

#app routing
@app.route('/', methods=['get'])
def home():
    return 'Hello Saurav! Welcome to home page!'

if __name__=='__main__':
    app.run(debug='true')