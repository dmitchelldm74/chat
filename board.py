from flask import Flask, request, render_template

import post_dao

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
        posts = post_dao.get_posts()
        return render_template('form.html', posts=posts)
    elif request.method == 'POST':
        ps = request.form['password']
        msg = request.form['msg']
        us1 = request.form['user']
        post_dao.add_post(ps, msg, us1)
        posts = post_dao.get_posts()
        return render_template('form.html', posts=posts)


if __name__ == '__main__':
    app.run(debug=True)
