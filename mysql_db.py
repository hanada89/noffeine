import pymysql

HOST = '127.0.0.1'
USER = 'root'
PSWD = 'hana1217'
DB = 'noffeine'


## DB Connection
def connect_db():
    try:
        conn = pymysql.connect(
            host = HOST,
            user = USER,
            passwd = PSWD,
            db = DB,
            port = 3306,
            charset='utf8'
        )
    except pymysql.err.OperationalError:
        conn = pymysql.connect(
            host = HOST,
            user = USER,
            passwd = PSWD,
            port = 3306,
            charset='utf8'
        )
        
    cur = conn.cursor(pymysql.cursors.DictCursor)
    return conn, cur


conn, cur = connect_db()



## Query Execute
def query(sql):
    cur.execute(sql)
    return cur.fetchall()
    
    
## Create DB
def create_db(db_name):
    ret = query('SHOW DATABASES')
    print(f'Before DB: {ret}')
    
    try:
        query(f'CREATE DATABASE {db_name}')
        
        ret = query('SHOW DATABASES')
        print(f'After DB: {ret}')
    except pymysql.err.ProgrammingError:
        print(f'EXISTS DB: {db_name}')
        pass
    
    
    
## Create Table
def create_table(db_name):
    query(f'USE {db_name}')
    
    ret = query('SHOW TABLES')
    print(f'Before Table: {ret}')
    
    sql = 'CREATE TABLE test_store_info( \
            store_no INT UNSIGNED NOT NULL AUTO_INCREMENT, \
            store_name_kor VARCHAR(100) NOT NULL, \
            store_name_eng VARCHAR(100) NOT NULL, \
            store_tel VARCHAR(15) NOT NULL, \
            is_pet TINYINT NOT NULL, \
            opening_time VARCHAR(11), \
            store_sns TEXT,\
            reg_dtime DATETIME DEFAULT CURRENT_TIMESTAMP,\
            mod_dtime DATETIME DEFAULT CURRENT_TIMESTAMP,\
            PRIMARY KEY(store_no) \
        )'
    query(sql)

    ret = query('SHOW TABLES')
    print(f'After Table: {ret}')
        
        
    
    
    
if __name__ == '__main__':
    db_name = 'test'
    db_name = DB
    create_db(db_name)
    create_table(db_name)