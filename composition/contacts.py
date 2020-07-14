from mixins import AsDictionaryMixin


class AddressBook:
    def __init__(self):
        self._employee_addresses = {
            1: Address('111 Manager\'s address', 'M city', 'M State', '11111'),
            2: Address('222 Secretary\'s address', 'S city', 'S State', '22222'),
            3: Address('333 Sales\'s address', 'Sales city', 'Sales State', '33333'),
            4: Address('444 Factory Worker\'s address', 'FW city', 'FW State', '44444'),
            5: Address('555 Temporary Secretary\'s address', 'TS city', 'TS State', '55555'),
        }

    def get_employee_address(self, employee_id):
        address = self._employee_addresses.get(employee_id)
        if not address:
            raise ValueError(employee_id)
        return address


class Address(AsDictionaryMixin):
    def __init__(self, street, city, state, zipcode, street2=''):
        self.street = street
        self.street2 = street2
        self.city = city
        self.state = state
        self.zipcode = zipcode

    def __str__(self):
        lines = [self.street]
        if self.street2:
            lines.append(self.street2)
        lines.append('{}, {}, {}'.format(self.city, self.state, self.zipcode))
        return '\n'.join(lines)
