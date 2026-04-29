from pydantic import BaseModel, EmailStr, AnyUrl, Field
from typing import List, Dict, Optional, Annotated

# Field :
# 1. Custom Data validation
# 2. Meta data attachment with following Field + Annotated
# Field + Annotated : To add title, description,... of the field
# 3. Can set default values too


# Type Validation
# Data Validation

# Pydantic model
class Patient(BaseModel):
    
    # Step-1 : Define schema

    # Required fields -> By default all are required fields
    name: Annotated[str, Field(max_length=50, title='name of the patient', desciption="Give the name of the patient")]
    email: EmailStr # Validate the email [data validation] Custom datatype: way-1
    linkedIn_url: AnyUrl # Data Validation : way-1
    age: int = Field(gt=0, lt=100) # Custom data validation : way-2 (Field)
    weight: Annotated[float, Field(gt=0, strict=True)] # Custom data validation : way-2 (Field)
    married: Annotated[bool, Field(default=None, description="Is a patient married or not")]
    contact_details: Dict[str, str]

    # optional fields
    allergies: Annotated[Optional[List[str]], Field(default=None, max_length=5)] # Custom data validation: way-2 (Field)
    # Add any new fields here

def insert_into_db(patient: Patient):
    print(patient.name)
    print(patient.age)
    print(patient.allergies)
    print('inserted')

def update_into_db(patient: Patient):
    print(patient.name)
    print(patient.age)
    print('updated')

# Step-2: Object
# patient_info = {'name': "Nitesh", 'age': 30, 'weight': 54.2, 'married': True, 'allergies': ['pollen', 'dust'],'contact_details': {'email': 'asddabj@gmail.com', 'phone': '218312418'}} # Raw input

# patient_info = {'name': "Nitesh", 'age': 30, 'weight': 54.2, 'married': True, 'contact_details': {'email': 'asddabj@gmail.com', 'phone': '218312418'}} # Raw input

patient_info = {'name': "Nitesh", 'email': 'asdajb@gmail.com', 'linkedIn_url': 'http://linkedin.com//12312','age': 30, 'weight': 54.2, 'married': True, 'contact_details': {'email': 'asddabj@gmail.com', 'phone': '218312418'}} # Raw input

# patient_info = {'name': "Nitesh", 'age': '30'} # Here it will convert the age into int 
patient1 = Patient(**patient_info)

# Step-3: Call the function
insert_into_db(patient1)
update_into_db(patient1)