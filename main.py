from flask import Flask, request, render_template

app = Flask(__name__)

password = open('passwords.txt', 'r+')
password1 = password.read()
pwd = password1.split('[*]') 
password.close()

text = open('accounts.txt', 'r+')
txt = text.read()
text.close()
     
#if us1 in txt and  ps == pwd[2]:
    #send_to()
#if us1 in txt and  ps == pwd[0]:
    #send_to()
            
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
        result = '%s' % (lic)
        return render_template('form.html', posts=[result])
    elif request.method == 'POST':
        password = open('passwords.txt', 'r+')
        password1 = password.read()
        pwd = password1.split('[*]') 
        password.close()

        text = open('accounts.txt', 'r+')
        txt = text.read() 
        text.close()
        import datetime
        senttime = datetime.datetime.now().strftime("%I:%M%p on %B %d, %Y")
        ps = request.form['password']
        msg = request.form['msg']
        us1 = request.form['user']
        to = request.form['to']
        fle = "%s.txt" % us1
        fle2 = "%s:inbox" % to
        def send_to():
            text = open('accounts.txt', 'r+')
            txt = text.read() 
            text.close()
            if to in txt:
                f = open(fle2, 'a+')
                user = "@%s:\n" % us1
                msgcontent = '<div id="d1"><br>' + user + msg + '<br>Sent at:&nbsp' + senttime + '<br>' + '</div><br>'
                f.write(msgcontent)      
                f.close() 
                f = open(fle, 'a+')
                user = "@%s:\n" % us1
                msgcontent = '<div id="d1"><br>' + user + msg + '<br>Sent at:&nbsp' + senttime + '<br>' + '</div><br>'
                f.write(msgcontent)      
                f.close()       
                
            if to == '':
                f = open('Public.txt', 'a+')
                user = "@%s:\t" % us1
                msgcontent = '<div id="d1"><br>' + user + msg + '<br>Sent at:&nbsp' + senttime + '<br>' + '</div><br>'
                f.write(msgcontent)      
                f.close()
                f = open(fle, 'a+')
                user = "@%s:\n" % us1
                msgcontent = '<div id="d1"><br>' + user + msg + '<br>Sent at:&nbsp' + senttime + '<br>' + '</div><br>'
                f.write(msgcontent)      
                f.close()       
        if ps == 'del':
            f = open(fle, 'w')
            f.truncate()
            f.close() 
           
      
        if us1 in txt and ps in password1:
            send_to()
       
        if ps == '':
            send_to()
            
        lic = open('Public.txt', 'r+')
        pub = lic.read() 
        result = '%s' % (pub)   
        return render_template('form.html', posts=[result])
        
@app.route('/@user:inbox', methods = ['GET', 'POST'])
def ew():
    if request.method == 'GET':
    
        return render_template('sign-in.html', pas=('/@user:inbox'))
    elif request.method == 'POST':
        password = open('passwords.txt', 'r+')
        password1 = password.read()
        pwd = password1.split('[*]') 
        password.close()

        text = open('accounts.txt', 'r+')
        txt = text.read()
        text.close()
        ps = request.form['pass']
        user = request.form['user']
        if user in txt:
            if ps in password1:
                ope = user + ':inbox'
                elong = open(ope, 'r+')
                willong = elong.read()
                result = """<h1>Inbox:</h1>%s""" % willong
                se = user + '.txt'
                f12 = open(se, 'r+')
                rd = f12.read()
                sent = '''<h1>Sent:</h1>%s''' % rd
                return render_template('@', cr={'ps': ps, 'us': user}, lng=[result, sent, '<a id="link" href="/post">Home</a>'])
            else:
                return 'Wrong Password...'
        
@app.route('/create', methods = ['GET', 'POST'])
def me():
    if request.method == 'GET':
        return render_template('create.html')
    elif request.method == 'POST':
        
        ps = request.form['pass']
        user = request.form['user']
        
        name = user + ':inbox'
        name2 = user + '.txt'
        f = open(name, 'w')
      
        f.close()
        f12 = open(name2, 'w')
  
        f = open('accounts.txt', 'a+')
        msgcontent = user + '[*]'
        f.write(msgcontent)      
        f.close() 
        f = open('passwords.txt', 'a+')
        msgcontent = ps + '[*]'
        f.write(msgcontent)      
        f.close()       
        msg = 'Successful!'
        return render_template('form.html', lng=[msg, '<a id="link" href="/post">Home</a>'])
        
           

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
    return render_template('@', lng=[Do, '<a id="link" href="/post">Home</a>'])    

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0")
