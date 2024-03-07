# domain/services/user_service.py
class UserService:
    def __init__(self, user_repo):
        self.user_repo = user_repo

    def get_all_users(self):
        return self.user_repo.get_all_users()

    def get_user(self, user_id):
        return self.user_repo.get_user(user_id)

    def create_user(self, user_data):
        return self.user_repo.create_user(user_data)
    
    def delete_user(self, user_id):
        return self.user_repo.delete_user(user_id)
