from distutils.command.config import config
from multiprocessing.connection import Connection
import pymysql
from tgbot.bd_bot.db_loger import DB_USER, DB_HOST,DB_NAME,DB_PASS



def insert_data(id, name, phone):
    try:
        connection = pymysql.connect(
            host=DB_HOST,
            port= 3306,
            user=DB_USER,
            password=DB_PASS,
            database=DB_NAME,
            cursorclass=pymysql.cursors.DictCursor
        )
        print("successful")

        try:
            with connection.cursor() as cursor:
                insert_query = f"INSERT INTO Users (ID, name, phone_number) VALUES({id},'{name}','{phone}');"
                cursor.execute(insert_query)
                connection.commit()
        finally:
            connection.close()
    except Exception as ex:
        print("Connection refused...")
        print(ex)

def update_data_name(id, name):
    try:
        connection = pymysql.connect(
            host=DB_HOST,
            port= 3306,
            user=DB_USER,
            password=DB_PASS,
            database=DB_NAME,
            cursorclass=pymysql.cursors.DictCursor
        )
        print("successful")

        try:
            with connection.cursor() as cursor:
                update_query = f"UPDATE Users SET  name='{name}' WHERE ID = {id};"
                cursor.execute(update_query)
                connection.commit()
        finally:
            connection.close()
    except Exception as ex:
        print("Connection refused...")
        print(ex)

def update_data_phoone(id, phone):
    try:
        connection = pymysql.connect(
            host=DB_HOST,
            port= 3306,
            user=DB_USER,
            password=DB_PASS,
            database=DB_NAME,
            cursorclass=pymysql.cursors.DictCursor
        )
        print("successful")

        try:
            with connection.cursor() as cursor:
                update_query = f"UPDATE Users SET  phone_number='{phone}' WHERE ID = {id};"
                cursor.execute(update_query)
                connection.commit()
        finally:
            connection.close()
    except Exception as ex:
        print("Connection refused...")
        print(ex)

def view_data_id(id):
    try:
        connection = pymysql.connect(
            host=DB_HOST,
            port= 3306,
            user=DB_USER,
            password=DB_PASS,
            database=DB_NAME,
            cursorclass=pymysql.cursors.DictCursor
        )
        print("successful")

        try:
            with connection.cursor() as cursor:
                select_all_rows = "SELECT ID FROM Users"
                cursor.execute(select_all_rows)
                rows = cursor.fetchall()
                for row in rows:
                    if row["ID"] == id:
                        return (row["ID"])
                return(None)
        finally:
            connection.close()
    except Exception as ex:
        print("Connection refused...")
        print(ex)

def view_data_name(id):
    try:
        connection = pymysql.connect(
            host=DB_HOST,
            port= 3306,
            user=DB_USER,
            password=DB_PASS,
            database=DB_NAME,
            cursorclass=pymysql.cursors.DictCursor
        )
        print("successful")

        try:
            with connection.cursor() as cursor:
                select_all_rows = "SELECT * FROM Users"
                cursor.execute(select_all_rows)
                rows = cursor.fetchall()
                for row in rows:
                    if row["ID"] == id:
                        print(row)
                        return (row["name"])
        finally:
            connection.close()
    except Exception as ex:
        print("Connection refused...")
        print(ex)

def view_data_phone(id):
    try:
        connection = pymysql.connect(
            host=DB_HOST,
            port= 3306,
            user=DB_USER,
            password=DB_PASS,
            database=DB_NAME,
            cursorclass=pymysql.cursors.DictCursor
        )
        print("successful")

        try:
            with connection.cursor() as cursor:
                select_all_rows = "SELECT * FROM Users"
                cursor.execute(select_all_rows)
                rows = cursor.fetchall()
                for row in rows:
                    if row["ID"] == id:
                        return (row["phone_number"])
        finally:
            connection.close()
    except Exception as ex:
        print("Connection refused...")
        print(ex)
