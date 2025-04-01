import datetime
import time

def display_current_datetime():
    return datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

def calculate_date_difference(date1,date2):
    d1=datetime.datetime.strptime(date1, "%Y-%m-%d")
    d2=datetime.datetime.strptime(date2, "%Y-%m-%d")
    return (d2-d1).days

def format_date(date,format_str="%d-%m-%Y"):
    return datetime.datetime.strptime(date, "%Y-%m-%d").strftime(format_str)

def stopwatch():
    print("Press enter to start the stopwatch. Press Ctrl+C to stop.")
    input()
    start_time=time.time()
    try:
        while True:
            elasped =time.time()-start_time
            print(f"Elasped time:{elasped: .2f} sec")
            time.sleep(1)
    except KeyboardInterrupt:
        print(f"\nStopwatch stopped. Elasped time: {elasped:.2f} sec")


def countdown_time(seconds):
    while seconds:
        print(f"TIme left: {seconds} sec")
        time.sleep(1)
        seconds-=1
    print("Time's up!")