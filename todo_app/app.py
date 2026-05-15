from flask import Flask, render_template, request, redirect
from datetime import datetime

app = Flask(__name__)

tasks = [
    {'text': 'Купить хлеб', 'date': datetime.now().strftime('%Y-%m-%d %H:%M')},
    {'text': 'Сделать уроки', 'date': datetime.now().strftime('%Y-%m-%d %H:%M')},
    {'text': 'Позвонить другу', 'date': datetime.now().strftime('%Y-%m-%d %H:%M')}
]

@app.route('/')
def index():
    return render_template('index.html', tasks=tasks)

@app.route('/add', methods=['POST'])
def add_task():
    new_task = request.form['task']
    if new_task:
        tasks.append({
            'text': new_task,
            'date': datetime.now().strftime('%Y-%m-%d %H:%M')
        })
    return redirect('/')

@app.route('/clear', methods=['POST'])
def clear_all():
    tasks.clear()
    return redirect('/')

@app.route('/delete/<int:task_id>')
def delete_task(task_id):
    if 0 <= task_id < len(tasks):
        tasks.pop(task_id)
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)