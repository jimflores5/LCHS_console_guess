import sys
import cgi
from flask import Flask, request, redirect, render_template

app = Flask(__name__)
app.config['DEBUG'] = True

# Progam code here:


# Keep this at the bottom of the program:
app.run()