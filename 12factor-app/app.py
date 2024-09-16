from flask import Flask
from redis import Redis
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
redisDb = Redis(host=os.getenv('HOST'), port=os.getenv('PORT'))

@app.route('/')
def welcome():
    redisDb.incr('visitorCount')
    visitCount = str(redisDb.get('visitorCount'), 'utf-8')
    return "Welcome Collins\n Visitor count: " + visitCount

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)