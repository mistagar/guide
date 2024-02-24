from flask import Flask, url_for
#from flask import url_for

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World'

@app.route('/about')
def about():
    return 'This is the about page'

@app.route('/post/<int:post_id>')
def view_post(post_id):
    return f"Viewing Blog Post#{post_id}"


@app.route('/user/<username>')
def user(username):
    #return "The user is : " + username
    url = url_for('user', username="gar")
    return "The user is : " + username




if __name__ == '__main__':
    app.run()
