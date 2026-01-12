#Create menu
#Create add_task function
#Create vew_task function
#Create mark as completed function
#Create delelte function
#file handling
#Error handling
#1. coding
#2. walkout
#3. Sleep

FILENAME = "tasks.txt"
def add_task(task):
    try:
        with open(FILENAME, "r", encoding="utf-8") as file:
            lines = file.readlines()
            if lines:
                last_line = lines[-1]
                number = int(last_line.split(". ")[0])
                i = number + 1
            else:
                i = 1
    except FileNotFoundError:
        i = 1
    with open(FILENAME, "a", encoding="utf-8") as task_file:
        task_file.write(f"{i}. {task} \n")
    print(f"{task} added successfully")


def view_task():
    try:
        with open(FILENAME, "r", encoding="utf-8") as file:
            task = file.readlines()
            if task:
                for line in task:
                    print(line)
            else:
                print("No task found")
    except FileNotFoundError:
        print("File Not Found")


def mark_task():
    
    task = input("Task to be marked ").strip().lower()
    updated_line = []
    try:
        with open(FILENAME, "r", encoding="utf-8") as file:
            found = False
            lines = file.readlines()
            for line in lines:
                line = line.strip()
                number, task_name = line.split(". ", 1)
                if task_name.lower() == task:
                    found = True
                    updated_line.append(f"{number}. {task_name} ✅\n")
                else:
                    updated_line.append(line+"\n")
            if found:
                with open(FILENAME, "w", encoding="utf-8") as updated_file:
                    updated_file.writelines(updated_line)
                    print(f"{task} marked as completed")
            else:
                print(f"{task} NOT FOUND")
    except FileNotFoundError:
        print("File not found")
            


        

def delete_task():
    tobeDeleted = input("Enter the task name or the number ")
    found = False
    updated_line = []
    try:
        with open(FILENAME, "r", encoding="utf-8") as file:
            lines = file.readlines()
            for line in lines:
                number, task_name = line.split(". ", 1)
                if(
                    (tobeDeleted.isdigit() and int(tobeDeleted) == int(number) )
                   or tobeDeleted.lower() == task_name.strip().lower()
                   ):
                    found = True
                    print(f"{task_name} has been deleted")
                    continue
                else:
                    updated_line.append(line)
        if found:
            with open(FILENAME, "w", encoding="utf-8") as updated_file:
                updated_file.writelines(updated_line)
        else:
            print(f"{tobeDeleted} not found ")
            if tobeDeleted.isalpha():
                answer = input(f"Hit 1 to add {tobeDeleted} to the task file")
                if answer == "1":
                    add_task(tobeDeleted)
    except FileNotFoundError:
        print("No file found")        




def show_menu():
    print("-------- TODO LIST ------------")
    print("1. Add task ")
    print("2. view tasks ")
    print("3. mark task as completed ")
    print("4. delete task ")
    print("5. exit ")

if __name__ == '__main__':
    while True:
        show_menu()
        choice = input("Enter Your choice ")
        if choice == "1":
            task = input("Task: ")
            add_task(task)
        elif choice == "2":
            view_task()
        elif choice == "3":
            mark_task()
        elif choice == "4":
            delete_task()
        elif choice == "5":
            exit()
        else:
            print("invalid input")
        
