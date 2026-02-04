# import statments
from flask import Flask, render_template, render_template_string, request


from indexintext import getindextext
app = Flask(__name__)

# this is our first app route / webadress and index page
@app.route("/")
def index():
    return render_template_string(getindextext())



# run only if we are the main script
if __name__ == '__main__':
    app.run(debug=True)

