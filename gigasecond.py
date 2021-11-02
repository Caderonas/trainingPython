import datetime
def gigasecond():
	year = int(input('Enter a year '))
	month = int(input('Enter a month '))
	day = int(input('Enter a day '))

	today = datetime.datetime.now()
	d = datetime.datetime(year, month, day)

	timedelta = today - d
	gigaseconds = timedelta.total_seconds()/(10**9)
	return gigaseconds