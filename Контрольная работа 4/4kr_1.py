"""Создать базовый класс – работник, и производные классы – служащий с почасовой оплатой, служащий в штате и служащий
с процентной ставкой. Определить функцию начисления зарплаты"""

class Worker:
    def calculate_salary(self):
        raise NotImplementedError("Метод calculate_salary должен быть переопределен в дочерних классах")

#Служащий с почасовой оплатой
class HourlyEmployee(Worker):
    def __init__(self, hours_worked, hourly_rate):
        self.hours_worked = hours_worked 
        self.hourly_rate = hourly_rate

    def calculate_salary(self):
        return self.hours_worked * self.hourly_rate

#Служащий в штате
class SalariedEmployee(Worker):
    def __init__(self, monthly_salary):
        self.monthly_salary = monthly_salary

    def calculate_salary(self):
        return self.monthly_salary

#Служащий с процентной ставкой
class CommissionedEmployee(Worker):
    def __init__(self, sales_amount, commission_rate):
        self.sales_amount = sales_amount
        self.commission_rate = commission_rate

    def calculate_salary(self):
        return self.sales_amount * self.commission_rate

if __name__ == "__main__":
    emp = HourlyEmployee(40, 15)
    print(emp.calculate_salary())
    emp = SalariedEmployee(3000)
    print(emp.calculate_salary())
    emp = CommissionedEmployee(10000, 0.2)
    print(emp.calculate_salary())

