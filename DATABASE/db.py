import sqlite3

class Database:
	def __init__(self, db):
		self.conn = sqlite3.connect(db)
		self.cur = self.conn.cursor()
		self.cur.execute("CREATE TABLE IF NOT EXISTS Employee (id INTEGER PRIMARY KEY, FistName text, \
			LastName text, CellNumber text, EmployeeID text, EmployeePosistion text, Gender text)")
		self.conn.commit()
	def fetch(self):
		self.cur.execute("SELECT * FROM Employee")
		rows = self.cur.fetchall()
		return rows

	def insert(self,FistName,LastName, CellNumber, EmployeeID, EmployeePosistion, Gender):
		self.cur.execute("INSERT INTO Employee VALUES (NULL,?,?,?,?,?,?)", \
			(FistName,LastName, CellNumber, EmployeeID, EmployeePosistion, Gender))
		self.conn.commit()

	def remove(self, id):
		self.cur.execute("DELETE FROM Employee WHERE id=?", (id,))
		self.conn.commit()

	def __del__(self):
		self.conn.close()

'''db = Database('store.db')
db.insert("Siphephelo", "Mlungwana", "0785894256", "D15159", "DevOps", "Male")
db.insert("Sabelo", "Mlungwana", "0827211308", "D15159", "SysOps", "Male")
db.insert("Ayanda", "Mngomezulu", "0785894256", "D15159", "Elecrical", "Male")
db.insert("Zanele", "Mlungwana", "0785894256", "D15159", "Designer", "Female")'''