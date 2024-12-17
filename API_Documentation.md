# API Documentation

## Base URL
```
http://localhost:8000/api/v1
```

## Endpoints

### 1. Get Requests

- **Get Students**
  - **Endpoint:** `/get_students`
  - **Method:** GET
  - **Response:** List of students.

- **Get Teachers**
  - **Endpoint:** `/get_teachers`
  - **Method:** GET
  - **Response:** List of teachers.

- **Get Groups**
  - **Endpoint:** `/get_groups`
  - **Method:** GET
  - **Response:** List of groups.

- **Get Subjects**
  - **Endpoint:** `/get_subjects`
  - **Method:** GET
  - **Response:** List of subjects with `id` and `subject_name`.

- **Get Attendance Records**
  - **Endpoint:** `/get_attendance_records`
  - **Method:** GET
  - **Response:** List of attendance records with `id`, `subject_id`, `student_id`, and `status`.

### 2. Create Requests

- **Create Student**
  - **Endpoint:** `/create_student`
  - **Method:** POST
  - **Request Body:**
    ```json
    {
      "first_name": "string",
      "middle_name": "string",
      "last_name": "string",
      "group_id": "integer"
    }
    ```
  - **Response:** Success message or error message.

- **Create Group**
  - **Endpoint:** `/create_group`
  - **Method:** POST
  - **Request Body:**
    ```json
    {
      "group_name": "string",
      "size": "integer"
    }
    ```
  - **Response:** Success message or error message.

- **Create Groups**
  - **Endpoint:** `/create_groups`
  - **Method:** POST
  - **Request Body:**
    ```json
    {
      "groups": [
        {
          "group_name": "string",
          "size": "integer"
        }
      ]
    }
    ```
  - **Response:** Success message or error message.

- **Create Subject**
  - **Endpoint:** `/create_subject`
  - **Method:** POST
  - **Request Body:**
    ```json
    {
      "id_teacher": "integer",
      "subject_name": "string",
      "hours": "integer"
    }
    ```
  - **Response:** Success message or error message.

- **Create Attendance Record**
  - **Endpoint:** `/create_attendance_record`
  - **Method:** POST
  - **Request Body:**
    ```json
    {
      "subject_id": "integer",
      "student_id": "integer",
      "status": "string"
    }
    ```
  - **Response:** Success message or error message.

- **Create Teacher**
  - **Endpoint:** `/create_teacher`
  - **Method:** POST
  - **Request Body:**
    ```json
    {
      "first_name": "string",
      "middle_name": "string",
      "last_name": "string"
    }
    ```
  - **Response:** Success message or error message.

### 3. Delete Requests

- **Delete Student**
  - **Endpoint:** `/delete_student`
  - **Method:** DELETE
  - **Request Body:**
    ```json
    {
      "id": "integer"
    }
    ```
  - **Response:** Success message or error message.

- **Delete Group**
  - **Endpoint:** `/delete_group`
  - **Method:** DELETE
  - **Request Body:**
    ```json
    {
      "id": "integer"
    }
    ```
  - **Response:** Success message or error message.

- **Delete Subject**
  - **Endpoint:** `/delete_subject`
  - **Method:** DELETE
  - **Request Body:**
    ```json
    {
      "id": "integer"
    }
    ```
  - **Response:** Success message or error message.

- **Delete Teacher**
  - **Endpoint:** `/delete_teacher`
  - **Method:** DELETE
  - **Request Body:**
    ```json
    {
      "id": "integer"
    }
    ```
  - **Response:** Success message or error message.

- **Delete Attendance Record**
  - **Endpoint:** `/delete_attendance_record`
  - **Method:** DELETE
  - **Request Body:**
    ```json
    {
      "id": "integer"
    }
    ```
  - **Response:** Success message or error message.

### Additional Information
- **Error Handling:** Each endpoint returns a JSON response with a message indicating success or failure.
- **Authentication:** Currently, there is no authentication implemented in the API.
