# API Documentation

## Base URL
`http://localhost:8000`

## Endpoints

### GET Requests

- **Get Students**
  - **URL:** `/api/v1/get_students`
  - **Method:** `GET`
  - **Response:** List of students.

- **Get Teachers**
  - **URL:** `/api/v1/get_teachers`
  - **Method:** `GET`
  - **Response:** List of teachers.

- **Get Groups**
  - **URL:** `/api/v1/get_groups`
  - **Method:** `GET`
  - **Response:** List of groups.

- **Get Subjects**
  - **URL:** `/api/v1/get_subjects`
  - **Method:** `GET`
  - **Response:** List of subjects.

- **Get Attendance Records**
  - **URL:** `/api/v1/get_attendance_records`
  - **Method:** `GET`
  - **Response:** List of attendance records.

### POST Requests

- **Create Student**
  - **URL:** `/api/v1/create_student`
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
  - **Response:** 
    ```json
    {
      "message": "Success"
    }
    ```

- **Create Group**
  - **URL:** `/api/v1/create_group`
  - **Method:** `POST`
  - **Request Body:** 
    ```json
    {
      "group_name": "string"
    }
    ```
  - **Response:** 
    ```json
    {
      "message": "Success"
    }
    ```

- **Create Subject**
  - **URL:** `/api/v1/create_subject`
  - **Method:** `POST`
  - **Request Body:** 
    ```json
    {
      "subject_name": "string",
      "hours": "integer",
      "id_teacher": "integer"
    }
    ```
  - **Response:** 
    ```json
    {
      "message": "Success"
    }
    ```

- **Create Attendance Record**
  - **URL:** `/api/v1/create_attendance_record`
  - **Method:** `POST`
  - **Request Body:** 
    ```json
    {
      "student_id": "integer",
      "subject_id": "integer",
      "date": "string",
      "pair_number": "integer",
      "status": "string"
    }
    ```
  - **Response:** 
    ```json
    {
      "message": "Success"
    }
    ```

### DELETE Requests

- **Delete Student**
  - **URL:** `/api/v1/delete_student`
  - **Method:** `DELETE`
  - **Request Body:** 
    ```json
    {
      "id": "integer"
    }
    ```
  - **Response:** 
    ```json
    {
      "message": "Success"
    }
    ```

- **Delete Group**
  - **URL:** `/api/v1/delete_group`
  - **Method:** `DELETE`
  - **Request Body:** 
    ```json
    {
      "id": "integer"
    }
    ```
  - **Response:** 
    ```json
    {
      "message": "Success"
    }
    ```

- **Delete Subject**
  - **URL:** `/api/v1/delete_subject`
  - **Method:** `DELETE`
  - **Request Body:** 
    ```json
    {
      "id": "integer"
    }
    ```
  - **Response:** 
    ```json
    {
      "message": "Success"
    }
    ```

- **Delete Teacher**
  - **URL:** `/api/v1/delete_teacher`
  - **Method:** `DELETE`
  - **Request Body:** 
    ```json
    {
      "id": "integer"
    }
    ```
  - **Response:** 
    ```json
    {
      "message": "Success"
    }
    ```

- **Delete Attendance Record**
  - **URL:** `/api/v1/delete_attendance_record`
  - **Method:** `DELETE`
  - **Request Body:** 
    ```json
    {
      "id": "integer"
    }
    ```
  - **Response:** 
    ```json
    {
      "message": "Success"
    }
    ```

## Pages

- **Index Page**
  - **URL:** `/`
  - **Method:** `GET`
  - **Response:** HTML page.

- **All Students Page**
  - **URL:** `/students`
  - **Method:** `GET`
  - **Response:** HTML page.

- **Groups Page**
  - **URL:** `/groups`
  - **Method:** `GET`
  - **Response:** HTML page.

- **Subjects Page**
  - **URL:** `/subjects`
  - **Method:** `GET`
  - **Response:** HTML page.

- **Admin Page**
  - **URL:** `/admin_page`
  - **Method:** `GET`
  - **Response:** HTML page.
