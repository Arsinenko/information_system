# import random
# import requests

# # Функция для генерации случайных имен
# def generate_random_name():
#     first_names = ["John", "Jane", "Alice", "Bob", "Charlie", "David", "Eva", "Frank", "Grace", "Hannah"]
#     middle_names = ["A.", "B.", "C.", "D.", "E.", "F.", "G.", "H.", "I.", "J."]
#     last_names = ["Smith", "Johnson", "Williams", "Jones", "Brown", "Davis", "Miller", "Wilson", "Moore", "Taylor"]
    
#     first_name = random.choice(first_names)
#     middle_name = random.choice(middle_names)
#     last_name = random.choice(last_names)
    
#     return first_name, middle_name, last_name

# # URL вашего API
# base_url = "http://localhost:8000/api/v1"

# # Cleanup function to reset the database state
# def cleanup_groups():
#     # This should delete all groups; adjust as necessary
#     response = requests.delete(f"{base_url}/delete_group", json={"id": 1})  # Adjust to delete all groups
#     print(response.json())

# # Test case for creating multiple groups
# def test_create_multiple_groups():
#     cleanup_groups()  # Reset the database state
#     groups = [
#         {"group_name": "Group A", "size": 5},
#         {"group_name": "Group B", "size": 5},
#         {"group_name": "Group C", "size": 5}
#     ]
#     response = requests.post(f"{base_url}/create_groups", json={"groups": groups})
#     print(response.json())
#     assert response.status_code == 200
#     assert response.json()["message"] == "Success. Groups were created"

# # Test case for creating duplicate groups
# def test_create_duplicate_groups():
#     cleanup_groups()  # Reset the database state
#     groups = [
#         {"group_name": "Group A", "size": 5},
#         {"group_name": "Group A", "size": 5}  # Duplicate group name
#     ]
#     response = requests.post(f"{base_url}/create_groups", json={"groups": groups})
#     print(response.json())
#     assert response.status_code == 400
#     assert "Group 'Group A' already exists." in response.json()["message"]

# # Run tests
# if __name__ == "__main__":
#     test_create_multiple_groups()
#     test_create_duplicate_groups()
import requests

headers = {
    'Content-Type': 'application/json',
}

json_data = {
    'groups': [
        {
            'group_name': 'group2',
            'size': 0,
        },
        {
            'group_name': 'group3',
            'size': 0,
        },
        {
            'group_name': 'group4',
            'size': 0,
        },
    ],
}

response = requests.post('http://localhost:8000/api/v1/create_groups', headers=headers, json=json_data)
print(response.content)

# Note: json_data will not be serialized by requests
# exactly as it was in the original request.
#data = '{\n  "groups": [\n    {\n      "group_name": "group2",\n      "size": 0\n    },\n    {\n      "group_name": "group3",\n      "size": 0\n    },\n    {\n      "group_name": "group4",\n      "size": 0\n    }\n  ]\n}'
#response = requests.post('http://localhost:8000/api/v1/create_groups', headers=headers, data=data)
