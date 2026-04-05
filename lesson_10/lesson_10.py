# Завдання 1
# Створіть клас Employee, який має атрибути name та salary.
# Далі створіть два класи, Manager та Developer, які успадковуються від Employee. Клас Manager повинен мати додатковий атрибут department, а клас Developer - атрибут programming_language.
# Тепер створіть клас TeamLead, який успадковується як від Manager, так і від Developer.
# Цей клас представляє керівника з команди розробників.
# Клас TeamLead повинен мати всі атрибути як Manager (ім'я, зарплата, відділ), а також атрибут team_size, який вказує на кількість розробників у команді, якою керує керівник.
# Напишіть тест, який перевіряє наявність атрибутів з Manager та Developer у класі TeamLead

class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

class Manager(Employee):
    def __init__(self, name, salary, department):
        self.department = department
        Employee.__init__(self, name, salary)

class Developer(Employee):
    def __init__(self, name, salary, programming_language):
        self.programming_language = programming_language
        Employee.__init__(self, name, salary)

class TeamLead(Manager, Developer):
    def __init__(self, name, salary, department, team_size, programming_language):
        self.team_size = team_size
        Manager.__init__(self, name, salary, department)
        Developer.__init__(self, name, salary, programming_language)

team_lead = TeamLead("Andrii", 70, "QA", 5, "Python")
assert hasattr(team_lead, "name")
assert hasattr(team_lead, "salary")
assert hasattr(team_lead, "department")
assert hasattr(team_lead, "programming_language")
assert hasattr(team_lead, "team_size")
