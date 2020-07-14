import payroll as pay
import productivity as prod
import employee as emp
import contacts as con


manager = emp.Manager(1, 'Manager', weekly_salary=1000)
manager.address = con.Address(street='111 Manager\'s address', city='M city', state='M State', zipcode='11111')

secretary = emp.Secretary(2, 'Secretary', weekly_salary=500)
secretary.address = con.Address(street='222 Secretary\'s address', city='S city', state='S State', zipcode='22222')

sales_person = emp.SalesPerson(3, 'Sales Guy', weekly_salary=400, commission=200)
sales_person.address = con.Address(street='333 Sales\'s address', city='Sales city', state='Sales State', zipcode='33333')

factory_worker = emp.FactoryWorker(4, 'Factory Worker', hours_worked=40, hour_rate=10)
factory_worker.address = con.Address(street='444 Factory Worker\'s address', city='FW city', state='FW State', zipcode='44444')

temp_worker = emp.TemporarySecretary(5, 'Temporary Secretary', hours_worked=40, hour_rate=20)
temp_worker.address = con.Address(street='555 Temporary Secretary\'s address', city='TS city', state='TS State', zipcode='55555')


employees = [manager, secretary, sales_person, factory_worker, temp_worker]

productivity_system = prod.ProductivitySystem()
productivity_system.track(employees, 40)

payroll_system = pay.PayrollSystem()
payroll_system.calculate_payroll(employees)
