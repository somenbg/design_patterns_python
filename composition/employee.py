from productivity import ProductivitySystem
from payroll import PayrollSystem
from contacts import AddressBook
from mixins import AsDictionaryMixin


class EmployeeDatabase:
    def __init__(self):
        self._employees = [
            {
                'id': 1,
                'name': 'Manager',
                'role': 'manager'
            },
            {
                'id': 2,
                'name': 'Secretary',
                'role': 'secretary'
            },
            {
                'id': 3,
                'name': 'Sales Guy',
                'role': 'sales'
            },
            {
                'id': 4,
                'name': 'Factory Worker',
                'role': 'factory'
            },
            {
                'id': 5,
                'name': 'Temporary Secretary',
                'role': 'secretary'
            },
        ]

        self.productivity = ProductivitySystem()
        self.payroll = PayrollSystem()
        self.employee_addresses = AddressBook()

    @property
    def employees(self):
        return [self._create_employee(**data) for data in self._employees]

    def _create_employee(self, id, name, role):
        address = self.employee_addresses.get_employee_address(id)
        employee_role = self.productivity.get_role(role)
        payroll_policy = self.payroll.get_policy(id)
        return Employee(id, name, address, employee_role, payroll_policy)


class Employee(AsDictionaryMixin):
    def __init__(self, id, name, address, role, payroll):
        self.id = id
        self.name = name
        self.address = address
        self._role = role
        self._payroll = payroll

    def work(self, hours):
        result = self._role.perform_duties(hours)
        print('{}: {}'.format(self.id, self.name))
        print('{}'.format(result))
        print('')
        self._payroll.track_work(hours)

    def calculate_payroll(self):
        return self._payroll.calculate_payroll()