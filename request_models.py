from pydantic import BaseModel
import datetime as dt


### Create models
class CreateGroupModel(BaseModel):
    group_name: str
    size: int = 0


class CreateGroups(BaseModel):
    groups: list[CreateGroupModel]


class CreateStudentModel(BaseModel):
    first_name: str
    middle_name: str
    last_name: str
    group_id: int


class CreateStudents(BaseModel):
    students: list[CreateStudentModel]


class CreateSubjectModel(BaseModel):
    id_teacher: int
    subject_name: str
    hours: int


class CreateTeacherModel(BaseModel):
    first_name: str
    middle_name: str
    last_name: str


class CreateAttendance(BaseModel):
    subject_id: int
    student_id: int
    date: dt.datetime
    pair_number: int
    status: str


### Delete models
class DeleteEntityModel(BaseModel):
    id: int
