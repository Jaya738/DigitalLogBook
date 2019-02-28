import mysql.connector


def connection():
    conn = mysql.connector.connect(host="database host address",
                           user="username",
                           passwd="password",
                           db="Database created for log book")
    c = conn.cursor()
    return c, conn
