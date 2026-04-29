from pydantic import BaseModel, EmailStr, model_validator
from typing import List, Dict

class Patient(BaseModel):
    
    name: str
    email: EmailStr 
    age: int
    weight: float
    married: bool
    contact_details: Dict[str, str]
    allergies: List[str] = None

    @model_validator(mode='after')
    def validate_emergency_contact(cls, model):
        if model.age > 60 and 'emergency' not in model.contact_details:
            raise ValueError('Patients older than 60 must have contact')
        return model


def insert_into_db(patient: Patient):

    print(patient.name)
    print(patient.age)
    print(patient.allergies)
    print('inserted')

def update_into_db(patient: Patient):
    print(patient.name)
    print(patient.age)
    print('updated')

patient_info = {'name': "Nitesh", 'email': 'asdajb@hdfc.com', 'age': 65, 'weight': 54.2, 'married': True, 'contact_details': {'email': 'asddabj@gmail.com', 'phone': '218312418', 'emergency': '12863182'}} # Raw input

patient1 = Patient(**patient_info) # validation => type coercion (performs automatically here)**

insert_into_db(patient1)
update_into_db(patient1)