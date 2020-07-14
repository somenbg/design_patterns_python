def line_print():
    print('****************')


class ProductivitySystem:
    def __init__(self):
        self._roles = {
            'manager': ManagerRole,
            'secretary': SecretaryRole,
            'sales': SalesRole,
            'factory': FactoryRole,
            # 'temp': ManagerRole,
        }

    def get_role(self, role_id):
        role_type = self._roles.get(role_id)
        if not role_type:
            raise ValueError(role_id)
        return role_type()

    def track(self, employees, hours):
        print('Tracking employee productivity:')
        line_print()
        for employee in employees:
            employee.work(hours)
            line_print()

class ManagerRole:
    def perform_duties(self, hours):
        return 'Demands {} hours.'.format(hours)

class SecretaryRole:
    def perform_duties(self, hours):
        return 'Does paperwork for {} hours.'.format(hours)

class SalesRole:
    def perform_duties(self, hours):
        return 'Sells for {} hours.'.format(hours)

class FactoryRole:
    def perform_duties(self, hours):
        return 'Spends {} hours in the factory.'.format(hours)
