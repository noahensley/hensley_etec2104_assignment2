import tornado.web

D={
    "alice": {
        "name" : "Alice Smith", 
        "dob" : "Jan. 1",
        "email": "alice@example.com"
    },
    "bob": { 
        "name" : "Bob Jones",
        "dob" : "Dec. 31",
        "email" : "bob@bob.xyz"
    },
    "carol": {
        "name" : "Carol Ling",
        "dob" : "Jul. 17",
        "email" : "carol@example.com"
    },
    "dave": {
        "name" : "Dave N. Port",
        "dob" : "Mar. 14",
        "email" : "dave@dave.dave"
    }
}

class Handler(tornado.web.RequestHandler):
    def get(self):
        L = self.request.path.split("/")
        # print(L)
        uname = L[2]
        info = D[uname]
        if info:
            self.render( "ProfilePage.html",
                name=info["name"], dateOfBirth=info["dob"],
                email=info["email"], user=uname)