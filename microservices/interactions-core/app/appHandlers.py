from flask_restful import Resource
from flask_api import status
from flask import request
from domain.useCases import UseCases
import bcrypt


class Main(Resource):
    def get(self):
        documents = UseCases.find_last_registers("iot_devices", "created_at")
        if(len(documents) > 0):
            return documents, status.HTTP_200_OK
        else:
            return documents, status.HTTP_204_NO_CONTENT


class Registry(Resource):
    def post(self):
        request_data = request.get_json()
        is_user_name = "username" in request_data.keys()
        is_password = "password" in request_data.keys()

        if (is_password and is_user_name):
            hashed_pwd = bcrypt.hashpw(
                request_data["password"].encode('utf8'), bcrypt.gensalt())
            user = {
                "username": request_data["username"], "password": hashed_pwd}
            user_id = UseCases.register_user(user)
            return {"user_id": user_id}, status.HTTP_201_CREATED
        else:
            return {"status": False}, status.HTTP_400_BAD_REQUEST
