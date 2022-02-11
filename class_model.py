import mariadb
import requests
class model:

    def bid(self,data):
        data+= "aaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
        print(data)
        return data
    def create_id(self,data):
        conn = mariadb.connect(host="127.0.0.1", user="root", password="1234", port=3306,db="stuuuudy")
        curs = conn.cursor()
        sql = 'INSERT INTO user(user_email,user_pw) VALUES ( "' +data['id']+'", "'+ data['pw'] + '")'
        try :
            curs.execute(sql)
            conn.commit()
            conn.close()
            return 'SUCCESS'
        except :
            print('sql is ===============>',sql)
            return 'FAIL'

# class render_model:
    
#     def bring_coin_data(self):
#         coin_data = requests.get("https://api.bithumb.com/public/ticker/"+coin_name+"_KRW")
#         data = coin_data.json()
#         print(data)