from flask import Flask 

app=Flask(__name__)

#app routing
@app.route('/', methods=['get'])
def home():
    return 'Welcome to home page!'

if __name__=='__main__':
    app.run(debug='true')