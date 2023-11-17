from flask import Flask, render_template, request

VandeBharat = Flask(__name__)

@VandeBharat.route('/')
def helloworld():
    return render_template("index.html")

if __name__ == '__main__':
    VandeBharat.run(debug = False, port = 8000)
