from pydantic import BaseModel


### Create models
class CreateGroupModel(BaseModel):
    group_name: str
    


class CreateStudentModel(BaseModel):
    first_name: str
    middle_name: str
    last_name: str
    group_id: int


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
    status: str


### Delete models
class DeleteEntityModel(BaseModel):
    id: int
