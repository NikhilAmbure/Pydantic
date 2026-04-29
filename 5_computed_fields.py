from pydantic import BaseModel, EmailStr, computed_field
from typing import List, Dict, Optional, Annotated

class Patient(BaseModel):
    
    name: str
    email: EmailStr 
    age: int
    weight: float
    height: float
    married: bool
    contact_details: Dict[str, str]
    allergies: List[str] = None

    @computed_field
    @property
    def bmi(self) -> float:
        bmi = self.weight / (self.height ** 2)
        return round(bmi, 2)


def insert_into_db(patient: Patient):

    print(patient.name)
    print(patient.age)
    print(patient.allergies)
    print('inserted')

def update_into_db(patient: Patient):
    print(patient.name)
    print(patient.age)
    print(patient.bmi) # Accessing the computed field
    print('updated')

patient_info = {'name': "Nitesh", 'email': 'asdajb@hdfc.com', 'age': 30, 'weight': 54.2, 'height': 1.75, 'married': True, 'contact_details': {'email': 'asddabj@gmail.com', 'phone': '218312418'}} # Raw input

patient1 = Patient(**patient_info) # validation => type coercion (performs automatically here)**

insert_into_db(patient1)
update_into_db(patient1)