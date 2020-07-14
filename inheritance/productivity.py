def line_print():
    print('****************')


class ProductivitySystem():
    def track(self, employees, hours):
        print('Tracking employee productivity:')
        line_print()
        for employee in employees:
            result = employee.work(hours)
            print('{}: {}'.format(employee.name, result))
            line_print()


class ManagerRole:
    def work(self, hours):
        return 'Demands {} hours.'.format(hours)


class SecretaryRole:
    def work(self, hours):
        return 'Does paperwork for {} hours.'.format(hours)


class SalesRole:
    def work(self, hours):
        return 'Sells for {} hours.'.format(hours)


class FactoryRole:
    def work(self, hours):
        return 'Spends {} hours in the factory.'.format(hours)
