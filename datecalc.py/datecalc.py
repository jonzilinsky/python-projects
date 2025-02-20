import datetime

today = datetime.datetime.now()

month = input("What month did you start? ").strip().lower()


if month.isdigit():
    month = int(month)
else:
    if month.startswith('jan'): 
        month = 1
    elif month.startswith('feb'):
        month = 2
    elif month.startswith('mar'):
        month = 3
    elif month.startswith('apr'):
        month = 4
    elif month.startswith('may'):
        month = 5
    elif month.startswith('jun'):
        month = 6
    elif month.startswith('jul'):
        month = 7
    elif month.startswith('aug'):
        month = 8
    elif month.startswith('sep'):
        month = 9
    elif month.startswith('oct'):
        month = 10
    elif month.startswith('nov'):
        month = 11
    elif month.startswith('dec'):
        month =12 

day = int(input("What day did you start? "))
askyear = input("Of this year? y/n ")
if askyear.startswith('y'):
    year = datetime.datetime.now().year 
elif askyear == "":
    year = datetime.datetime.now().year
else:
   year = int(input("What year did you start? "))

start = datetime.datetime(year, month, day)

timedif = today - start
dayssince = timedif.days
weekssince = round((dayssince / 7), 2) 
monthssince = round((dayssince / 30.5), 2) 
yearssince = round((monthssince / 12), 2)

print(f"\nDays since start: ",dayssince)
print(f"Weeks since start: ", weekssince)
print(f"Months since start: ", monthssince)
if yearssince > 1 :
    print("Years since start: ", yearssince)
