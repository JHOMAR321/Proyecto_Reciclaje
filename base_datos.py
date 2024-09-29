import sqlite3

conn=sqlite3.connect('datos_residuos.db')
c=conn.cursor()

def create_table():
	c.execute("CREATE TABLE IF NOT EXISTS administrador(codigo TEXT,tipo TEXT ,cantidad TEXT)")
	conn.commit()
	c.execute("INSERT INTO administrador values ('tf85','Sólido','3')")
	conn.commit()

	c.close()
	conn.close()

create_table()