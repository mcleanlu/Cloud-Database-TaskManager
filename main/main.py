import firebase_admin
from firebase_admin import credentials, firestore, auth
import datetime
import getpass

cred = credentials.Certificate("firebase_key/fir-database-taskmanager-firebase-adminsdk-4dkme-e0116745a6.json")
firebase_admin.initialize_app(cred)

db = firestore.client()

def create_task():
    name = input("Enter task name: ")
    description = input("Enter task description: ")
    due_date = input("Enter task due date (yyyy-mm-dd): ")
    due_date = datetime.datetime.strptime(due_date, "%Y-%m-%d")
    priority = input("Enter task priority: ")
    complete = False

    task = {
        u'name': name,
        u'description': description,
        u'due_date': due_date,
        u'priority': priority,
        u'complete': complete
    }

    db.collection(u'tasks').add(task)
    print("Task added.")

def get_all_tasks():
    tasks = db.collection(u'tasks').stream()
    task_list = []
    for task in tasks:
        task_list.append(task.id)
        task_data = task.to_dict()
        print(f"Task ID: {task.id}\n"
              f"Task: {task_data['name']}\n"
              f"Description: {task_data['description']}\n"
              f"Due Date: {task_data['due_date'].strftime('%Y-%m-%d')}\n"
              f"Priority: {task_data['priority']}\n"
              f"Completed: {task_data['complete']}\n"
              "------------------------------------")
    return task_list

def get_single_task(task_id):
    task_ref = db.collection(u'tasks').document(task_id)
    task = task_ref.get()
    if task.exists:
        task_data = task.to_dict()
        print(f"Task ID: {task_id}\n"
              f"Task: {task_data['name']}\n"
              f"Description: {task_data['description']}\n"
              f"Due Date: {task_data['due_date'].strftime('%Y-%m-%d')}\n"
              f"Priority: {task_data['priority']}\n"
              f"Completed: {task_data['complete']}\n"
              "------------------------------------")
    else:
        print(f"No such task with ID {task_id} exists.")

def update_task(task_id, description):
    task_ref = db.collection(u'tasks').document(task_id)
    task_ref.update({u'description': description})
    print("Task updated.")

def mark_complete(task_id):
    task_ref = db.collection(u'tasks').document(task_id)
    task_ref.update({u'complete': True})
    print("Task marked as complete.")

def delete_task(task_id):
    db.collection(u'tasks').document(task_id).delete()
    print("Task deleted.")

def main_menu():
    print("""
    1. Create a task
    2. Update a task
    3. Retrieve all tasks
    4. Retrieve a single task
    5. Mark a task as complete
    6. Delete a task
    7. Exit
    """)

    option = input("Select an option: ")

    if option == "1":
        create_task()
    elif option == "2":
        task_id = input("Enter task ID to update: ")
        description = input("Enter new description: ")
        update_task(task_id, description)
    elif option == "3":
        get_all_tasks()
    elif option == "4":
        task_id = input("Enter task ID to retrieve: ")
        get_single_task(task_id)
    elif option == "5":
        task_id = input("Enter task ID to mark as complete: ")
        mark_complete(task_id)
    elif option == "6":
        task_id = input("Enter task ID to delete: ")
        delete_task(task_id)
    elif option == "7":
        exit()
    else:
        print("Invalid option. Please try again.")
        main_menu()

if __name__ == "__main__":
    main_menu()
