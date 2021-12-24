import configparser
import mysql.connector as connector

config = configparser.ConfigParser()
config.read("config.ini")

def connect():
    return connector.connect(host=config['mysqlDB']['host'],
    user=config['mysqlDB']['user'],
    password=config['mysqlDB']['password'],
    database=config['mysqlDB']['database'])

def select_one_sql(field_name,table_name,where_field_name,where_value):
        try:
            db = connect()
            cursor = db.cursor()
            query = "select  {0}  from {1} where   {2} ='{3}'".format(field_name,table_name,where_field_name,where_value)
            cursor.execute(query)
            one_records = cursor.fetchone()
        except TypeError as e:
            raise Exception(e)
        finally:
            cursor.close()
            db.close()
        return one_records


    