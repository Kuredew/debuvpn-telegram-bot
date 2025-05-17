import datetime

def get_date_after(day):
    date = datetime.datetime.now() + datetime.timedelta(30)
    return date.strftime('%d %b %Y')