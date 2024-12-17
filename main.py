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
@app.get("/api/v1/get_students")  # verified
async def get_students():
    return await Student.all().values_list()


@app.get("/api/v1/get_teachers")  # verified
async def get_teachers():
    return await Teacher.all().values_list()


@app.get("/api/v1/get_groups")  # verified
async def get_groups():
    return await Group.all().values()


@app.get("/api/v1/get_subjects") # verified
async def get_subjects():
    return await Subject.all()


@app.get("/api/v1/get_attendance_records") #verified
async def get_attendance_records():
    return await Attendance.all()


### Create requests

@app.post("/api/v1/create_student")  #verified
async def create_user(item: CreateStudentModel):
    group = await Group.get(id=item.group_id)
    try:
        await Student.create(first_name=item.first_name, middle_name=item.middle_name, last_name=item.last_name,
                             group=group)
        group.size += 1
        await group.save()
        return JSONResponse(content={"message": "Success"}, status_code=200)
    except Exception as ex:
        return JSONResponse(content={"message": ex})


# @app.post("/api/v1/create_students") not work
# async def create_students(item: CreateStudents):
#     try: 
#         for elem in item.students:
#             group = await Group.get(id=elem.group_id)
#             await Student.create(first_name=elem.first_name, middle_name=elem.middle_name, last_name=elem.last_name)

#             group.size += 1
#             await group.save()
#             return JSONResponse(content={"message": "Success. Students"}, status_code=200)
#     except Exception as ex:
#         return JSONResponse(content={"message": ex})


@app.post("/api/v1/create_group")  #verified
async def create_group(item: CreateGroupModel):
    try:
        await Group.create(group_name=item.group_name)
        return JSONResponse(content={"message": "Success"}, status_code=200)
    except Exception as ex:
        return JSONResponse(content={"message": ex})


@app.post("/api/v1/create_groups")  # verified
async def create_groups(item: CreateGroups):
    try:
        for elem in item.groups:
            # Check if the group name already exists
            existing_group = await Group.filter(group_name=elem.group_name).first()
            if existing_group:
                return JSONResponse(content={"message": f"Group '{elem.group_name}' already exists."}, status_code=400)
            await Group.create(group_name=elem.group_name, size=elem.size)
        return JSONResponse(content={"message": "Success. Groups were created"}, status_code=200)
    except Exception as ex:
        return JSONResponse(content={"message": str(ex)}, status_code=500)


@app.post("/api/v1/create_subject")  # verified
async def create_subject(item: CreateSubjectModel):
    try:
        teacher = await Teacher.get(id=item.id_teacher)
        await Subject.create(teacher=teacher, subject_name=item.subject_name, hours=item.hours)
        return JSONResponse(content={"message": "Success"}, status_code=200)
    except Exception as ex:
        return JSONResponse(content={"message": ex})


@app.post("/api/v1/create_attendance_record")  #verified
async def create_attendance_record(item: CreateAttendance):
    try:
        student = await Student.get(id=item.student_id)
        subject = await Subject.get(id=item.subject_id)
        await Attendance.create(subject=subject, student=student, date=item.date, pair_number=item.pair_number, status=item.status)
        return JSONResponse(content={"message": "Success"}, status_code=200)
    except Exception as ex:
        return JSONResponse(content={"message": ex})


@app.post("/api/v1/create_teacher")  # verified
async def create_teacher(item: CreateTeacherModel):
    try:
        await Teacher.create(first_name=item.first_name, middle_name=item.middle_name, last_name=item.last_name)
        return JSONResponse(content={"message": "Success. Teacher created!"})
    except Exception as ex:
        return JSONResponse(content={"error": ex}, status_code=500)


### Delete requests

@app.delete("/api/v1/delete_student")  # verified
async def delete_student(item: DeleteEntityModel):
    try:
        await Student.filter(id=item.id).delete()
        return JSONResponse(content={"message": "Success"}, status_code=200)
    except Exception as ex:
        return JSONResponse(content={"message": ex})


@app.delete("/api/v1/delete_group")  #verified
async def delete_group(item: DeleteEntityModel):
    try:
        await Group.filter(id=item.id).delete()
        return JSONResponse(content={"message": "Success"}, status_code=200)
    except Exception as ex:
        return JSONResponse(content={"message": ex})


@app.delete("/api/v1/delete_subject")  #verified
async def delete_subject(item: DeleteEntityModel):
    try:
        await Subject.filter(id=item.id).delete()
        return JSONResponse(content={"message": "Success"}, status_code=200)
    except Exception as ex:
        return JSONResponse(content={"message": ex})


@app.delete("/api/v1/delete_teacher")  #verified
async def delete_teacher(item: DeleteEntityModel):
    try:
        await Teacher.filter(id=item.id).delete()
        return JSONResponse(content={"message": "Success"}, status_code=200)
    except Exception as ex:
        return JSONResponse(content={"message": ex})


@app.delete("/api/v1/delete_attendance_record")  #verified
async def delete_attendance_record(item: DeleteEntityModel):
    try:
        await Attendance.filter(id=item.id).delete()
        return JSONResponse(content={"message": "Success"}, status_code=200)
    except Exception as ex:
        return JSONResponse(content={"message": ex})


#### Pages verified

@app.get("/")  # verified
async def index():
    return FileResponse(path="ui/index.html", media_type="text/html")


@app.get("/students")  #verified
async def all_students():
    return FileResponse(path="ui/all_students_page.html", media_type="text/html")


@app.get("/groups")  # verified
async def groups():
    return FileResponse(path="ui/groups.html", media_type="text/html")


@app.get("/subjects")  # verified
async def subjects():
    return FileResponse(path="ui/subjects.html", media_type="text/html")


@app.get("/admin_page")  # verified
async def admin_page():
    return FileResponse(path="ui/admin_page.html", media_type="text/html")


if __name__ == "__main__":
    uvicorn.run(app=app, host="localhost", port=8000)
