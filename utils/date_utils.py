import datetime

def get_date_after(day):
    date = datetime.datetime.now() + datetime.timedelta(day)
    return date.strftime('%d %b %Y')