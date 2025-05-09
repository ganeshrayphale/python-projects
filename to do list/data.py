
import pandas as pd


def showtask(date):
    # tasks show karat hey
    try:
        data = pd.read_csv("to_do_list.csv")  # csv file read karta hey
    except FileNotFoundError:
        print("No task file found yet.")
        return
    

    if date in data['date'].values:  # date ke vaules ki array mey date ko check karta hey
        print(f"Tasks on {date}:")
        print(data[data['date'] == date])
    else:
        print(f"No tasks found for {date}.")

def addtasks(date):
    # Add tasks for a specific date
    while True:
        task = input("Enter the task (type 'STOP' to finish): ")
        if task.strip().upper() == "STOP":
            break
        else:
            new_row = pd.DataFrame([[date, task]], columns=['date', 'Task']) # new row tyar karke add karat hey usme

       

    print("All tasks added successfully.")


date = input("Enter the date in format DD-MM-YYYY: ") # date input letta hey

showtask(date)

check = input("Want to add a task? Enter ADD or NO: ")

if check.strip().upper() == "ADD":
    addtasks(date)
elif check.strip().upper() == "NO":
    print("Thanks! Visit again.")
else:
    print("Invalid input.")
