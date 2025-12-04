import pymysql
from tkinter import messagebox

def connect_database():
    global mycur, con
    try:
        con = pymysql.connect(host='localhost', user='root', password='dileep8542')
        mycur = con.cursor()
    except Exception as e:
        messagebox.showerror('Error', f'Connection not established: {e}')
        return

    mycur.execute('CREATE DATABASE IF NOT EXISTS student_data')
    mycur.execute('USE student_data')
    # Corrected CREATE TABLE with closing parenthesis
    mycur.execute('''
        CREATE TABLE IF NOT EXISTS college (
          id varchar(20),
          name varchar(50),
          fname varchar(50),
          DOB varchar(20),
          Email varchar(50),
          Gender varchar(20),
          clas varchar(20),
          section varchar(4),
          contact varchar(20),
          Address varchar(200)
        )
    ''')

connect_database()

def insert(id, name, fname, dob, email, gender, clas, section, contact, address):
    # Specify columns, and separate %s placeholders properly
    sql = '''
        INSERT INTO college
        (id, name, fname, DOB, Email, Gender, clas, section, contact, Address)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
    '''
    mycur.execute(sql, (id, name, fname, dob, email, gender, clas, section, contact, address))
    con.commit()

def id_exists(id):
    mycur.execute('SELECT COUNT(*) FROM college WHERE id = %s', (id,))
    result = mycur.fetchone()
    print(result)
    return result[0] > 0

def fetch_records():
    mycur.execute('SELECT * FROM college')
    result=mycur.fetchall()
    return result

def update(id, name, fname, dob, email, gender, clas, section, contact, address):
    sql = """
        UPDATE college
        SET id = %s,
            name = %s,
            fname = %s,
            dob = %s,
            email = %s,
            gender = %s,
            clas = %s,
            section = %s,
            contact = %s,
            address = %s
        WHERE id = %s
    """
    params = (id, name, fname, dob, email, gender, clas, section, contact, address, id)
    mycur.execute(sql, params)
    con.commit()

def delete(id):
    mycur.execute('DELETE FROM college WHERE id=%s',id)
    con.commit()


def search(opt,val):
    mycur.execute(f'SELECT* FROM college WHERE {opt}=%s',val)
    result=mycur.fetchall()
    return result


def delete_all():
    mycur.execute('TRUNCATE TABLE college')
    con.commit()



