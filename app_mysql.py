from flask import Flask, render_template, flash, redirect, url_for, session, request, logging, Response
#from data import Vendors
from wtforms import Form, StringField, TextAreaField, PasswordField, RadioField, BooleanField, validators
from wtforms.validators import DataRequired
from passlib.hash import sha256_crypt
from functools import wraps
from datetime import datetime, date, time
import time as t
from flask_mysqldb import MySQL
from jinja2 import Environment 
from jinja2.loaders import FileSystemLoader
import subprocess
import requests
from requests.auth import HTTPBasicAuth
import json
import os
import humanize
from read_zipfile import list_zip_file
from file_list import file_list

app = Flask(__name__, static_url_path='/assets', static_folder='assets')

print('-------FLASK INFO--------')
print('STARTING THE FLASK APP...')
print('-------FLASK INFO--------')

# Config MySQL
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'root'
app.config['MYSQL_DB'] = 'dsi'
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'

# init MYSQL
mysql = MySQL(app)

# cur = mysql.connection.cursor()
# result = cur.execute("SELECT USER")
# loggedin = cur.fetchall()
# print('Logged in as : '+str(loggedin))

print('------FLASK INFO--------')
print('CONNECTION TO MYSQL MADE')
print('------FLASK INFO-------')


# FILTERS

@app.template_filter('time_fmt')
def time_desc(timestamp):
    mdate = datetime.fromtimestamp(timestamp)
    str = mdate.strftime('%Y-%m-%d %H:%M:%S')
    return str

@app.template_filter('data_fmt')
def data_fmt(filename):
    t = 'unknown'
    for type, exts in datatypes.items():
        if filename.split('.')[-1] in exts:
            t = type
    return t

@app.template_filter('humanize')
def time_humanize(timestamp):
    mdate = datetime.utcfromtimestamp(timestamp)
    return humanize.naturaltime(mdate)

@app.template_filter('icon_fmt_text')
def icon_fmt_text(filename):
    i = 'history'#DEFAULT
    for icon, exts in icontypes.items():
        if filename == exts:
            i = icon
    return i

@app.template_filter('icon_fmt_ext')
def icon_fmt_ext(filename):
    i = 'history'#DEFAULT
    for icon, exts in icontypes.items():
        if filename in exts:
            i = icon
    return i

#ASSOCIATE FILE EXTENSIONS WITH ICONS
icontypes = {'mail green': 'Data Request', 'rocket red': 'Internal Data Request', 'question blue': 'Information Request', 'file pdf outline': 'pdf', 'file video outline': '3g2,3gp,3gp2,3gpp,mov,qt', 'file code outline': 'atom,plist,bat,bash,c,cmd,coffee,css,hml,js,json,java,less,markdown,md,php,pl,py,rb,rss,sass,scpt,swift,scss,sh,xml,yml', 'file alternate outline': 'txt', 'film': 'mp4,m4v,ogv,webm', 'globe': 'htm,html,mhtm,mhtml,xhtm,xhtml'}


#ASSUMES THE FILE IS WRITTEN TO A LOG FILE
def code_to_run(file):    
    proc = subprocess.Popen(
        ['python',file],             #call something with a lot of output so we can see it            
        universal_newlines=True,
        stdout=subprocess.PIPE
    )


# HOME
@app.route('/')
def index():
    print('Website is running....')

    # Create cursor
    cur = mysql.connection.cursor()
    # Get gmails
    result = cur.execute("SELECT * FROM dsi.gmail where datediff(now(),gmSentDate) < 60;")
    gmails = cur.fetchall()

    # Get gmails
    result = cur.execute("SELECT * FROM dsi.testdata")
    data = cur.fetchall()

    #ADD A CHART
    legend = 'Monthly Data'
    labels = ["January", "February", "March", "April", "May", "June", "July", "August"]
    values = [10, 9, 8, 7, 6, 4, 7, 8]
    
    return render_template('home.html', gmails=gmails, values=values, labels=labels, legend=legend, data=data)

# ABOUT
@app.route('/about')
def about():
    return render_template('about.html')


# METRICS
@app.route('/metrics')
def metrics():
    return render_template('metrics.html')

# USER LOGIN
@app.route('/login', methods=['GET', 'POST'])
def login():
    
        
    if request.method == 'POST':
        print('this was a post request')
        # Get Form Fields
        userid = request.values.get('userid')
        password_candidate = request.values.get('password')

        print(userid)

        # Create cursor
        cur = mysql.connection.cursor()
        # Get user by username
        result = cur.execute("SELECT * FROM user WHERE userid = %s", [userid])
        print('this is the test for login in'+str(result) )


        if result > 0:
            # Get stored hash
            data = cur.fetchone()
            userpw = data['userpw']

            # Compare Passwords
            if sha256_crypt.verify(password_candidate, userpw):
                # Passed
                session['logged_in'] = True
                session['userid'] = userid

                flash('You are now logged in', 'success')
                return redirect(url_for('index'))
            else:
                error = 'Invalid login'
                flash('UserID found but password incorrect', 'error')
                return render_template('login.html', error=error)
            # Close connection
            cur.close()
        else:
            flash('UserID not found', 'error')
            return redirect(url_for('login'))

    return render_template('login.html')


# Check if user logged in
def is_logged_in(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        if 'logged_in' in session:
            return f(*args, **kwargs)
        else:
            flash('Unauthorized, Please login', 'error')
            return redirect(url_for('login'))
    return wrap


# LOGOUT
@app.route('/logout')
@is_logged_in
def logout():
    session.clear()
    flash('You are now logged out', 'success')
    return redirect(url_for('login'))



# SUMMARY
@app.route('/summary',methods=['GET', 'POST'])
@is_logged_in
def summary():
    
    # Create cursor
    cur = mysql.connection.cursor()

    #GET SOME VALUES
    #SELECT count(*) FROM dsi.jira group by status order by status desc;
    result = cur.execute("SELECT count(*) as total FROM dsi.jira where status='Open' union all SELECT count(*)  as total FROM dsi.jira where status='In Progress' union all SELECT count(*) as total FROM dsi.jira where status='Closed';")
    counts = cur.fetchall()

    result = cur.execute("SELECT * FROM dsi.jira;")
    jira = cur.fetchall()

    if result > 0:#SEEMS to only work when I name the vars as a dictionary and not a list I guess
        #print('Result is : '+str(result))
        return render_template('summary.html', jira=jira, counts=counts)
    else:
        msg = 'Nothing Found...strange'
        return render_template('summary.html', jira=jira,msg=msg)
    # Close connection
    cur.close()

# DELIVERABLES FROM LOGFILE TABLE
@app.route('/logs',methods=['GET', 'POST'])
@is_logged_in
def logs():

    #FIND THE LIST OF ZIP FILES
    zip=list_zip_file('mjh2.zip') 
    print(zip)

    # Create cursor
    cur = mysql.connection.cursor()
 
    #GET SOME VALUES
    #SELECT count(*) FROM dsi.jira group by status order by status desc;
    result = cur.execute("SELECT * FROM dsi.logfiles;")
    logfiles = cur.fetchall()

    
    if result > 0:#SEEMS to only work when I name the vars as a dictionary and not a list I guess
        #print('Result is : '+str(result))
        return render_template('logs.html', logfiles=logfiles,zip=zip)
    else:
        msg = 'Nothing Found...strange'
        return render_template('logs.html', msg=msg)
    # Close connection
    cur.close()


# DCHECK ALL FILES ARE PRESENT
@app.route('/check',methods=['GET', 'POST'])
@is_logged_in
def checks():

    # Create cursor
    cur = mysql.connection.cursor()

    #GET SOME VALUES
    #SELECT count(*) FROM dsi.jira group by status order by status desc;
    result = cur.execute("SELECT * FROM dsi.logfiles order by jirakey,filecat;")
    chkfiles = cur.fetchall()

    
    if result > 0:#SEEMS to only work when I name the vars as a dictionary and not a list I guess
        #print('Result is : '+str(result))
        return render_template('check.html', chkfiles=chkfiles)
    else:
        msg = 'Nothing Found...strange'
        return render_template('check.html', msg=msg)
    # Close connection
    cur.close()

# Anonymize Dashboard
# @app.route('/anonymize',methods=['GET', 'POST'])
# @is_logged_in
# def anonymize():
    
#     # Create cursor
#     cur = mysql.connection.cursor()
      
#     #GET SOME VALUES
#     #SELECT count(*) FROM dsi.jira group by status order by status desc;
#     result = cur.execute("SELECT distinct table_schema FROM sys.schema_table_statistics;")
#     schemas = cur.fetchall()

#     tables=''
#     if request.method == 'POST':
#             name2=request.values.get("onesel")
#             print('Single select is :'+str(name2))
#             x=str(name2)  

#             result = cur.execute("SELECT table_name,rows_fetched FROM sys.schema_table_statistics where table_schema='"+x+"';")
#             tables = cur.fetchall()
#             print(str(tables))

#     if result > 0:#SEEMS to only work when I name the vars as a dictionary and not a list I guess
#         #print('Result is : '+str(result))
#         return render_template('anonymize.html', schemas=schemas, tables=tables)
#     else:
#         msg = 'Nothing Found...strange'
#         return render_template('anonymize.html', msg=msg)
#     # Close connection
#     cur.close()


# ANONYMIZATION
@app.route('/anonymize',methods=['GET', 'POST'])
@is_logged_in
def anonymize():
    
    # Create cursor
    cur = mysql.connection.cursor()
      
    #GET SOME VALUES
    #SELECT count(*) FROM dsi.jira group by status order by status desc;
    result = cur.execute("SELECT table_schema,table_name FROM sys.schema_table_statistics order by table_schema,table_name;")
    schemas = cur.fetchall()
  
    if result > 0:#SEEMS to only work when I name the vars as a dictionary and not a list I guess
        #print('Result is : '+str(result))

        if request.method == 'POST':

            schema_selected=request.values.get("schemasel")
            print('Schema selcted is :'+str(schema_selected))  

        return render_template('anonymize.html', schemas=schemas)
    else:
        msg = 'Nothing Found...strange'
        return render_template('anonymize.html', msg=msg)

    # Close connection
    cur.close()

    return render_template('anonymize.html')


@app.route('/anonymize_schema',methods=['GET', 'POST'])
@is_logged_in
def anonymize_schema():
    
    # Create cursor
    cur = mysql.connection.cursor()
      
    #GET SOME VALUES
    #SELECT count(*) FROM dsi.jira group by status order by status desc;
    result = cur.execute("SELECT * FROM dsi.logfiles order by category,jirakey,filecreatedate,logfileid;")
    logs = cur.fetchall()
  
    if result > 0:#SEEMS to only work when I name the vars as a dictionary and not a list I guess
        return render_template('anonymize_schema.html', logs=logs)
    else:
        msg = 'Nothing Found...strange'
        return render_template('anonymize_schema.html', msg=msg)

    # Close connection
    cur.close()

    
    return render_template('anonymize_schema.html')


# import time
# def follow(thefile):
#     thefile.seek(0,2)
#     while True:
#         line = thefile.readline()
#         if not line:
#             time.sleep(0.1)
#             continue
#         yield line


#     for line in iter(proc.stdout.readline,''):
#         time.sleep(0.1)                           # Don't need this just shows the text streaming
#         yield line.rstrip() + '<br/>\n'
#     inner2()

def read_log(logname):
    info=0
    error=0
    warn=0    
    try:
        with open(os.path.join(".",logname),"r") as logfile:
            loglines=logfile.readlines()

            log=list()  
            for item in loglines:
                if item.startswith("INFO"): 
                    info=info+1
                    log.append('<span style="color:blue;">'+str(item[10:])+'</span><br>')
                elif item.startswith("ERROR"): 
                    error=error+1
                    log.append('<span style="color:red;">'+str(item[11:])+'</span><br>')
                elif item.startswith("WARNING"): 
                    warn=warn+1
                    log.append('<span style="color:teal;">'+str(item[13:])+'</span><br>')
    except:
        log=['No file found yet!']

    return log,info,error,warn    

@app.route('/runcode',methods=['GET', 'POST'])
@is_logged_in
def runcode():

    # Create cursor
    cur = mysql.connection.cursor()
      
    result = cur.execute("SELECT * FROM dsi.jira order by jirakey")
    jira = cur.fetchall()
  

    x=['No file found yet!']
    i=0
    e=0
    w=0
    if request.method == 'GET':
        get_log=request.values.get("submit")
        clear_log=request.values.get("clear")
        save_log=request.values.get("save")

        if get_log=='submit':
            code_to_run('code2run.py')                                
            i=0
            e=0
            w=0
            t.sleep(1)
            x,i,e,w=read_log('./code2run.log')

        if clear_log=='clear':
            i=0
            e=0
            w=0
            x=['No file found yet!']
            try:
                os.remove('code2run.log')
            except:
                print('cant fine the files... oh no!')                

        if save_log=='save':
            print(e)
            if e>0:
                flash('Error found - will not save the log', 'warning')
            try:
                import shutil
                savelog=('code2run.log').split('.')[0]+'_rcr-2_2018.log'
                print(savelog)
                shutil.copy('code2run.log', os.path.join('./log',savelog))
                flash('Log saved as '+savelog, 'success')
            except:
                flash('No log file found to save','warning')
                print('Cant fine the files... oh no!')                

    return render_template('runcode.html',loglines=x,i=i,e=e,w=w,jira=jira)






# @app.route('/wip',methods=['GET', 'POST'])
# @is_logged_in
# def wip():
    
#     if request.method == 'GET':
#         get_log=request.values.get("submit")
#         clear_log=request.values.get("clear")

#         if get_log=='submit':
#             code_to_run('code2run.py')                                

#         if clear_log=='clear':
#             try:
#                 os.remove('code2run.log')
#             except:
#                 print('cant fine the files... oh no!')                
            
    
#     i=0
#     e=0
#     w=0
#     try:
#         with open("./code2run.log","r") as logfile:
#             #loglines =logfile.readlines()
#             loglines=logfile.readlines()

#             x=list()  
#             for item in loglines:
#                 if item.startswith("INFO"): 
#                     i=i+1
#                     x.append('<span style="color:blue;">'+str(item[10:])+'</span><br>')
#                 elif item.startswith("ERROR"): 
#                     e=e+1
#                     x.append('<span style="color:red;">'+str(item[11:])+'</span><br>')
#                 elif item.startswith("WARNING"): 
#                     w=w+1
#                     x.append('<span style="color:teal;">'+str(item[13:])+'</span><br>')
#     except:
#         x=list('<no file found yet>')
#     return render_template('wip.html',loglines=x,i=i,e=e,w=w)






# Vendors
# @app.route('/vendors')
# def vendors():
#     # Create cursor
#     cur = mysql.connection.cursor()
#     # Get vendors
#     result = cur.execute("SELECT * FROM vendors")
#     vendors = cur.fetchall()
#
#     if result > 0:
#         return render_template('vendors.html', vendors=vendors)
#     else:
#         msg = 'No Vendors Found'
#         return render_template('vendors.html', msg=msg)
#     # Close connection
#     cur.close()
#
# #Single Vendor
# @app.route('/vendor/<string:id>/')
# def vendor(id):
#     # Create cursor
#     cur = mysql.connection.cursor()
#     # Get vendor
#     result = cur.execute("SELECT * FROM accessrole WHERE id = %s", [id])
#     vendor = cur.fetchone()
#     return render_template('vendor.html', vendor=vendor)


if __name__ == '__main__':
    app.secret_key='secret123'
    app.run(port=5003,debug=True)
