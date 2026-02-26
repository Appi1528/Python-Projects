def task():
    tasks = [] #empty list
    print("Welcome to the To-Do List App!")

    total_tasks = int(input("Enter the number of tasks you want to add: "))
    for i in range(total_tasks):
        task_name = input(f"Enter task{i} = ")
        tasks.append(task_name)


    print(f"Today's tasks are\n{tasks}")


    while True:
        operation = int(input("Enter 1-Add \n2-Update \n3-Delete \n4-View \n5-Exit\n"))
        if operation == 1:
            add = input("Enter the task you want to add = ")
            tasks.append(add)
            print(f"Task {add} Has been added successfully!!")

        elif operation ==2:
            update = input("Enter the task name you want to update  = ")
            if update in tasks:
                new_task = input("Enter the New tasks =")
                index = tasks.index(update)
                tasks[index] = new_task
                print(f"Task {update} has been updated to {new_task} successfully!!")


        elif operation == 3:
            delete = input("Enter the task you want to delete = ")
            if delete in tasks:
                tasks.remove(delete)
                print(f"Task {delete} has been deleted successfully!!")
            else:
                print(f"Task {delete} not found in the list.")

        elif operation == 4:
            print(f"Your current tasks are: {tasks}")

        elif operation == 5:
            print("Closing the To-Do List App...")
            break

task() 