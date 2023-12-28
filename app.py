from flask import Flask

app = Flask(__name__)

@app.route("/") # its a decorator
#a route refers to a URL pattern that an application's web #server can match to a specific piece of code or function.

def hello_wrld():
    return "Hello Mumma!"

if __name__ == "__main__":
  app.run(host = "0.0.0.0", debug = True)
