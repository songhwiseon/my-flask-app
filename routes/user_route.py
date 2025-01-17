from flask import render_template,request,jsonify,Blueprint
import pymysql
from db import get_db_connection

user_route = Blueprint('user',__name__)

# 회원가입 
@user_route.route("/add-user", methods=['post'])
def adduser():

    #아이디 중복

    data = request.json

    id = data.get('id')
    pw = data.get('pw')
    nick = data.get('nick')
    type = data.get('type')
    address = data.get('address')
    

    conn = get_db_connection()
    cursor = conn.cursor(pymysql.cursors.DictCursor)

    query = """
    INSERT INTO user
    (id,pw,nick,type,address,created_date)
    VALUES
    (%s,md5(%s),%s,%s,%s,sysdate())
"""

    cursor.execute(query,(id,pw,nick,type,address))
    conn.commit()
    cursor.close()
    conn.close()

    return jsonify({"message":"ok"})



#회원 조회
@user_route.route("/user")  
def detailUser():
    user_idx = request.args.get("user_idx") 
    
    try:
        connection = get_db_connection()
        cursor = connection.cursor(pymysql.cursors.DictCursor)
        cursor.execute("SELECT * FROM user where user_idx=%s",(user_idx,))
        users = cursor.fetchone()
        return jsonify(users)
    except Exception as e:
        return jsonify({"error": str(e)})
    finally:
        cursor.close()
        connection.close()
    
    