def main():
    tasks = []

    while True:
        control = input("Type 1 for show tasks, 0 for add new task, other to end: ")

        if control == "1":
            for task in tasks:
                print(f'{task} \n')
        elif control == "0":
            new_task = input("Write new task: ")
            tasks.append(new_task)
        else:
            break


if __name__=="__main__":
    main()