# from dateutil import parser
from datetime import datetime
def change_date_format(dates):
    newDate = []
    for eachDate in dates:
        try:
            date_time_obj = datetime.strptime(eachDate, '%Y%m%d')
        except Exception as e:
            print(e)
            # normalize_date = parser.parse(eachDate).strftime("%Y%m%d")
            newDate.append(eachDate)
    return newDate

dates = change_date_format(["2010/03/30", "15/12/2016", "11-15-2012", "20130720"])
print(*dates, sep='\n')