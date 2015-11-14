# dao stands for data-access-object, a common naming convention
def get_posts():
    e = open('ewilson.txt', 'r+')
    wil = e.read()
    f = open('Daniel.txt', 'r+')
    f3 = f.read()
    air = open('Airrider295.txt', 'r+')
    rider = air.read()
    pub = open('Public.txt', 'r+')
    lic = pub.read()
    return [f3, wil, rider, lic]


def add_post(password, message, user):
    fle = "%s.txt" % user
    if password == 'del':
        f = open(fle, 'w')
        f.truncate()
        f.close()
    if user == 'Daniel' and  password == 'blog123':
        f = open(fle, 'a+')
        user = "@%s:\n" % user
        msgcontent = user + message
        f.write(msgcontent)
        f.close()
    if user == 'Airrider295' and  password == 'airrider':
        f = open(fle, 'a+')
        user = "@%s:\n" % user
        msgcontent = user + message
        f.write(msgcontent)
        f.close()

    if user == 'ewilson' and  password == 'ewilson':
        f = open(fle, 'a+')
        user = "@%s:\n" % user
        msgcontent = user + message
        f.write(msgcontent)
        f.close()
    if user == 'Public' and  password == '':
        f = open("Public.txt", 'a+')
        user = "@Public:\n"
        msgcontent = user + message
        f.write(msgcontent)
        f.close()
