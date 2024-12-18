from faker import Faker
import requests

faker = Faker("ru_RU")


    


def push_students(faker):
    for i in range(40):
        first_name = faker.first_name_male()
        middle_name = faker.middle_name_male()
        last_name = faker.last_name_male()
    # send request
        data = {
        "first_name": first_name,
        "middle_name": middle_name,
        "last_name": last_name,
        "group_id" : 1
    }
        header = {
        "Content-Type": "application/json",
    }
        response = requests.post(json=data, url="http://localhost:8000/api/v1/create_student", headers=header)
        print(response.status_code)

push_students(faker)