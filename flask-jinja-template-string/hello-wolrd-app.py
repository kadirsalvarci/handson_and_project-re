from flask import Flask,redirect,url_for,render_template,request
#burda string olarak donduk yaeni return sonunda ne 
app=Flask(__name__) # name almak zorundayiz direk calismasi icin 
@app.route('/')# dekorater  nereye adresleme yapilaca "/"  yani burda donecegi yer -- enterlamak request 
def head():# fonksiyon tanimyalip ne yapcagina karar veriyoruz
    return "Hello World!"

@app.route("/second") # burada nereden gosterecegiz bunu yaziyoruz
def second():
    return "this is the second"

@app.route("/third/<string:id>") # burada nereden gosterecegiz bunu yaziyoruz, du dinamik id icin ne vereceksek o gelecek 
def third(id):
    return f"this is the second {id}" #dinamik web sayfalar icin 

if __name__ == '__main__': # name main e yani dosyanin kendisine atanmismi kontroldur  
    #DEBUG is SET to TRUE. CHANGE FOR PROD
    app.run(port=5000,debug=True)