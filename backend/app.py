from flask import Flask, request, jsonify
import psycopg2
import redis
import os
from config import Config

app = Flask(__name__)
r = redis.Redis(host=os.getenv('REDIS_HOST', 'redis'), port=6379, decode_responses=True)

def get_db_connection():
    conn = psycopg2.connect(
        host=Config.DB_HOST,
        database=Config.DB_NAME,
        user=Config.DB_USER,
        password=Config.DB_PASSWORD
    )
    return conn

@app.route('/api/tasks', methods=['GET', 'POST'])
def tasks():
    conn = get_db_connection()
    cur = conn.cursor()

    if request.method == 'POST':
        task = request.json['task']
        cur.execute('INSERT INTO tasks (task) VALUES (%s)', (task,))
        conn.commit()
        r.delete('tasks_cache')
        cur.close()
        conn.close()
        return jsonify({'message': 'Task added!'}), 201

    if request.method == 'GET':
        tasks = r.get('tasks_cache')
        if tasks:
            return jsonify(eval(tasks))
        cur.execute('SELECT id, task FROM tasks')
        tasks = cur.fetchall()
        r.set('tasks_cache', str(tasks)) 
        cur.close()
        conn.close()
        return jsonify(tasks)

@app.route('/api/tasks/<int:id>', methods=['DELETE'])
def delete_task(id):
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('DELETE FROM tasks WHERE id = %s', (id,))
    conn.commit()
    r.delete('tasks_cache')  
    cur.close()
    conn.close()
    return jsonify({'message': 'Task deleted!'})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
