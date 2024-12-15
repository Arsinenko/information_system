import random
import requests

# Функция для генерации случайных имен
def generate_random_name():
    first_names = ["John", "Jane", "Alice", "Bob", "Charlie", "David", "Eva", "Frank", "Grace", "Hannah"]
    middle_names = ["A.", "B.", "C.", "D.", "E.", "F.", "G.", "H.", "I.", "J."]
    last_names = ["Smith", "Johnson", "Williams", "Jones", "Brown", "Davis", "Miller", "Wilson", "Moore", "Taylor"]
    
    first_name = random.choice(first_names)
    middle_name = random.choice(middle_names)
    last_name = random.choice(last_names)
    
    return first_name, middle_name, last_name

# URL вашего API
base_url = "http://localhost:8000/api/v1"

# Создание групп
groups = [
    {"group_name": "Group A", "size": 5},
    {"group_name": "Group B", "size": 5},
    {"group_name": "Group C", "size": 5}
]

# Отправка запросов на создание групп
for group in groups:
    response = requests.post(f"{base_url}/create_group", json=group)
    print(response.json())

# Создание студентов
students = []
for i in range(15):
    first_name, middle_name, last_name = generate_random_name()
    group_id = random.randint(2, 4)  # Предполагаем, что ID групп от 1 до 3
    student = {
        "first_name": first_name,
        "middle_name": middle_name,
        "last_name": last_name,
        "group_id": group_id
    }
    students.append(student)

# Отправка запросов на создание студентов
for student in students:
    response = requests.post(f"{base_url}/create_user", json=student)
    print(response.json())