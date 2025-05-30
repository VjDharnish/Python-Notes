from employee import Secretary,HourlyEmployee
import hr
import productivity

class TemporaryEmployee(Secretary,HourlyEmployee):
    def __init__(self, id, name, hours_worked, hourly_rate):
        HourlyEmployee.__init__(self, id, name, hours_worked, hourly_rate)
        pass
    def calculate_payroll(self):
        # return super().calculate_payroll() #super() by default invokes SalrayEMployye calcuilate_payroll()  method due to Secretary is first inherited
        return HourlyEmployee.calculate_payroll(self) # explicitlky specifues to use HourlyEmployee's calculate method

print(TemporaryEmployee.__mro__)

temp_employee = TemporaryEmployee(11,"Dharun",40,9)
company_employees = [
    temp_employee,
]
print(TemporaryEmployee.__bases__)

productivity_system = productivity.ProductivitySystem()
productivity_system.track(company_employees, 40)

payroll_system = hr.PayrollSystem()
payroll_system.calculate_payroll(company_employees)