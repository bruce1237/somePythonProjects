
class asset:
    utility=700
    rent=1000
    business_rate=900
    salary_rate = 10
    working_hours = 8
    day_in_business = 5
    employee=1

    def __init__(self, employee=1, day_in_busniess=5):
        self.employee = employee
        self.day_in_business = day_in_busniess

    def monthly_cost(self):
        return self.utility + self.rent + self.business_rate + \
            (self.day_in_business * self.salary_rate * self.working_hours * self.employee)
