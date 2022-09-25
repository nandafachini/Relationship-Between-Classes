# Implement the class diagram below.

# ----------------------------                   -----------------
# | Person                   |                   | Job           |
# ----------------------------                   -----------------
# | name: str                |-------------------| post: str     |
# | telephone: int           |                   | role: str     |
# | email: str              |                   | salary: float |
# | job: Job                 |                   | bonus: int    |
# | dependents: List<Person> |                   -----------------
# ----------------------------
# | calculate_salary()       |
# ----------------------------

# calculate_salary(): returns the value of the employee's salary, 
# according to the bonus percentage and number of dependents. 
# For example, if the bonus is 2%, and the employee has 3 dependents, 
# he will receive a 6% increase on his salary.


class Job:
    def __init__(self, post, role, salary, bonus):
        self.post = post
        self.role = role
        self.salary = salary
        self.bonus = bonus


class Person:
    def __init__(self, name, telephone, email, job):
        self.name = name
        self.telephone = telephone
        self.email = email
        self.job = job
        self.dependents = []


    def calculate_salary(self):
        qty_dependents = len(self.dependents)
        salary = self.job.salary + (self.job.salary * ((self.job.bonus * qty_dependents)/100))
        return salary

job = Job("Programmer", "IT", 1000, 5)
person1 = Person("Paulo", "11-99999999", "paulo@email.com", job)

dep1 = Person("Maria", "", "", None)
dep2 = Person("Joao", "", "", None)

person1.dependents.append(dep1)
person1.dependents.append(dep2)

print("Salary: ", person1.calculate_salary())
