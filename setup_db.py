from config import db_config
import pymysql

conn = pymysql.connect(
    host=db_config['host'],
    user=db_config['user'],
    password=db_config['password']
)
cur = conn.cursor()
cur.execute('CREATE DATABASE IF NOT EXISTS sneha_db')
cur.execute('USE sneha_db')
cur.execute('''CREATE TABLE IF NOT EXISTS users (
  id INT AUTO_INCREMENT PRIMARY KEY,
  name VARCHAR(100),
  email VARCHAR(100)
)''')
conn.commit()
print('Done!')
