import pymysql


# def get_db_connection():
#     return pymysql.connect(
#         host='43.201.69.136',
#         port=3306,
#         user='hwiseon',
#         password='1234',
#         database='my_db',
        
#     )


def get_db_connection():
    return pymysql.connect(
        host='127.0.0.1',
        port=3306,
        user='root',
        password='12345',
        database='my_db',
        
    )