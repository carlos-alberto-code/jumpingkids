class TutorDataBuilder:
    @staticmethod
    def build(signup_data, subscription_type_name):
        return {
            "username": signup_data["username"],
            "password": signup_data["password"],
            "full_name": signup_data["full_name"],
            "children": [],
            "subscription_type": subscription_type_name
        }
