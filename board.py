from flask import Flask, request, render_template
#g = open('Messages.txt', 'r')
#p = g.readlines()
#pt = p.split("\n+$+\n")
#second = int(1,100)
#with open(, 'r+') as f:
        #content = f.read()
        #f.seek(0, 0)
#p1 = str(content)       
#with open('Messages.txt', 'r') as content_file:
    #content = content_file.read()
    #nc = content.split("+$+")
    #nc2 = len(nc)
    #print nc2
    #p8 = nc2
    #for nc2 in nc:
        #nc3 = content
app = Flask(__name__)


@app.route('/')
@app.route('/hello')
def hello_world():
    name = request.args.get('name')
    name = name if name else 'World'
    return render_template('hello.html', name=name)


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
        air = open('Airrider295.txt', 'r+')
        rider = air.read()
        pub = open('Public.txt', 'r+')
        lic = pub.read() 
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
            user = "@%s:\n" % us1
            msgcontent = user + msg
            f.write(msgcontent)
            f.close() 
        if us1 == 'Airrider295' and  ps == 'airrider':
            f = open(fle, 'a+')
            user = "@%s:\n" % us1
            msgcontent = user + msg
            f.write(msgcontent)
            f.close() 
                
        if us1 == 'ewilson' and  ps == 'ewilson':
            f = open(fle, 'a+')
            user = "@%s:\n" % us1
            msgcontent = user + msg
            f.write(msgcontent)
            f.close() 
        if us1 == 'Public' and  ps == '':
            f = open("Public.txt", 'a+')
            user = "@Public:\n"
            msgcontent = user + msg
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

if __name__ == '__main__':
    app.run(debug=True)
