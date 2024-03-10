from .Mongo import mongo_collection


# Path: app/db/__init__.py

def get_user_history(uid):
    try:
        collection = mongo_collection('user_history')
        user_history = []
        for history in collection.find({"uid": uid}, {"_id": 0}):
            user_history.append(history)
        return user_history[0]['history']
    except Exception as e:
        print(f"Error getting user history: {str(e)}")
        return []


def get_all_user_history():
    try:
        collection = mongo_collection('user_history')
        all_user_history = []
        for user_history in collection.find({}, {"_id": 0}):
            all_user_history.append(user_history)
        return all_user_history
    except Exception as e:
        print(f"Error getting all user history: {str(e)}")
        return []
    
    
def save_user_history(uid, history):
    try:
        collection = mongo_collection('user_history')
        collection.update_one(
            {"uid": uid},
            {"$push": {"history": {"$each": history}}},
            upsert=True
        )
    except Exception as e:
        print(f"Error saving user history: {str(e)}")


