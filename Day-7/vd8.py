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
        return sale_amount/kpi

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
        #TODO: return 1.0 - c * missed_bugs/tested_bugs
        test_score = ...
        score = super().review_performance()
        return score * test_score

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