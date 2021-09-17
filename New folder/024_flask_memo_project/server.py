import datetime
from flask import Flask, redirect, url_for, render_template, session, flash, request
from flask_sqlalchemy import SQLAlchemy
from datetime import timedelta
import calendar
from markupsafe import Markup
from sqlalchemy.inspection import inspect

app = Flask(__name__)
app.secret_key = 'helloworld'
app.permanent_session_lifetime = timedelta(minutes=5)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:password@localhost/db_name'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)


class Memo(db.Model):
    _id = db.Column('id', db.Integer, primary_key=True)
    start_date = db.Column('start_date', db.DateTime)
    stop_date = db.Column('stop_date', db.DateTime)
    start_day = db.Column('start_day', db.DateTime)
    topic = db.Column('topic', db.String(100))
    description = db.Column('description', db.String(100))
    alert_time = db.Column('alert_time', db.DateTime)

    def __init__(self, start_date, stop_date, topic, description, alert_time):
        self.start_date = start_date
        self.stop_date = stop_date
        self.topic = topic
        self.description = description
        self.alert_time = alert_time
        self.start_day = self.start_date.date()

    @property
    def pk(self):
        return self._id

    @property
    def interval(self):
        return self.stop_date - self.start_date

    @property
    def start_time(self):
        return self.start_date.time()

    @property
    def stop_day(self):
        return self.stop_date.date()

    @property
    def stop_time(self):
        return self.stop_date.time()


# class Custom_HTML_Calendar(calendar.HTMLCalendar):
#     cssclass_month_head = "text-centre month-head"
#     cssclass_month = "text-center month"


# main view (month)
@app.route('/')
def month_view():
    # task_list = Memo.query.all()
    # new = Memo(datetime.datetime.now(), datetime.datetime(2021, 5, 10, 14, 0), 'Test memo',
    #            'This is memo description string.', datetime.datetime(2021, 5, 6, 15, 20))
    # db.session.add(new)
    # db.session.commit()
    # # return render_template('month.html')
    # return render_template('test_view.html', task_list=task_list)
    hc = calendar.HTMLCalendar(calendar.MONDAY)
    str = Markup(hc.formatmonth(2021, 5))
    return render_template('month.html', str=str)


# day view
@app.route('/days/<string:date>')
def day_view(date):
    task_list = Memo.query.filter_by(start_day=date).all()
    if len(task_list) == 0:
        return redirect(url_for('day_choose'))
    else:
        # return render_template('day.html', task_list=task_list)
        for task in task_list:
            print(task.pk)
        return render_template('test_view.html', task_list=task_list)


@app.route('/day', methods=['POST', 'GET'])
def day_choose():
    if request.method == "POST":
        year = request.form['year']
        month = request.form['month']
        day = request.form['day']
        date = f"{year}-{month}-{day}"
        # print(f"/day/{year}-{month}-{day}")
        return redirect(url_for('day_view', date=date))
    else:
        return render_template('day.html')


# memo edit
@app.route('/edit/<var>', methods=['POST', 'GET'])
def edit_memo(var):
    # if request.method == "POST":
    #     data = Memo.query.filter_by(pk=var).first()
    #     memo = [data.start_date, data.stop_date, data.start_day, data.topic, data.description, data.alert_time]
    #     return render_template('edit.html', memo=data)
    data = Memo.query.get(var)
    memo = [data.start_date, data.stop_date, data.start_day, data.topic, data.description, data.alert_time]
    data.start_date = datetime.datetime.now()
    db.session.commit()
    return render_template('test2.html', memo=memo)


# For testing
@app.route('/test1')
def test1():
    test_date = Memo(datetime.datetime.now(), datetime.datetime(2021, 5, 7, 8, 15),
                     'Test Memo', 'Short description', datetime.datetime(2021, 5, 7, 20))
    return render_template('test1.html', var=test_date)


@app.route('/test2/<var>/')
def test2(var):
    return render_template('test2.html', var=var)


@app.route('/filldb')
def filldb():
    pool = [('Test1', 'Test1 content', datetime.datetime(2021, 5, 15, 2), datetime.datetime(2021, 5, 14, 12)),
            ('Test2', 'Test2 content', datetime.datetime(2021, 5, 30, 7), datetime.datetime(2021, 5, 29, 23)),
            ('Test3', 'Test3 content', datetime.datetime(2021, 5, 8, 10), datetime.datetime(2021, 5, 8, 8)),
            ('Test4', 'Test4 content', datetime.datetime(2021, 5, 12, 12), datetime.datetime(2021, 5, 12, 8)),
            ('Test5', 'Test5 content', datetime.datetime(2021, 5, 16, 15), datetime.datetime(2021, 5, 16, 10))
            ]
    for topic, description, stop_date, alert_time in pool:
        new = Memo(datetime.datetime.now(), stop_date, topic,
                    description, alert_time)
        db.session.add(new)
        db.session.commit()
    return 'All done'


if __name__ == '__main__':
    db.create_all()
    app.run(debug=True)