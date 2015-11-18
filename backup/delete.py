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
