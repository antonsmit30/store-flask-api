from werkzeug.security import safe_str_cmp
from models.user import UserModel


# Authenticate a User
def authenticate(username, password):
    # Another way of accessing dictionary
    user = UserModel.find_by_username(username)
    if user and safe_str_cmp(user.password, password):
        return user

def identity(payload):
    user_id = payload['identity']
    return UserModel.find_by_id(user_id)