class Employee:
    def __init__(self, name, email, phone):
        self.name = name
        self.email = email
        self.phone = phone
        self.late_days = 0

    def check_in(self, date):
        #TODO: if date.time > 8h30: self.late_days += 1
        pass

    def review_performance(self):
        score = 1.0 - self.late_days/30
        self.late_days = 0
        return score

class Sale(Employee):
    def __init__(self, name, email, phone, kpi):
        super().__init__(name, email, phone)
        self.kpi = kpi
        self.sale_amount = 0
    
    def sell(self, amount):
        self.sale_amount += amount
        
    def review_performance(self):
        return self.sale_amount/self.kpi

sale_1 = Sale('Nguyen Van Sale', 'sale1@abc.com', '012324214', 100000000)
sale_1.sell(50000000)
sale_1.sell(20000000)
sale_1.sell(10000000)
print(sale_1.name, ':' , sale_1.review_performance())

class Tester(Employee):
    def __init__(self, name, email, phone):
        super().__init__(name, email, phone)
        self.tested_bugs = 0
        self.missed_bugs = 0

    def test_bug(self):
        self.tested_bugs += 1

    def bad_report_from_customer(self):
        self.missed_bugs += 1

    def review_performance(self):
        c = 2.0
        test_score = 1.0 - c * self.missed_bugs/self.tested_bugs
        score = super().review_performance()
        self.tested_bugs = self.missed_bugs = 0
        return (0.5+0.5*score) * test_score

tester = Tester('Nguyen Van Test', 'nvtest@abc.com', '01231235')
for i in range(10): tester.test_bug()
tester.bad_report_from_customer()
print(tester.name, ':', tester.review_performance())

class PM(Employee):
    def assign_task(self, dev, date):
        dev.current_deadline = date

class Dev(Employee):
    def __init__(self, name, email, phone):
        self.total_tasks = 0
        self.late_tasks = 0
        self.current_deadline = None

    def commit_task(self, date):
        # TODO: check (date vs deadline) --> late_tasks += 1
        self.total_tasks += 1

    def review_performance(self):
        #TODO: return 1.0 - c * late_tasks/total_tasks
        return ...