from flask import Flask,request,render_template,jsonify
from encryption import *
from decryption import *
app = Flask(__name__)
@app.route('/')
def index():
      List_0=[0,0,0,0,0,0,0,0]
      List_1=[]
      for i in range(16):
         temp_list=[0,0,0,0,0,0,0,0,0,0]
         List_1.append(temp_list)
      return render_template('index.html',List_0=List_0,List_1=List_1,flag=0,method="")
@app.route('/calculate',methods= ['POST'])
def process():
      message = request.form['message']
      key = request.form['key']
      method = request.form['func']
      if(method == "encryption"):
            List_0,List_1,res = encryption(message,key)
            method="Encrypted "
      else:
            List_0,List_1,res = decryption(message,key)
            method="Decrypted "
      return render_template('index.html',List_0 = List_0,List_1 = List_1,res=res,flag=1,method=method)

if __name__ == '__main__':
    app.run(debug=True)