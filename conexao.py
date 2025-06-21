import psycopg2
 
host = "localhost"
bdbane = "fundo-remove"
user = "postgres"
password = "Z9ytte@1821"
sslmode = "disable"

conn_string = 'host={0} dbname={1} user={2} password={3} sslmode={4}'.format(host, bdbane, user, password, sslmode)

def conectar():
    return psycopg2.connect(conn_string)
    
