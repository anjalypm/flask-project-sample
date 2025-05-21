from flask import Flask,render_template
app =Flask(__name__)

@app.route('/')
def index():
    fruits=["apple","orange","pineapple","mango"]
    return render_template('index.html',items=fruits)


@app.route('/users')
def listuser():
    users=["user1-amal" ,"user2-vineeth","user3-amala"]
    return render_template('users.html',users=users)
if __name__=='__main__':
        app.run(debug=True)

        
@app.route('/GRADE')
def index():
    students=["GRADE A","GRADE B","GRADE C","GRADE D"]
    return render_template('.html',students=GRADE)
