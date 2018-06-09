from flask import Flask, request
from flask import render_template
from flask import redirect
from flask_sqlalchemy import SQLAlchemy
import utilities.log_utility as utilities

logger = utilities.setup_custom_logger(__name__)
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
db = SQLAlchemy(app)


class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.Text)
    done = db.Column(db.Boolean, default=False)

    def __init__(self, content):
        self.content = content
        self.done = False

    def __repr__(self):
        return '<Content %s>' % self.content


db.drop_all()
db.create_all()


@app.route('/')
def tasks_list():
    tasks = Task.query.all()
    logger.info("tasks list: " + str(tasks))
    logger.info("going to display html template")
    return render_template('list.html', tasks=tasks)


@app.route('/task', methods=['POST'])
def add_task():
    try:
        content = request.form['content']
        task = Task(content)
        logger.info("going to add new task to db. task info: " + str(task))
        db.session.add(task)
        db.session.commit()
        logger.info("task was added successfully")
    except Exception as e:
        logger.error("failed to add new task to db. error info: " + str(e))
    return redirect('/')


@app.route('/delete/<int:task_id>')
def delete_task(task_id):
    try:
        task = Task.query.get(task_id)
        logger.info("going to delete task from db. task info: " + str(task))
        db.session.delete(task)
        db.session.commit()
        logger.info("task was deleted successfully")
    except Exception as e:
        logger.error("failed to delete task from db. error info: " + str(e))
    return redirect('/')


@app.route('/done/<int:task_id>')
def resolve_task(task_id):
    try:
        task = Task.query.get(task_id)

        if task.done:
            task.done = False
            logger.info("going to mark task as undone in db. task info: " + str(task))
        else:
            logger.info("going to mark task as done in db. task info: " + str(task))
            task.done = True

        db.session.commit()
        logger.info("task was marked successfully")
    except Exception as e:
        logger.error("failed to mark task in db. error info: " + str(e))
    return redirect('/')


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5050)