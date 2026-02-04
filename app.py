# This is a sample Python script.
# import statments
from flask import Flask, render_template, render_template_string, request


from indexintext import getindextext
app = Flask(__name__)

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

@app.route("/")
def index():
    return render_template_string(getindextext())



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    app.run(debug=True)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
