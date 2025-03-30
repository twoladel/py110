'''
The function is supposed to return True if a date has events scheduled
and False if not.

You just need to flip False and True in the function. Which I did, but then
refactored again into a one liner Returning date not in events will return 
True if the date is available and False if something is already scheduled.
'''


events = {
    "2023-08-13": ["Python debugging exercises"],
    "2023-08-14": ["Read 'Automate the Boring Stuff'"],
    "2023-08-15": ["Webinar: Python for Data Science"],
}

def is_date_available(date):
    return date not in events


print(is_date_available("2023-08-14"))  # should return False
print(is_date_available("2023-08-16"))  # should return True