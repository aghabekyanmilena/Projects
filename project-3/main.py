import time

def f_time(seconds):
    hours = seconds // 3600
    minutes = (seconds % 3600) // 60
    seconds = seconds % 60
    return f"{hours:02d}:{minutes:02d}:{seconds:02d}"

def count(seconds):
    while seconds > 0:
        print(f"Time remaining: {f_time(seconds)}")
        time.sleep(1)
        seconds -= 1
    print("Time's up!")

def get_input():
    while True:
        try:
            time_str = input("Enter the time to countdown (h:m:s): ")
            hours, minutes, seconds = map(int, time_str.split(':'))
            total_seconds = hours * 3600 + minutes * 60 + seconds
            return total_seconds
        except ValueError:
            print("Invalid input. Please enter the time in the format 'h:m:s'.")

def main():
    seconds = get_input()
    count(seconds)

if __name__ == "__main__":
    main()