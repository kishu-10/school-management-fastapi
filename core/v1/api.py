from fastapi import FastAPI
from core.v1.routers import courses, users, graphql

apiv1 = FastAPI()
apiv1.include_router(users.user_routes, prefix="/users")
apiv1.include_router(courses.course_routes, prefix="/courses")
apiv1.include_router(graphql.graphql_app, prefix="/graphql")

@apiv1.get('/')
def index():
    return {"message": "This is v1 of this application."}
