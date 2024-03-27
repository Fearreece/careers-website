from flask import Flask, render_template, url_for, redirect

app = Flask(__name__)

jobs = [
    {
        'id':1,
        'title':"Software Developer",
        'location':'Nigeria'
    },
    {
        'id':2,
        'title':"Data Analyst",
        'location':'South Africa'
    },
    {
        'id':3,
        'title':"Network Engineer",
        'location':'London'
    },
    {
        'id':4,
        'title':"System Admin",
        'location':'Qatar'
    }
]

@app.route("/")
def hello_world():
    greeting = "hello!"
    return render_template('index.html',
                           jobs=jobs,
                           company_name="Reece"
                           )


if __name__ == '__main__':
    app.run(debug=True)