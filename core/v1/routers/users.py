from bson import ObjectId
from fastapi import APIRouter, BackgroundTasks, Request, status

from core.database import get_db
from core.email import Email
from core.models.users import Program, StudentProfile, User
from core.schemas.users import program_serializer, student_serializer, user_serializer
from core.utils import Response

user_routes = APIRouter()

user_collection = get_db().get_collection("users")
program_collection = get_db().get_collection("programs")
student_collection = get_db().get_collection("studentprofiles")
student_course_collection = get_db().get_collection("studentcoursedetails")
student_record_detail_collection = get_db().get_collection("studentannualrecorddetails")


async def send_verification_email(user: User, url: str):
    await Email(user, url, [user.email]).send_verification_code()


@user_routes.post("/create")
async def create_user(user: User, request: Request, background_tasks: BackgroundTasks):
    _user = user_collection.insert_one(dict(user))
    new_user = user_serializer(user_collection.find_one({"_id": _user.inserted_id}))
    url = f"{request.url.scheme}://{request.client.host}:{request.url.port}/api/auth/verifyemail"
    background_tasks.add_task(send_verification_email, user, url)
    return Response(
        status_code=status.HTTP_201_CREATED,
        message="User created successfully.",
        data=new_user,
    )


@user_routes.put("/{id}")
async def update_user(id: str, user: User):
    user_collection.find_one_and_update({"_id": ObjectId(id)}, {"$set": dict(user)})
    user = user_serializer(user_collection.find_one({"_id": ObjectId(id)}))
    return Response(
        status_code=status.HTTP_200_OK, message="User updated successfully.", data=user
    )


@user_routes.get("")
async def retrieve_users():
    users = []
    for user in user_collection.find():
        users.append(user_serializer(user))
    return Response(
        status_code=status.HTTP_200_OK,
        message="Users retrieved successfully.",
        data=users,
    )


@user_routes.get("/{id}")
async def retrieve_user(id: str):
    user = user_collection.find_one({"_id": ObjectId(id)})
    return Response(
        status_code=status.HTTP_200_OK,
        message="User retrieved successfully.",
        data=user,
    )


@user_routes.post("/create-program")
async def create_program(program: Program):
    _program = program_collection.insert_one(dict(program))
    program = program_serializer(program_collection.find_one({"_id": _program.inserted_id}))
    return Response(
        status_code=status.HTTP_201_CREATED,
        message="Program created successfully.",
        data=program,
    )


@user_routes.post("/student-profile")
async def create_student_profile(profile: StudentProfile):
    _student = student_collection.insert_one(dict(profile))
    user = user_collection.find_one({"_id": ObjectId(profile.user)})
    student = student_serializer(_student, user)
    return Response(
        status_code=status.HTTP_201_CREATED,
        message="Student profile created successfully.",
        data=student,
    )
