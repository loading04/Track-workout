from flask import Flask, render_template, request
import database

app = Flask(__name__)

all_pr = database.get_all()


@app.route('/')
def home():
    return render_template("index.html", prs=all_pr)


@app.route("/add", methods=['POST', 'GET'])
def add():
    if request.method == 'POST':
        exo = request.form['exo']
        kg = request.form['kg']

        database.create_column(exo, kg)
        all_pr = database.get_all()

        return render_template("index.html", prs=all_pr)

    return render_template("add.html")


if __name__ == "__main__":
    app.run(debug=True)
