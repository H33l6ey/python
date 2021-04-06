command = ""
status = "stopped"

while command.lower() != "quit":

    # Start
    command = input("> ").lower()
    if command.lower() == "start":
        if status == "stopped":
            print("Car started...")
            status = "started"
        else:
            print("casr is already started!")


    elif command.lower() == "stop": # user asked to stop
        if status == "started":
            print("Car stopped..")
            status = "stopped"
        else:
            print("car is already stopped")


    elif command == "help":
        print("""
        start - to start the car
        stop - to stop the car
        quit - to quit
        """)
    else:
        print("i dont understand that")