from flask import Flask , render_template

#Create Flask Instance
app = Flask(__name__)

#Create a route decorator
@app.route('/')
def index():
    fn = "zainab"
    return render_template("index.html" , fn=fn)


#/user/zainab
@app.route('/user/<name>')
def user(name):
     return render_template("user.html", user_name=name)

#Invalid Error
@app.errorhandler(404)
def page_not_foud(e):
     return render_template("404.html") , 404

#Internal Error
@app.errorhandler(500)
def user(e):
     return render_template("500.html") , 500