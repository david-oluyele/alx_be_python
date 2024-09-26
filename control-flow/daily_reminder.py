#Prompt user for a single task
task = input("Enter a task description: ")
priority = input("What is the priority level? (high/medium/low): ").lower()
time_bound = input("Is the task time-bound? (yes/no): " ).lower()

#Use match case to handle priority level
match priority:
    case 'high':
        reminder = f"{task} is a high priority task"
    case 'medium':
        reminder = f"{task} is a medium priority task"
    case 'low':
        reminder = f"{task} is a low priority task"
    case _:
        reminder = "Invalid priority level."

#Use if statement to check if task is time bound
if time_bound == "yes":
    reminder = f"{reminder} that requires immediate attention today."
elif time_bound == "no":
    reminder = f"{reminder} consider completing it when you have free time."
else:
    reminder = "Time sensitivity not specified correctly."

#Customized Output
print(f"Reminder: {reminder}")

