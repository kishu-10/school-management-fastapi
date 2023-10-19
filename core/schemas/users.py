def user_serializer(user: dict) -> dict:
    return {
        "id": str(user["_id"]),
        "first_name": user["first_name"],
        "middle_name": user["middle_name"],
        "last_name": user["last_name"],
        "email": user["email"],
        "user_type": user["user_type"],
    }


def program_serializer(program: dict) -> dict:
    return {
        "id": str(program["_id"]),
        "name": program["name"],
        "code": program["code"],
    }


def student_serializer(student: dict, user: dict) -> dict:
    return {
        "id": str(student["_id"]),
        "user": student["user"],
        "first_name": user["first_name"],
        "middle_name": user["middle_name"],
        "last_name": user["last_name"],
        "email": user["email"],
        "program": student["program"],
        "admission_date": student["admission_date"],
        "guardian_name": student["guardian_name"],
        "guardian_number": student["guardian_number"],
    }
