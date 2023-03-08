
def main():
    time = input("What time is it? ##:##")
    if 7 <= convert(time) <= 8:
        print("breakfast time")
    elif 12 <= convert(time) <= 13:
        print("lunch time")
    elif 18 <= convert(time) <= 19:
        print("dinner time")
    else:
        print(" ")

def convert(time):
    hours, minutes_meridiem = time.split(":")
    minutes, meridiem = minutes_meridiem.split(" ")
    if meridiem == "p.m.":
        hours = int(hours) + 12 
    decimal_minutes = int(minutes)/60
    return float(hours) + float(decimal_minutes) 

if __name__ == "__main__":
    main()

