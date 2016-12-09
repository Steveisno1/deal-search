import sqlite3

db = sqlite3.connect('deals.sqlite')

c = db.cursor()

try:
	c.execute('''CREATE TABLE coupons(item varchar(300), image varchar(300), link varchar(300), description varchar(300), feature varchar(300))''')
	db.commit()
except:
	pass

try:
	query = "INSERT INTO coupons SELECT * FROM dealmoon UNION SELECT * FROM dealsea UNION SELECT * FROM slickdeal"
	c.execute(query)
	db.commit()
except:
	pass