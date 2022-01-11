
#1 -> psql -U postgres
#2 CREATE DATABASE pythondb;
#3 \c pythondb;

import psycopg2
from decouple import config

DROP_TABLE_USERS = "DROP TABLE IF EXISTS users"

USERS_TABLE = """CREATE TABLE users(
    id SERIAL,
    username VARCHAR(50) NOT NULL,
    password VARCHAR(50) NOT NULL,
    email VARCHAR(50) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
)"""

#Insertar multiples registros
users = [
    ("user1","password","user1@yahoo.com"),
    ("user2","password","user2@yahoo.com"),
    ("user3","password","user3@yahoo.com"),
    ("user4","password","user4@yahoo.com"),
]

if __name__ == '__main__':
    
    try:
        connect = psycopg2.connect(dbname='pythondb',
                                   user= config('USER'),
                                   password= config ('SECRET_KEY'),
                                   host='localhost' )
                
        with connect.cursor() as cursor:
           
            cursor.execute(DROP_TABLE_USERS)        
            cursor.execute(USERS_TABLE )
            
            query = "INSERT INTO users(username, password, email) VALUES(%s, %s, %s)"
            
            #insertar varios usuarios
            for user in users:
                cursor.execute(query, user)            
            connect.commit()   
            
                #ELIMINAR    
            # query= "DELETE FROM users WHERE is = %s " 
            # cursor.execute(query,(3,))
            # connect.commit()
                
                #CONSULTAR
            # query = "SELECT * FROM users"
            # cursor.execute(query)
            # for user in cursor.fetchall():
            #      print(user)
               
            
            
        
    except psycopg2.OperationalError as err:
        
        print('¡¡no fue posible realizar la conexion!!')
        print(err)
        
    finally:    
        
        connect.close()        
        print("Conexion finalizada con exito")