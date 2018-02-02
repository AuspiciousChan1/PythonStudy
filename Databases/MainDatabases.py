from Databases import MySQLHandler

mysql = MySQLHandler.MySQLHandler(user="AuspiciousChan", password="123456", database="mysql_study")
colu_dic = {}
colu_dic['id'] = ["INT", "AUTO_INCREMENT", "PRIMARY KEY"]
colu_dic['value'] = ["INT"]
print(mysql.create_table("new_table", colu_dic))
print(mysql.drop_table(("new_table")))

