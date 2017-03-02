'''
Created on 2017. 2. 17.

@author: thcho
'''


import MySQLdb


host = "localhost"
user = "thcho"
passwd = "12345"
db = "stock_ml"
conn = MySQLdb.connect(host, user, passwd, db)
x = conn.cursor()

x.execute("INSERT INTO STOCK_INFO VALUES (1,'SD','SD','SD','SD')")
x.execute("SELECT * FROM STOCK_INFO")
x.execute("commit")
print(x)
print(x.fetchone())
print(x)
print(x.fetchone())
conn.close()