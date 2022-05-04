from flask import Flask, render_template
import webbrowser
app = Flask(__name__)





@app.route("/")
def hello_world():
  return render_template('home.html') 

if __name__ == "__main__":
    webbrowser.open_new('http://127.0.0.1:5002/')
    app.run(port=5002, debug=True, use_reloader=False)