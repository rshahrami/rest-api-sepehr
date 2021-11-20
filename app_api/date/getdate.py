from datetime import datetime
import pytz



def get_date_zone():
    datetime_NY = datetime.now(pytz.timezone('utc')).strftime("%Y-%m-%dT%H:%M:%SZ")
    return datetime_NY