from application import people, salary
from datetime import date

if __name__ == '__main__':
    salary.calculate_salary()
    people.get_employees()
    print(date.today())