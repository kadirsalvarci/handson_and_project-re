from flask import Flask,redirect,url_for,render_template,request #render template template calsitirmak isin 

app=Flask(__name__)
@app.route('/')
def head():
    return render_template('index.html', number1=12, number2=34)#farkli degiskende koyabilirim burada index icinde n1 cagirilirsa 12 olsun 

@app.route('/ikinci')
def head2():
    return render_template('yeni.html', hazirlayan = "kadir" )

if __name__ == '__main__':
    #DEBUG is SET to TRUE. CHANGE FOR PROD
    app.run(port=5000,debug=True)