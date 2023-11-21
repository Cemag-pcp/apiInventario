from flask import Flask, jsonify
import psycopg2

DB_HOST = "database-2.cdcogkfzajf0.us-east-1.rds.amazonaws.com"
DB_NAME = "postgres"
DB_USER = "postgres"
DB_PASS = "15512332"

conn = psycopg2.connect(dbname=DB_NAME, user=DB_USER,
                        password=DB_PASS, host=DB_HOST)

app = Flask(__name__)

@app.route('/api/publica/inventario/registros', methods=['GET'])
def get_registros():
    cursor = conn.cursor()
    cursor.execute('SELECT familia,codigo,descricao,sum(contagem) as contagem_agrupada FROM inventario.registros GROUP BY familia,codigo,descricao')
    registros = cursor.fetchall()
    cursor.close()
    
    return jsonify(registros)

if __name__ == '__main__':
    app.run(debug=True)