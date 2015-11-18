from flask import Flask, request, render_template

app = Flask(__name__)

password = open('passwords.txt', 'r+')
password1 = password.read()
pwd = password1.split('[*]') 
password.close()

@app.route('/')
@app.route('/hello')
def hello_world():
    return render_template('hello.html')


@app.route('/goodbye/<user>')
def goodbye(user):
    return render_template('bye.html', user=user)
    


@app.route('/post', methods = ['GET', 'POST'])
def post():
    if request.method == 'GET':
        pub = open('Public.txt', 'r+')
        lic = pub.read() 
        result = '<div id="d1"><p>%s</p><br></div>' % (lic)
        return render_template('form.html', posts=[result])
    elif request.method == 'POST':
        ps = request.form['password']
        msg = request.form['msg']
        us1 = request.form['user']
        to = request.form['to']
        fle = "%s.txt" % us1
        fle2 = "%s:inbox" % to
        def send_to():
            if to == 'ewilson' or to == 'Daniel' or to == 'Airrider295' or to == 'Public':
                f = open(fle2, 'a+')
                user = "@%s:\n" % us1
                msgcontent = user + msg
                f.write(msgcontent)      
                f.close() 
                f = open(fle, 'a+')
                user = "@%s:\n" % us1
                msgcontent = user + msg
                f.write(msgcontent)      
                f.close()       
                
            if to == '':
                f = open('Public.txt', 'a+')
                user = "@%s:\t" % us1
                msgcontent = user + msg
                f.write(msgcontent)      
                f.close()
                f = open(fle, 'a+')
                user = "@%s:\n" % us1
                msgcontent = user + msg
                f.write(msgcontent)      
                f.close()       
        if ps == 'del':
            f = open(fle, 'w')
            f.truncate()
            f.close() 
        global pwd    
        if us1 == 'Daniel' and  ps == pwd[1]:
            send_to()
            
        if us1 == 'Airrider295' and  ps == pwd[2]:
            send_to()
            
        if us1 == 'ewilson' and  ps == pwd[0]:
            send_to()
            
        if ps == '':
            send_to()
            
        lic = open('Public.txt', 'r+')
        pub = lic.read() 
        result = '<div id="d1"><p>%s</p><br></div>' % (pub)   
        return render_template('form.html', posts=[result])
        
@app.route('/@ewilson:inbox', methods = ['GET', 'POST'])
def ew():
    if request.method == 'GET':
        return render_template('sign-in.html', pas=('/@ewilson:inbox'))
    elif request.method == 'POST':
        global pwd
        ps = request.form['pass']
        if ps == pwd[0]:
            elong = open('ewilson:inbox', 'r+')
            willong = elong.read()
            result = '''<h1>Inbox:</h1><div id="d1"><p>%s</p><br></div>''' % willong
            f12 = open('ewilson.txt', 'r+')
            rd = f12.read()
            sent = '''<h1>Sent:</h1><div id="d1"><p>%s</p><br></div>''' % rd
            return render_template('@', lng=[result, sent, '<a href="/post">Home</a>'])
        else:
            return 'Wrong Password...'
        
@app.route('/@Daniel:inbox', methods = ['GET', 'POST'])
def me():
    if request.method == 'GET':
        return render_template('sign-in.html', pas=('/@Daniel:inbox'))
    elif request.method == 'POST':
        global pwd
        ps = request.form['pass']
        if ps == pwd[1]:
            elong = open('Daniel:inbox', 'r+')
            willong = elong.read()
            result = '''<h1>Inbox:</h1><div id="d1"><p>%s</p><br></div>''' % willong
            f12 = open('Daniel.txt', 'r+')
            rd = f12.read()
            sent = '''<h1>Sent:</h1><div id="d1"><p>%s</p><br></div>''' % rd
            return render_template('@', lng=[result, sent, '<a href="/post">Home</a>'])
        else:
            return 'Wrong Password...'
@app.route('/@Airrider295:inbox', methods = ['GET', 'POST'])    
def airride():
    if request.method == 'GET':
        return render_template('sign-in.html', pas=('/@Airrider295:inbox'))
    elif request.method == 'POST':
        global pwd
        ps = request.form['pass']
        if ps == pwd[2]:
            elong = open('Airrider295:inbox', 'r+')
            willong = elong.read()
            result = '''<h1>Inbox:</h1><div id="d1"><p>%s</p><br></div>''' % willong
            f12 = open('Airrider295.txt', 'r+')
            rd = f12.read()
            sent = '''<h1>Sent:</h1><div id="d1"><p>%s</p><br></div>''' % rd
            return render_template('@', lng=[result, sent, '<a href="/post">Home</a>'])
        else:
            return 'Wrong Password...'
       
@app.route('/@Public:inbox')    
def public():
    f = open('Pubic:inbox', 'r+')
    f2 = f.read()
    f.close()
    result = '''<h1>Inbox:</h1><div id="d1"><p>%s</p><br></div>''' % f2
    f12 = open('Public.txt', 'r+')
    rd = f12.read()
    sent = '''<h1>Sent:</h1><div id="d1"><p>%s</p><br></div>''' % rd
    return render_template('@', lng=[result, sent, '<a href="/post">Home</a>']) 
    
@app.route('/@All')    
def al():
    qw = open('Daniel.txt', 'r') 
    f4 = qw.read()   
    e2 = open('ewilson.txt', 'r+')
    wil2 = e2.read()
    ai = open('Airrider295.txt', 'r+')
    ride = ai.read()
    lic = open('Public.txt', 'r+')
    pub = lic.read()    
    result = '''<div id="d1"><p>%s</p><br></div><div id="d1"><p>%s</p><br></div><div id="d1"><p>%s</p><br></div><div id="d1"><p>%s</p><br></div>''' % (f4, wil2, ride, pub)
    return render_template('@', lng=[result, '<a href="/post">Home</a>'])         
@app.route('/@del')
def truncate():
    get_pass = 'admin.permission'
    if get_pass == 'admin.permission':
        elong = open('ewilson.txt', 'w')
        elong.truncate()
        elong.close()
        elong = open('Daniel.txt', 'w')
        elong.truncate()
        elong.close()
        elong = open('Airrider295.txt', 'w')
        elong.truncate()
        elong.close()
        elong = open('Public.txt', 'w')
        elong.truncate()
        elong.close()
        Do = 'DELETED ALL DATA'
    else:
        Do = 'Failed to get Administrator Priveledges.'   
    return render_template('@', lng=[Do, '<a href="/post">Home</a>'])    

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0")
