#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar  1 20:12:07 2022

@author: nimisha
"""

#conventional naming: app.py
from flask import Flask
app = Flask(__name__) #main
#dir(app)
from flask import request, render_template
import joblib

#decorator: run this function before you run the next function (index) !!READ MORE!!
@app.route("/",methods=["GET","POST"])
def index():
    #detect if submit button pressed
    if request.method == "POST":
        Nikkei = request.form.get("Nikkei")
        print(Nikkei)
        model1 = joblib.load("STI_REG")
        pred1 = model1.predict([[Nikkei]])
        str1 = "The prediction for STI using Regression is : " + str(pred1)
        return (render_template("index.html",result1=str1))
    
    else:
        return (render_template("index.html",result1="2"))

if __name__=="__main__":
    #in developer environment, not needed
    #but in cloud, important to verify that the code running is yours
    app.run()
    #app.run(host="127.0.0.1", port = int("80")) #1111 can also be tried
