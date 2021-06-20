from infraestructure import mongoImp

mongo = mongoImp.MongoImplementation() #this is remplace by an interface


class UseCases(object):

    @staticmethod
    def find_last_registers(document_name: str, field_name: str):
        documents = mongo.find_last_iot_registers(document_name, field_name)
        return documents

    @staticmethod
    def register_user(user):
        
        user_id = mongo.insert_document("iot_devices", "users", user)
        return user_id