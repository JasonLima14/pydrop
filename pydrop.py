from bcrypt import gensalt,hashpw
import sqlite3

def welcome():
	print("Welcome to your dashboard")

def auth():
    uid = input("Username: ")
    pwd = input("Password: ")

    #TODO Look for UID in DB and retrieve password

    #TODO check password with bcrypt

    #TODO If user does no exist print user does not exist, would you like to create an account and route to register exit on no


		

def register():
    uid = input("Username: ")
    pwd = input("Password: ").encode()
    pwdConfirm = input("Confirm password: ")
    hashed = hashpw(pwd, gensalt())
    # TODO READ TO SEE IF USER EXISTS
    read_from_db(uid)
    # TODO IF USER DOES NOT EXIST CREATE
    write_to_db(uid, hashed.decode())
    welcome()

    


def write_to_db(uid, pwd, filename='data.db'):
    add_user_sql = "INSERT INTO users VALUES ('{}','{}')"
    conn, cursor = create_connection()
    print(conn, cursor)
    cursor.execute(add_user_sql.format(uid, pwd))
    conn.commit()

def read_from_db(uid, filename='data.db'):
    conn, cursor = create_connection()
    row = cursor.execute("SELECT * FROM users").fetchall()
    print(row)

def create_connection():
    connection = sqlite3.connect('data.db')
    cursor = connection.cursor()
    return connection, cursor

def home():
	print("Welcome, please select an option")
	option = (input("Login or Signup: ")).lower()
	if option == "login":
		auth()
	elif option == "signup":
		register()
	else:
		home()


home()