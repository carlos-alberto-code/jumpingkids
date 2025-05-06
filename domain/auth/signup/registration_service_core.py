from domain.registration.registration_service_port import RegistrationServicePort
from domain.registration.registration_repository_port import RegistrationRepositoryPort

class RegistrationServiceCore(RegistrationServicePort):
    def __init__(self, repository: RegistrationRepositoryPort):
        self.repository = repository
        self.session = {
            'tutor_data': None,
            'children': [],
            'subscription_type': None,
            'payment_status': None
        }

    def start_registration(self, tutor_data: dict):
        self.session['tutor_data'] = tutor_data

    def add_child(self, child_data: dict):
        self.session['children'].append(child_data)

    def set_subscription(self, subscription_type: str):
        self.session['subscription_type'] = subscription_type

    def process_payment(self, payment_data: dict):
        # Mock: siempre éxito
        self.session['payment_status'] = 'success'

    def finalize_registration(self):
        tutor_id = self.repository.save_tutor(self.session['tutor_data'])
        self.repository.save_children(tutor_id, self.session['children'])
        self.repository.save_subscription(tutor_id, self.session['subscription_type'])
        return tutor_id
