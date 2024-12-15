from tortoise import Tortoise
from models import Teacher, Attendance, Group, Student, Subject
from fastapi import FastAPI
from fastapi.responses import FileResponse, JSONResponse
import uvicorn
from request_models import *


async def init():
    await Tortoise.init(
        db_url='sqlite://db.sqlite3',
        modules={'models': ['__main__']}
    )
    await Tortoise.generate_schemas()


async def close():
    await Tortoise.close_connections()


app = FastAPI()


### Events

@app.on_event("startup")
async def startup_event():
    await init()


@app.on_event("shutdown")
async def shutdown_event():
    await close()


#### API v1
### Get requests
@app.get("/api/v1/get_students")
async def get_students():
    return await Student.all()

@app.get("/api/v1/get_groups")
async def get_groups():
    return await Group.all().values("id", "group_name", "size")


@app.get("/api/v1/get_subjects")
async def get_subjects():
    return await Subject.all().values("id", "subject_name")


@app.get("/api/v1/get_attendance_records")
async def get_attendance_records():
    return await Attendance.all().values("id", "subject_id", "student_id", "status")


### Create requests

@app.post("/api/v1/create_student")
async def create_user(item: CreateStudentModel):
    group = await Group.get(id=item.group_id)
    try:
        await Student.create(first_name=item.first_name, middle_name=item.middle_name, last_name=item.last_name,
                             group_id=group)
        return JSONResponse(content={"message": "Success"}, status_code=200)
    except Exception as ex:
        return JSONResponse(content={"message": ex})


@app.post("/api/v1/create_group")
async def create_group(item: CreateGroupModel):
    try:
        await Group.create(group_name=item.group_name, size=item.size)
        return JSONResponse(content={"message": "Success"}, status_code=200)
    except Exception as ex:
        return JSONResponse(content={"message": ex})


@app.post("/api/v1/create_subject")
async def create_subject(item: CreateSubjectModel):
    try:
        await Student.create(subject_name=item.subject_name)
        return JSONResponse(content={"message": "Success"}, status_code=200)
    except Exception as ex:
        return JSONResponse(content={"message": ex})


@app.post("/api/v1/create_attendance_record")
async def create_attendance_record(item: CreateAttendance):
    try:
        await Attendance.create(subject_id=item.subject_id, student_id=item.student_id, status=item.status)
        return JSONResponse(content={"message": "Success"}, status_code=200)
    except Exception as ex:
        return JSONResponse(content={"message": ex})

@app.post("/api/v1/create_teacher")
async def create_teacher(item: CreateTeacherModel):
    try:
        await Teacher.create(first_name=item.first_name, middle_name=item.middle_name, last_name=item.last_name)
        return JSONResponse(content={"message": "Success. Teacher created!"})
    except Exception as ex:
        return JSONResponse(content={"error": ex}, status_code=500)

### Delete requests

@app.delete("/api/v1/delete_student")
async def delete_student(item: DeleteEntityModel):
    try:
        await Student.filter(id=item.id).delete()
        return JSONResponse(content={"message": "Success"}, status_code=200)
    except Exception as ex:
        return JSONResponse(content={"message": ex})


@app.delete("/api/v1/delete_group")
async def delete_group(item: DeleteEntityModel):
    try:
        await Group.filter(id=item.id).delete()
        return JSONResponse(content={"message": "Success"}, status_code=200)
    except Exception as ex:
        return JSONResponse(content={"message": ex})


@app.delete("/api/v1/delete_subject")
async def delete_subject(item: DeleteEntityModel):
    try:
        await Subject.filter(id=item.id).delete()
        return JSONResponse(content={"message": "Success"}, status_code=200)
    except Exception as ex:
        return JSONResponse(content={"message": ex})


@app.delete("/api/v1/delete_teacher")
async def delete_teacher(item: DeleteEntityModel):
    try:
        await Teacher.filter(id=item.id).delete()
        return JSONResponse(content={"message": "Success"}, status_code=200)
    except Exception as ex:
        return JSONResponse(content={"message": ex})


@app.delete("/api/v1/delete_attendance_record")
async def delete_attendance_record(item: DeleteEntityModel):
    try:
        await Attendance.filter(id=item.id).delete()
        return JSONResponse(content={"message": "Success"}, status_code=200)
    except Exception as ex:
        return JSONResponse(content={"message": ex})


#### Pages

@app.get("/")
async def index():
    return FileResponse(path="ui/index.html", media_type="text/html")


@app.get("/students")
async def all_students():
    return FileResponse(path="ui/all_students_page.html", media_type="text/html")


@app.get("/groups")
async def groups():
    return FileResponse(path="ui/groups.html", media_type="text/html")


@app.get("/subjects")
async def subjects():
    return FileResponse(path="ui/subjects.html", media_type="text/html")


@app.get("/admin_page")
async def admin_page():
    return FileResponse(path="ui/admin_page.html", media_type="text/html")


if __name__ == "__main__":
    uvicorn.run(app=app, port=8000)
