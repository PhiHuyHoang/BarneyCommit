import random, os
from flask import Flask

app = Flask(__name__)

setup_variable = "commit_messages.txt"
messages = open(setup_variable,encoding='utf-8').read().split('\n')

@app.route('/', methods=['GET' , 'POST'])
def index():
    return random.choice(messages)

if __name__ == '__main__':
    port = int(os.getenv('PORT', 8000))
    print("Starting app on port %d" % port)

app.run(debug=False, port=port, host='0.0.0.0')

