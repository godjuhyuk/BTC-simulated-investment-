# from urllib import request
import webbrowser
import requests
import mariadb
import class_model
import flask 
from flask_cors import CORS
from flask import Flask,request, render_template
app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}}) 

@app.route("/")
def hello():
    return render_template('test.html')

@app.route("/test", methods=['POST'])
def test():
    if request.method == "POST":
        data = request.json['data']
        model = class_model.model()
        model.bid(data)
    return model.bid(data)
@app.route("/go_to_create")
def hello1():

	return render_template('test2.html')
@app.route("/create_id", methods = ['POST'])
def create_id():
    if request.method=="POST":
        data = request.json
        model = class_model.model()
        rslt = model.create_id(data)
        return rslt

@app.route("/get_api", methods = ['GET'])
def get():
    if request.method == "GET":
        coin_data = requests.get("https://api.bithumb.com/public/ticker/ALL_KRW")
        data = coin_data.json()
        data = data['data']
        del data['date']
        # print(dict(sorted(data.items() ,key = lambda item : float(item[1]['acc_trade_value_24H']), reverse=True)))
        
        return data

       
    # conn = mariadb.connect(host="127.0.0.1", user="root", password="1234", port=3306,db="stuuuudy")
    # curs = conn.cursor()
    # coin_name = 'ETH'
    # how_much = 10000000
    # coin_data = requests.get("https://api.bithumb.com/public/ticker/"+coin_name+"_KRW")
    # data = coin_data.json()
    # sql1 = 'SELECT money FROM wallet'
    # curs.execute(sql1)
    # row = curs.fetchall()
    # print(row)
    # sql2 = 'UPDATE wallet SET money = '+ str(row[0][0]-how_much) + ' WHERE wallet_id = 1'
    # curs.execute(sql2)  
    # coin_data = requests.get("https://api.bithumb.com/public/ticker/"+coin_name+"_KRW")
    # data = coin_data.json()
    # sql3 = 'UPDATE wallet SET '+coin_name+' = ' + str(how_much/float(data['data']['closing_price'])) + ' WHERE wallet_id = 1'
    # curs.execute(sql3)
    # conn.commit()
    # conn.close()
    # return render_template('test.html')




webbrowser.open('http://127.0.0.1:5000')



if __name__ == "__main__":
		app.run()   
        