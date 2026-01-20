# tasks = []

# while True:
#     print("\n--- TO-DO LIST MENU ---")
#     print("1. Add Task")
#     print("2. View Tasks")
#     print("3. Delete Task")
#     print("4. Exit")

#     choice = input("Enter your choice: ")
#     if choice == "1":
#         task = input("Enter task: ")
#         tasks.append(task)
#         print("Task added successfully!")
#     elif choice == "2":
#         if not tasks:
#             print("No tasks available.")
    #     else:
    #         print("\nYour Tasks:")
    #         for i, task in enumerate(tasks, start=1):
    #             print(f"{i}. {task}")

    # elif choice == "3":
    #     if not tasks:
    #         print("No tasks to delete.")
    #     else:
    #         num = int(input("Enter task number to delete: "))
    #         if 1 <= num <= len(tasks):
    #             removed = tasks.pop(num - 1)
    #             print(f"Deleted task: {removed}")
    #         else:
    #             print("Invalid task number.")

    # elif choice == "4":
    #     print("Exiting To-Do List. Goodbye!")
    #     break

    # else:
    #     print("Invalid choice. Try again.")


#> wheather app(api):
import requests

API_KEY = "1eaf068066bbcfa40f7ff6c845bc4df0"
CITY = input("Enter city name: ")

url = f"https://api.openweathermap.org/data/2.5/weather?q={CITY}&appid={API_KEY}&units=metric"

response = requests.get(url)

if response.status_code == 200:
    data = response.json()

    temperature = data["main"]["temp"]
    humidity = data["main"]["humidity"]
    weather = data["weather"][0]["description"]
    wind_speed = data["wind"]["speed"]

    print("\n🌤 Weather Details")
    print("City:", CITY)
    print("Temperature:", temperature, "°C")
    print("Humidity:", humidity, "%")
    print("Condition:", weather)
    print("Wind Speed:", wind_speed, "m/s")
else:
    print("❌ City not found!")
