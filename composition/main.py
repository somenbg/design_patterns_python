# from payroll import PayrollSystem, HourlyPolicy
# from productivity import ProductivitySystem
# from employee import EmployeeDatabase

# productivity_system = ProductivitySystem()
# payroll_system = PayrollSystem()
# employee_database = EmployeeDatabase()
# employees = employee_database.employees
# manager = employees[0]
# manager.payroll = HourlyPolicy(50)

# productivity_system.track(employees, 40)
# payroll_system.calculate_payroll(employees)

import json
from employee import EmployeeDatabase

def print_dict(d):
    print(json.dumps(d, indent=2))

for employee in EmployeeDatabase().employees:
    print_dict(employee.to_dict())