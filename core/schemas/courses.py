def course_serializer(course: dict) -> dict:
    return {
        "id": str(course["_id"]),
        "name": course["name"],
        "description": course["description"],
        "credit": course["credit"],
    }

# import strawberry
# from typing import Optional

# @strawberry.type
# class CourseType:
#     id: str
#     name: str
#     description: Optional[str]
#     credit: float