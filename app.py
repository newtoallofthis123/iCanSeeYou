from flask import Flask, render_template, redirect, request
from requests.api import get
from brain import engine, get_host_name

app = Flask(__name__)

month_int_to_str = {
    1 : "January",
    2 : "Febuary",
    3 : "March",
    4 : "April",
    5 : "May",
    6 : "June",
    7 : "July",
    8 : "August",
    9 : "September",
    10 : "October",
    11 : "November",
    12 : "December",
}

@app.route('/results')
def results():
    user_results = engine()
    month_to_convert = user_results[1]["month"]
    month_converter = month_int_to_str[month_to_convert] 
    return render_template('results.html', ip_results=user_results[0], time_zone_results=user_results[1], month_converter=month_converter, host_name=get_host_name())

@app.route('/about')
def about_page():
    return render_template('about.html')

@app.route('/terms')
def terms_page():
    return render_template('/tos.html')

@app.route('/')
def i_can_see_you():
    return render_template('home.html')