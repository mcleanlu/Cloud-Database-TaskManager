import firebase_admin
from firebase_admin import credentials, firestore, auth

# Initialize Firebase
cred = credentials.Certificate('firebase_key/fir-database-taskmanager-firebase-adminsdk-4dkme-e0116745a6.json')
firebase_admin.initialize_app(cred)
db = firestore.client()

# Sign in with email and password
user_email = 'lucas.w.mclean@gmail.com'  # Replace with real user email
user_password = 'password1'  # Replace with real user password
user = auth.get_user_by_email(user_email)
user_uid = user.uid
print(f'User ID token: {user_uid}')


# Function to create a task
def create_task(user_uid, name, description, due_date, priority):
    task_data = {
        'name': name,
        'description': description,
        'due_date': due_date,
        'priority': priority,
        'complete': False  # New field
    }
    task_ref = db.collection('users').document(user_uid).collection('tasks').document()
    task_ref.set(task_data)
    print(f'Task {task_ref.id} created.')
    return task_ref.id


# Function to update a task
def update_task(user_uid, task_id, description):
    task_ref = db.collection('users').document(user_uid).collection('tasks').document(task_id)
    task_ref.update({'description': description})
    print(f'Task {task_id} updated.')


# Function to retrieve a task
def retrieve_task(user_uid, task_id):
    task_ref = db.collection('users').document(user_uid).collection('tasks').document(task_id)
    task = task_ref.get()
    if task.exists:
        print(f'Task {task_id}: {task.to_dict()}')
    else:
        print(f'Task {task_id} does not exist.')


# Function to delete a task
def delete_task(user_uid, task_id):
    task_ref = db.collection('users').document(user_uid).collection('tasks').document(task_id)
    task_ref.delete()
    print(f'Task {task_id} deleted.')


# New Function to mark a task as complete
def mark_task_as_complete(user_uid, task_id):
    task_ref = db.collection('users').document(user_uid).collection('tasks').document(task_id)
    task_ref.update({'complete': True})
    print(f'Task {task_id} has been marked as complete.')


# Test the functions
# task_id = create_task(user_uid, 'Task 1', 'Description 1', '2023-07-15', 'High')
# update_task(user_uid, task_id, 'Updated Description')
# retrieve_task(user_uid, task_id)
# mark_task_as_complete(user_uid, task_id)
# delete_task(user_uid, task_id)

