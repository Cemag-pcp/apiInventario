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
    
    """
    API para visualizar os resultados agrupados por codigo, descricao, familia e origem.
    """
    
    cursor = conn.cursor()
    cursor.execute("""
                    SELECT T1.familia,T1.codigo,T1.descricao,origem,curva_abc,sum(contagem) as contagem_agrupada,sum(recontagem)
                    FROM inventario.registros AS T1
                    JOIN inventario.base_inventario_2023 AS T2 ON T1.codigo = T2.codigo
                    GROUP BY T1.familia,T1.codigo,T1.descricao,origem,curva_abc
                   """)
    
    registros = cursor.fetchall()
    cursor.close()
    
    return jsonify(registros)

if __name__ == '__main__':
    app.run(debug=True)