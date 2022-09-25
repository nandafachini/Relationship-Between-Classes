# Implement the class diagram below.

# ---------------------                   -----------------
# | Exam              |                   | Patient       |
# ---------------------                   -----------------
# | doctor: Doctor    |------------------ | name: str     |
# | patient: Patient  |                   | id: str       |
# | description: str  |                   | age: int      |
# | result: str       |                   -----------------
# ---------------------
# | print_exam()      |
# ---------------------
#           |
#           |
#           |
# -----------------------
# | Doctor              |
# -----------------------
# | name: str           |
# | id: str             |
# | specialization: str |
# -----------------------


# print_exam(): displays a report with exam data 
# (including physician and patient data)


class Doctor:
    def __init__(self, name, id, specialization):
        self.name = name
        self.id = id
        self.specialization = specialization


class Patient:
    def __init__(self, name, id, age):
        self.name = name
        self.id = id
        self.age = age
    

class Exam:
    def __init__(self, doctor, patient, description, result):
        self.doctor = doctor
        self.patient = patient
        self.description = description
        self.result = result


    def print_exam(self):
        print("The patient with name: " , self.patient.name , "and ID: " , self.patient.id , 
        "and age of: " , self.patient.age , "years old" , "Consulted with the doctor: ", self.doctor.name , 
        "which ID is: " , self.doctor.id , "and specialization is: " , self.doctor.specialization ,
        "realized the exam: " , self.description , "and had the result: " , self.result)

    
paciente = Patient('Marcelo Silva', '033444555-22', 26)
medico = Doctor('Ana Beatriz', 333431, 'Cardiologist')
exame01 = Exam(medico, paciente, 'COVID-19', 'Negative')  
exame01.print_exam()	
