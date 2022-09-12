#app.py

from flask import Flask, render_template
#app instance
app = Flask(__name__)




#app goes to "/"
@app.route("/")
def hello():
    return render_template('home.html')

@app.route('/addTodo', method=['POST'])
def addTodo():
    #access body info


#runs python app
if  __name__ == "__main__":
    app.run(debug=True)



#all 4 of them pass info through query parameters and path parameters
#query params --> www.google.com?page=3&row=53782&user=joe
#path params --> www.google.com/someRootURL/3/53782/joe
    #preference


#POST and PUT
#info passed in body --> www.google.com


#GET, PUT, POST, DELETE
# GET and DELETE 

#CRUD - CREATE, RETRIEVE, UPDATE, DELETE
