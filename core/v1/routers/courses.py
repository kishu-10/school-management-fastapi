from bson import ObjectId
from fastapi import APIRouter
from core.database import get_db
from core.models.courses import Course
from core.schemas.courses import course_serializer
from core.utils import Response
from fastapi import status

course_routes = APIRouter()

course_collection = get_db().get_collection("courses")


@course_routes.post("/create")
async def create_course(course: Course):
    _course = course_collection.insert_one(dict(course))
    course = course_serializer(course_collection.find_one({"_id": _course.inserted_id}))
    return Response(
        status_code=status.HTTP_201_CREATED,
        message="Course created successfully.",
        data=course,
    )


@course_routes.get("/")
async def retrieve_courses():
    courses = []
    for course in course_collection.find():
        courses.append(course_serializer(course))
    return Response(
        status_code=status.HTTP_200_OK,
        message="Courses retrieved successfully.",
        data=courses,
    )


@course_routes.get("/{id}")
async def retrieve_course(id: str):
    course = course_serializer(course_collection.find_one({"_id": ObjectId(id)}))
    return Response(
        status_code=status.HTTP_200_OK,
        message="Course retrieved successfully.",
        data=course,
    )


@course_routes.put("/{id}")
async def update_course(id: str, course: Course):
    course_collection.find_one_and_update({"_id": ObjectId(id)}, {"$set": dict(course)})
    course = course_serializer(course_collection.find_one({"_id": ObjectId(id)}))
    return Response(
        status_code=status.HTTP_200_OK,
        message="Course updated successfully.",
        data=course,
    )


@course_routes.delete("/{id}")
async def delete_course(id: str):
    course_collection.find_one_and_delete({"_id": ObjectId(id)})
    return Response(
        status_code=status.HTTP_204_NO_CONTENT,
        message="Course updated successfully.",
        data={},
    )
