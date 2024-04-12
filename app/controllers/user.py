from app.models import UserRegister, UserLogin
from app.db import get_database_client
from bson import ObjectId
import bcrypt


def register_user(user_data: UserRegister):
    db_client = get_database_client()
    users_collection = db_client["users"]

    # Check if user with given email already exists
    existing_user = users_collection.find_one({"email": user_data.email})
    if existing_user:
        return None
    print(user_data.password)

    # Hash the password before storing it
    hashed_password = bcrypt.hashpw(user_data.password.encode('utf-8'), bcrypt.gensalt())

    # Insert new user into the database
    user_data_dict = user_data.dict()
    user_data_dict["password"] = hashed_password.decode('utf-8')  # Store hashed password
    user_id = users_collection.insert_one(user_data_dict).inserted_id

    return str(user_id)


def login_user(user_data: UserLogin):
    db_client = get_database_client()
    users_collection = db_client["users"]

    # Find user with given email
    user_info = users_collection.find_one({"email": user_data.email})
    print(user_data.password)
    # Verify password
    if user_info and bcrypt.checkpw(user_data.password.encode('utf-8'), user_info['password'].encode('utf-8')):
        # Remove password field before returning user info
        user_info.pop('password')
        user_info['_id'] = str(user_info['_id'])
        return user_info
    else:
        return None
