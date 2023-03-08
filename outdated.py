#input in MM-DD-YYYY

months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]

#date checker
# while True:
#     try:
#         date = input("Date: ")

#     except:

def check_day(date):
    if 1 < int(date) < 31:
        # print("true")
        return True

def check_month(month):
    if month.title() in months:
    # print("true")
        return True

def check_month_text(month):
    if 1 < int(month) < 12:
    # print("TRUE")
        return True
    
def check_year(year):
    if year.isnumeric():
        return True

def check_date_text():
    month, date, year = n.split(" ")
    date_clean = date.strip(",")
    check_day(date_clean)
    check_month_text(month)
    check_year(year)
    print(year + "-" + month + "-" + date_clean)

def check_date():
    date = input("Date: ")
    month, date, year = date.split("/")
    if check_date(date):
        return True
    if check_month(month):
        return True
    if check_year(year):
        return True
    print(year + "-" + month + "-" + date)

    # if 1 < int(month) < 12 and 1 < int(date) < 30:
    #     print("True")
    # elif if month in months and 

check_date()

# check_date_text("8 September, 2020")


# date = input("Date: ")
# check_date_text(date)

# check_date(date)
#if not in format then ask user again

#output in  YYYY-MM-DD