class SignupValidator:
    @staticmethod
    def validate_fields(signup_view):
        if signup_view.not_completed_data:
            return False, "Por favor, completa todos los campos."
        return True, None

    @staticmethod
    def validate_passwords(signup_data):
        if signup_data["password"] != signup_data["confirm_password"]:
            return False, "Las contraseñas no coinciden."
        return True, None

    @staticmethod
    def validate_subscription_type(subscription_type_name):
        if subscription_type_name not in ["free", "premium"]:
            return False, "Tipo de suscripción inválido. Usa 'free' o 'premium'."
        return True, None
