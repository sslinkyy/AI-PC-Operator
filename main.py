from supervisor import Supervisor

if __name__ == "__main__":
    supervisor = Supervisor()

    while True:
        user_command = input("Enter a command: ")
        if user_command.lower() in ["exit", "quit"]:
            break
        response = supervisor.delegate_task(user_command)
        print(response)
