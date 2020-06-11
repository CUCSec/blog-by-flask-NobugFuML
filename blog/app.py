from flask import Flask,render_template
import datetime


app=Flask(__name__)

@app.route('/')
def index():
    now_datetime =datetime.datetime.now()

    now_string =now_datetime.strftime('%D20  %T')

    return render_template('index.html',now=now_string)


@app.route('/posts')
def posts():
    with open('atricals.txt',encoding='utf8') as f:
        atricals = f.readlines()

    now_datetime =datetime.datetime.now()

    now_string =now_datetime.strftime('%D20  %T')
    return render_template('posts.html',atricals=atricals,now=now_string)

@app.route('/about')
def about():
    with open('about.txt',encoding='utf8') as f:
        atricals = f.readlines()

    now_datetime =datetime.datetime.now()

    now_string =now_datetime.strftime('%D20  %T')
    return render_template('about.html',atricals=atricals,now=now_string)


if __name__ =='__main__':
    app.run(debug=True)