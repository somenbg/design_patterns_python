def line_print():
    print('****************')

class  PayrollSystem():

    def calculate_payroll(self, employees):
        line_print()
        print('Calculating pay for employees:')
        line_print()
        for employee in employees:
            print('Payroll for {} - {}'.format(employee.id, employee.name))
            print('- Check amount: ${}'.format(employee.calculate_payroll()))
            if employee.address:
                print('- Sent to:')
                print(employee.address)
            line_print()


class SalaryPolicy:
    def __init__(self, weekly_salary):
        self.weekly_salary = weekly_salary

    def calculate_payroll(self):
        return self.weekly_salary

class HourlyPolicy:
    def __init__(self, hours_worked, hour_rate):
        self.hours_worked = hours_worked
        self.hour_rate = hour_rate

    def calculate_payroll(self):
        return self.hours_worked * self.hour_rate

class CommissionPolicy(SalaryPolicy):
    def __init__(self, weekly_salary, commission):
        super().__init__(weekly_salary)
        self.commission = commission

    def calculate_payroll(self):
        fixed = super().calculate_payroll()
        return fixed + self.commission

