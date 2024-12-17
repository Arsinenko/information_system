# API Documentation

## Base URL
```
http://localhost:8000/api/v1
```

## Endpoints

### Get Requests

- **Get All Students**
  - **Endpoint:** `/get_students`
  - **Method:** `GET`
  - **Response:** List of students.

- **Get All Teachers**
  - **Endpoint:** `/get_teachers`
  - **Method:** `GET`
  - **Response:** List of teachers.

- **Get All Groups**
  - **Endpoint:** `/get_groups`
  - **Method:** `GET`
  - **Response:** List of groups.

- **Get All Subjects**
  - **Endpoint:** `/get_subjects`
  - **Method:** `GET`
  - **Response:** List of subjects.

- **Get All Attendance Records**
  - **Endpoint:** `/get_attendance_records`
  - **Method:** `GET`
  - **Response:** List of attendance records.

### Create Requests

- **Create Student**
  - **Endpoint:** `/create_student`
  - **Method:** `POST`
  - **Request Body:** 
    ```json
    {
      "first_name": "string",
      "middle_name": "string",
      "last_name": "string",
      "group_id": "integer"
    }
    ```
  - **Response:** Success message.

- **Create Group**
  - **Endpoint:** `/create_group`
  - **Method:** `POST`
  - **Request Body:** 
    ```json
    {
      "group_name": "string"
    }
    ```
  - **Response:** Success message.

- **Create Subject**
  - **Endpoint:** `/create_subject`
  - **Method:** `POST`
  - **Request Body:** 
    ```json
    {
      "id_teacher": "integer",
      "subject_name": "string",
      "hours": "integer"
    }
    ```
  - **Response:** Success message.

- **Create Attendance Record**
  - **Endpoint:** `/create_attendance_record`
  - **Method:** `POST`
  - **Request Body:** 
    ```json
    {
      "student_id": "integer",
      "subject_id": "integer",
      "date": "date",
      "pair_number": "integer",
      "status": "string"
    }
    ```
  - **Response:** Success message.

- **Create Teacher**
  - **Endpoint:** `/create_teacher`
  - **Method:** `POST`
  - **Request Body:** 
    ```json
    {
      "first_name": "string",
      "middle_name": "string",
      "last_name": "string"
    }
    ```
  - **Response:** Success message.

### Delete Requests

- **Delete Student**
  - **Endpoint:** `/delete_student`
  - **Method:** `DELETE`
  - **Request Body:** 
    ```json
    {
      "id": "integer"
    }
    ```
  - **Response:** Success message.

- **Delete Group**
  - **Endpoint:** `/delete_group`
  - **Method:** `DELETE`
  - **Request Body:** 
    ```json
    {
      "id": "integer"
    }
    ```
  - **Response:** Success message.

- **Delete Subject**
  - **Endpoint:** `/delete_subject`
  - **Method:** `DELETE`
  - **Request Body:** 
    ```json
    {
      "id": "integer"
    }
    ```
  - **Response:** Success message.

- **Delete Teacher**
  - **Endpoint:** `/delete_teacher`
  - **Method:** `DELETE`
  - **Request Body:** 
    ```json
    {
      "id": "integer"
    }
    ```
  - **Response:** Success message.

- **Delete Attendance Record**
  - **Endpoint:** `/delete_attendance_record`
  - **Method:** `DELETE`
  - **Request Body:** 
    ```json
    {
      "id": "integer"
    }
    ```
  - **Response:** Success message.

### Update Requests

- **Update Student**
  - **Endpoint:** `/update_student`
  - **Method:** `POST`
  - **Request Body:** 
    ```json
    {
      "id": "integer",
      "first_name": "string",
      "middle_name": "string",
      "last_name": "string",
      "group_id": "integer"
    }
    ```
  - **Response:** Success message.

- **Update Teacher**
  - **Endpoint:** `/update_teacher`
  - **Method:** `POST`
  - **Request Body:** 
    ```json
    {
      "id": "integer",
      "first_name": "string",
      "middle_name": "string",
      "last_name": "string"
    }
    ```
  - **Response:** Success message.

- **Update Subject**
  - **Endpoint:** `/update_subject`
  - **Method:** `POST`
  - **Request Body:** 
    ```json
    {
      "id": "integer",
      "id_teacher": "integer",
      "subject_name": "string",
      "hours": "integer"
    }
    ```
  - **Response:** Success message.

- **Update Attendance Record**
  - **Endpoint:** `/update_attendance_record`
  - **Method:** `POST`
  - **Request Body:** 
    ```json
    {
      "id": "integer",
      "student_id": "integer",
      "subject_id": "integer",
      "date": "date",
      "pair_number": "integer",
      "status": "string"
    }
    ```
  - **Response:** Success message.

## Data Models

- **Group**
  - **Fields:**
    - `id`: Integer (Primary Key)
    - `group_name`: String (Unique)
    - `size`: Integer (Default: 0)

- **Teacher**
  - **Fields:**
    - `id`: Integer (Primary Key)
    - `first_name`: String
    - `middle_name`: String
    - `last_name`: String

- **Subject**
  - **Fields:**
    - `id`: Integer (Primary Key)
    - `teacher`: ForeignKey (Teacher)
    - `subject_name`: String
    - `hours`: Integer

- **Student**
  - **Fields:**
    - `id`: Integer (Primary Key)
    - `first_name`: String
    - `middle_name`: String
    - `last_name`: String
    - `group`: ForeignKey (Group)

- **Attendance**
  - **Fields:**
    - `id`: Integer (Primary Key)
    - `subject`: ForeignKey (Subject)
    - `student`: ForeignKey (Student)
    - `date`: Date
    - `pair_number`: Integer
    - `status`: String (Choices: "be", "absent")
