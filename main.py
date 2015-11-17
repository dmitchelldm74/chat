from flask import Flask, request, render_template

app = Flask(__name__)


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
        e = open('ewilson.txt', 'r+')
        wil = e.read()
        f = open('Daniel.txt', 'r+')
        f3 = f.read()
        #print f3
        air = open('Airrider295.txt', 'r+')
        rider = air.read()
        pub = open('Public.txt', 'r+')
        lic = pub.read() 
        result = '<div id="d1"><p>%s</p><br></div><div id="d1"><p>%s</p><br></div><div id="d1"><p>%s</p><br></div><div id="d1"><p>%s</p><br></div>' % (f3, wil, rider, lic)
        return render_template('form.html', posts=[f3, wil, rider, lic])
    elif request.method == 'POST':
        ps = request.form['password']
        msg = request.form['msg']
        us1 = request.form['user']
        fle = "%s.txt" % us1
        if ps == 'del':
            f = open(fle, 'w')
            f.truncate()
            f.close() 
        if us1 == 'Daniel' and  ps == 'blog123':
            f = open(fle, 'a+')
            user = "@%s:\t" % us1
            msgcontent = user + msg
            #f.truncate()
            f.write(msgcontent)      
            f.close() 
        if us1 == 'Airrider295' and  ps == 'airrider':
            f = open(fle, 'a+')
            user = "@%s:\t" % us1
            msgcontent = user + msg
            #f.truncate()
            f.write(msgcontent)
            f.close() 
                
        if us1 == 'ewilson' and  ps == 'ewilson':
            f = open(fle, 'a+')
            user = "@%s:\t%s\n" % (us1, msg)
            msgcontent = user 
            #f.truncate()
            f.write(msgcontent)
            f.close() 
        if us1 == 'Public' and  ps == '':
            f = open("Public.txt", 'a+')
            user = "@Public:\t"
            msgcontent = user + msg
            #f.truncate()
            f.write(msgcontent)
            f.close()
        qw = open('Daniel.txt', 'r') 
        f4 = qw.read()   
        e2 = open('ewilson.txt', 'r+')
        wil2 = e2.read()
        ai = open('Airrider295.txt', 'r+')
        ride = ai.read()
        lic = open('Public.txt', 'r+')
        pub = lic.read()    
        return render_template('form.html', posts=[f4, wil2, ride, pub])
        
@app.route('/@ewilson')
def ew():
    # long for the long message
    elong = open('ewilson.txt', 'r')
    willong = elong.read()
    result = '''<div id="d1"><p>%s</p><br></div>''' % willong
    return render_template('@', lng=[result, '<a href="/post">Home</a>'])
    
@app.route('/@Daniel')
def me():
    # long for the long message
    elong = open('Daniel.txt', 'r')
    willong = elong.read()
    result = '''<div id="d1"><p>%s</p><br></div>''' % willong
    return render_template('@', lng=[result, '<a href="/post">Home</a>'])
@app.route('/@Airrider295')    
def airride():
    # long for the long message
    elong = open('Airrider295.txt', 'r')
    willong = elong.read()
    result = '''<div id="d1"><p>%s</p><br></div>''' % willong
    return render_template('@', lng=[result, '<a href="/post">Home</a>'])    
@app.route('/@Public')    
def public():
    # long for the long message
    f = open('Public.txt', 'r')
    f2 = f.read()
    f.close()
    result = '''<div id="d1"><p>%s</p><br></div>''' % f2
    return render_template('@', lng=[result, '<a href="/post">Home</a>']) 
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
    #get_pass = raw_input('Enter "a" to Start>>> ')
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
