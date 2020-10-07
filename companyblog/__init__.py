from flask import Flask,redirect,url_for,render_template,request

app=Flask(__name__)


from companyblog.core.views import core
from companyblog.error_pages.handlers import error_pages
app.register_blueprint(core)
app.register_blueprint(error_pages)
