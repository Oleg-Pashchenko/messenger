from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def chats():
    return render_template('chats.html')


@app.route('/<int:id>')
def chat(id: int):
    print(id)
    return render_template('chat.html')



if __name__ == '__main__':
    app.run(debug=True)
