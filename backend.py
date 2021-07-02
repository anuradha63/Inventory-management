import sqlite3

def connect():
    conn=sqlite3.connect("bookstore.db")
    cur=conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS book (id INTEGER PRIMARY KEY, TOOL_NAME text, Manufacturer text, Quantity integer, Supplier_Name text,date integer)")
    conn.commit()
    conn.close()

def insert(id,TOOL_NAME,Manufacturer,Quantity,Supplier_Name):
    conn=sqlite3.connect("bookstore.db")
    cur=conn.cursor()
    cur.execute("INSERT INTO book VALUES (?,?,?,?,?)",(id,TOOL_NAME,Manufacturer,Quantity,Supplier_Name))
    conn.commit()
    conn.close()
    view()

def view():
    conn=sqlite3.connect("bookstore.db")
    cur=conn.cursor()
    cur.execute("SELECT * FROM book")
    rows=cur.fetchall()
    conn.close()
    return rows


def search(TOOL_NAME="",Manufacturer="",Quantity="",Supplier_Name=""):
   conn=sqlite3.connect("bookstore.db")
   cur=conn.cursor()
   cur.execute("SELECT * FROM book WHERE TOOL_NAME=? OR Manufacturer=? OR Quantity=? OR Supplier_Name=? ", (TOOL_NAME,Manufacturer,Quantity,Supplier_Name))
   rows=cur.fetchall()
   conn.close()
   if len(rows)==0:
        return ["No record found"]
   else:
        return rows




def delete(id):
    conn=sqlite3.connect("bookstore.db")
    cur=conn.cursor()
    cur.execute("DELETE FROM book WHERE id=?",(id,))
    conn.commit()
    conn.close()

def update(id,TOOL_NAME,Manufacturer,Quantity,Supplier_Name):
    conn=sqlite3.connect("bookstore.db")
    cur=conn.cursor()
    cur.execute("UPDATE book SET TOOL_NAME=?, Manufacturer=?, Quantity=?, Supplier_Name=?,  WHERE id=?",(id,TOOL_NAME,Manufacturer,Quantity,Supplier_Name))
    conn.commit()
    conn.close()

connect()