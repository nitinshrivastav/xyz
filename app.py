#!/usr/bin/env python
# coding: utf-8

# In[3]:


from flask import Flask,render_template,request
import smtplib
app=Flask(__name__)
@app.route("/")
def xyz():
    return render_template("form.html")
@app.route("/details",methods=['GET','POST'])
def hjgh():
    if(request.method=='POST'):
        course=request.form['c1']
        name=request.form['n1']
        email=request.form['e1']
        phone=request.form['p1']
        
        server=smtplib.SMTP_SSL("smtp.gmail.com",465)
        server.login("intro.nitin@gmail.com",'Nitinstudent@123')
        msg='Hello {0},\nThank you for register in college\nour team will contact you the course {1}'.format(name,course)
        server.sendmail("intro.nitin@gmail.com",email,msg)
        server.quit()
        return render_template("form.html")
if __name__=="__main__":
    app.run()

