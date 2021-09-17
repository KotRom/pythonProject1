import mysql.connector
from datetime import datetime
from datetime import date

#TODO:Create a function that displays current month in a calendar view
def show_month(month, year):
    print('You are in month view:', month, year)
    # TODO: create a view for current month / year
    # TODO: realize show previous month / next
    # TODO: go to day view
    date=input("Enter a day")
    #TODO: Make error handling
    show_day(date)
    pass

#TODO:Create a function that displays current day view
def show_day(date):
    #TODO: Start default view
    while True:
        #TODO: Check that "Create event button is pressed"
        #if button Create pressed then call create event procedure
        #TODO: Display events
        #TODO: Check if button edit pressed for some event
        #TODO: Check if button delete pressed for some event
        event1 = [1,"Title 1", "Description 1",'05-05-2021','21:30','22:00','21:15','planned']
        event2 = [2, "Title 2", "Description 2", '05-05-2021', '20:00', '21:00', '19:30', 'planned']
        events = [event1, event2]
    pass

#TODO:Create a view that shows event
def view_event(id):
    #TODO: create view for certain event (start_time, date_time, alarm_time)
    #TODO: if Button save pressed then
    pass

#TODO:Create a function that creates event
def create_event(date):
    view_event(date)
    while True:
        # TODO: if button save pressed then call insert SQL script
        # TODO: use INSERT INTO organizer.table SET [parameters] WHERE event_id = [event_id]
        pass
    pass

#TODO:Create a function that edits event
def edit_event(event_id):
    #TODO: use UPDATE organizer.table SET [parameters] WHERE event_id = [event_id]
    pass

#TODO:Create a function that gets all events from certain date
def get_events(date):
    pass

#TODO:Create a function that deletes event
def delete_event(event_id):
    pass

def main(user):
    host = '127.0.0.1'
    port = '3308'
    user = 'root'
    password = '1234'
    db = 'organizer'
    config = {
        'user': "" + user + "",
        'password': "" + password + "",
        'host': "" + host + "",
        'port': "" + port + "",
        'database': "" + db + "",
        # 'auth_plugin': "" + auth + "",
        'raise_on_warnings': True,
    }
    link = mysql.connector.connect(**config)
    cursor = link.cursor(buffered=True)
    if link.is_connected():
        print("MySQL conection alive")
    else:
        print("MySQL connection failed")
    # TODO: Start the default interface (calendar view)
    current_date=date.today()
    current_month=datetime.now().month
    current_year = datetime.now().year
    print("Hello,", user, current_date, current_month, current_year)
    show_month(current_month, current_year)
    pass




# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main("Default user")


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
