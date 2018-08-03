import MySQLdb


def connection():
    conn = MySQLdb.connect(host="localhost",
                           user="your_sql_username",
                           passwd="your_sql_password",
                           db="kleflogbook")
    c = conn.cursor()
    return c, conn
