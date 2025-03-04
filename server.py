"""Greeting Flask app."""

from random import choice

from flask import Flask, request

# "__name__" is a special Python variable for the name of the current module
# Flask wants to know this to know what any imported things are relative to.
app = Flask(__name__)

AWESOMENESS = [
    'awesome', 'terrific', 'fantastic', 'neato', 'fantabulous', 'wowza',
    'oh-so-not-meh', 'brilliant', 'ducky', 'coolio', 'incredible',
    'wonderful', 'smashing', 'lovely']


STINKINESS = [
  'a rude ape', 'smelly', 'a jerk', 'a dipstick', 'a dingbat', 'stupid',
  'a bonehead', 'a dummy', 'undesirable', 'dirty']


@app.route('/')
def start_here():
    """Home page."""

    return """
    <!doctype html>
    <html>
      <head>
        <title>Hi! This is the home page.</title>
      </head>
    <body>
      <h1>Hi! This is the home page.</h1>
      <a href="http://localhost:5000/hello">Hello</a>
    </body>
    </html>
    """


@app.route('/hello')
def say_hello():
    """Say hello and prompt for user's name."""

    return """
    <!doctype html>
    <html>
      <head>
        <title>Hi There!</title>
      </head>
      <body>
        <h1>Hi There!</h1>
          <form action="/compliment">
          What's your name? <input type="text" name="person"><br>
            Click this button if you want a compliment! <input type="submit">
          </form>
          <br>
          <form action="/diss">
          What's your name? <input type="text" name="person"><br>
            Click this button if you want a diss! <input type="submit">
          </form>
      </body>
    </html>
    """


# @app.route('/greet')
# def greet_person():
#     """Get user by name."""

#     player = request.args.get("person")

#     compliment = request.args.get("compliment")

#     return f"""
#     <!doctype html>
#     <html>
#       <head>
#         <title>A Compliment</title>
#       </head>
#       <body>
#         Hi, {player}! I think you're {compliment}!
#       </body>
#     </html>
#     """

@app.route("/compliment")
def get_complimented():
    """Compliment user by name."""

    user = request.args.get("person")
    compliment = choice(AWESOMENESS)

    return f"""
      <!doctype html>
        <html>
          <head>
            <title>A Compliment</title>
          </head>
          <body>
          Hi {user}! I think you're {compliment}!
          </body>
        </html>
      """


@app.route("/diss")
def get_dissed():
    """Diss user by name."""

    user = request.args.get("person")
    diss = choice(STINKINESS)

    return f"""
      <!doctype html>
        <html>
          <head>
            <title>A Compliment</title>
          </head>
          <body>
          Hi {user}! I think you're {diss}!
          </body>
        </html>
      """

if __name__ == '__main__':
    # debug=True gives us error messages in the browser and also "reloads"
    # our web app if we change the code.
    app.run(debug=True, host="0.0.0.0")
