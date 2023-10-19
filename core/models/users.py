from datetime import datetime, date
from enum import Enum
from typing import List, Union

from pydantic import BaseModel


class UserTypeEnum(str, Enum):
    admin = "admin"
    teacher = "teacher"
    student = "student"


class User(BaseModel):
    first_name: str
    middle_name: Union[str, None]
    last_name: str
    email: str
    user_type: UserTypeEnum


class Program(BaseModel):
    name: str
    code: str


class StudentProfile(BaseModel):
    user: str
    program: str
    admission_date: date
    guardian_name: str
    guardian_number: str
    
    class Config:
        arbitrary_types_allowed = True

    
    @classmethod
    def from_json(cls, data):
        # Convert a string date to a datetime object
        data["admission_date"] = datetime.strptime(data["admission_date"], "%Y-%m-%d").date()
        
        return cls(**data)

    def to_json(self):
        data = self.dict()
        
        # Convert the date to a string in the format "%Y-%m-%d"
        data["admission_date"] = self.admission_date.strftime("%Y-%m-%d")
        
        return data


class StudentCourseDetail(BaseModel):
    student: str
    courses: str
    enrollment_date: date
    grade: Union[str, None]
    percentage: Union[float, None]
    attendance: Union[float, None]

    class Config:
        arbitrary_types_allowed = True


class StudentAnnualRecordDetail(BaseModel):
    student: str
    year: int
    student_courses: List[str]
    grade: Union[str, None]
    percentage: Union[float, None]
    attendance: Union[float, None]

    class Config:
        arbitrary_types_allowed = True
