from flask import Flask, render_template, session, redirect

app = Flask(__name__)

@app.route('/')
async def home():
    return render_template("templates/index.html")

if __name__ == "__main__":
    app.run(debug=True)
