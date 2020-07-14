def line_print():
    print('****************')


class PayrollSystem:
    def __init__(self):
        self._employee_policies = {
            1: SalaryPolicy(1000),
            2: SalaryPolicy(500),
            3: CommissionPolicy(400, 200),
            4: HourlyPolicy(10),
            5: HourlyPolicy(20)
        }

    def get_policy(self, employee_id):
        policy = self._employee_policies.get(employee_id)
        if not policy:
            return ValueError(employee_id)
        return policy

    def calculate_payroll(self, employees):
        print('Calculating pay for employees:')
        line_print()
        for employee in employees:
            print('Payroll for {} - {}'.format(employee.id, employee.name))
            print('- Check amount: ${}'.format(employee.calculate_payroll()))
            if employee.address:
                print('- Sent to:')
                print(employee.address)
            line_print()


class PayrollPolicy:
    def __init__(self):
        self.hours_worked = 0

    def track_work(self, hours):
        self.hours_worked += hours


class SalaryPolicy(PayrollPolicy):
    def __init__(self, weekly_salary):
        super().__init__()
        self.weekly_salary = weekly_salary

    def calculate_payroll(self):
        return self.weekly_salary


class HourlyPolicy(PayrollPolicy):
    def __init__(self, hour_rate):
        super().__init__()
        self.hour_rate = hour_rate

    def calculate_payroll(self):
        return self.hours_worked * self.hour_rate


class CommissionPolicy(SalaryPolicy):
    def __init__(self, weekly_salary, commission_per_sale):
        super().__init__(weekly_salary)
        self.commission_per_sale = commission_per_sale

    @property
    def commission(self):
        sales = self.hours_worked / 20
        return sales * self.commission_per_sale

    def calculate_payroll(self):
        fixed = super().calculate_payroll()
        return fixed + self.commission