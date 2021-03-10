# Create a Py Webserver with Flask
# Function should come right after @app
# Host= Localhost my machine - Port = generic convention
# Host is a Building
# Port one apartment
# Allow you website to be access by another pcs
# Host="0.0.0.0"
# render_template create a template with the name you are looking for
# the folder need be called templates, you can add multiple html files
# create a static folder to java and css script
# Flask is a micro framework (easy tool to make it simple to develop web sites) python

from flask import Flask

app = Flask(__name__)
print(__name__)


@app.route('/')
def hello_world():
    return 'Hellow World!'



# @app.router('/')
# def hello_world():
#     return render_template("index.html")
#
#
# @app.route('/blog')
# def blog():
#     return 'These are thoughts'
#
#
# @app.route('blog/2020/dogs')
# def blog2():
#     return 'this is my dog'
