from flask import Flask, render_template, request, redirect

app = Flask(__name__)

students = []

@app.route('/')
def home():
    return render_template('index.html', students=students)

@app.route('/add', methods=['POST'])
def add_student():
    name = request.form['name']
    students.append(name)
    return redirect('/')

@app.route('/delete/<name>')
def delete_student(name):
    students.remove(name)
    return redirect('/')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
