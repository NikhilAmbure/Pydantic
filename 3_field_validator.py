from pydantic import BaseModel, EmailStr,field_validator
from typing import List, Dict

class Patient(BaseModel):
    
    name: str
    email: EmailStr 
    age: int
    weight: float
    married: bool
    contact_details: Dict[str, str]
    allergies: List[str] = None

    # Usecase-1
    @field_validator('email')
    @classmethod
    def email_validator(cls, value): # class, value

        valid_domains = ['hdfc.com', 'icici.com']
        # basb@gmail.com
        domain_name = value.split('@')[-1]

        if domain_name not in valid_domains:
            raise ValueError('Not a valid domain')
        
        return value
    
    # Usecase-2
    @field_validator('name', mode='after')
    @classmethod
    def transform_name(cls, value):
        return value.upper()
    
    # Mode : before
    # @field_validator('age', mode='before')
    @field_validator('age', mode='after')
    @classmethod
    def validate_age(cls, value): 
        """  Here, we passed the 'age': '30' into the object so it will get the age in str format """
        """  PROBLEM: Will throw the error (bc, it gets the value before the type coercion occurs when we are passing
             the dictionary to the object) i.e. patient1 = Patient(patient_info)"""
        """  SOLUTION : To overcome this -> set mode = "after" """
        if 0 < value < 100:
            return value
        else:
            raise ValueError("Age should be between 0 - 100")


def insert_into_db(patient: Patient):

    print(patient.name)
    print(patient.age)
    print(patient.allergies)
    print('inserted')

def update_into_db(patient: Patient):
    print(patient.name)
    print(patient.age)
    print('updated')

patient_info = {'name': "Nitesh", 'email': 'asdajb@hdfc.com', 'age': 30, 'weight': 54.2, 'married': True, 'contact_details': {'email': 'asddabj@gmail.com', 'phone': '218312418'}} # Raw input

patient1 = Patient(**patient_info) # validation => type coercion (performs automatically here)**

insert_into_db(patient1)
update_into_db(patient1)