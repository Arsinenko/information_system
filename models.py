from tortoise.models import Model
from tortoise import fields


class Group(Model):
    id = fields.IntField(pk=True)
    group_name = fields.CharField(max_length=20, unique=True)
    size = fields.IntField(default=0)

    class Meta:
        table = "groups"


class Teacher(Model):
    id = fields.IntField(pk=True)
    first_name = fields.CharField(max_length=20)
    middle_name = fields.CharField(max_length=20)
    last_name = fields.CharField(max_length=20)
    
    class Meta:
        table = "teachers"


class Subject(Model):
    id = fields.IntField(pk=True)
    teacher = fields.ForeignKeyField(model_name="models.Teacher", related_name="teacher_id",
                                        on_delete=fields.CASCADE)
    subject_name = fields.CharField(max_length=50)
    hours = fields.IntField(null=False)

    class Meta:
        table = "subjects"


class Student(Model):
    id = fields.IntField(pk=True)
    first_name = fields.CharField(max_length=20)
    middle_name = fields.CharField(max_length=20)
    last_name = fields.CharField(max_length=20)
    group = fields.ForeignKeyField(model_name="models.Group", related_name="Student_group", on_delete=fields.CASCADE)

    class Meta:
        table = "students"


class Attendance(Model):
    id = fields.IntField(pk=True)
    subject= fields.ForeignKeyField(model_name="models.Subject", related_name="attendance_subject",
                                        on_delete=fields.CASCADE)
    student = fields.ForeignKeyField(model_name="models.Student", related_name="attendance_student",
                                        on_delete=fields.CASCADE)
    date = fields.DateField(null=False)
    pair_number = fields.IntField(null=False)
    status = fields.CharField(max_length=50, choices=["be", "absent"])

    class Meta:
        table = "attendance"
