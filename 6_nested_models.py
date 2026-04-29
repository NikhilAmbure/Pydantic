from pydantic import BaseModel

class Address(BaseModel):

    city: str
    state: str
    pincode: str

class Patient(BaseModel):

    name: str
    gender: str
    age: int
    address: Address # nested model

address_dict = {'city': 'pune', 'state': "MH", 'pincode': '141221'}
address1 = Address(**address_dict)

patient_dict = {'name': 'Nick', 'gender': 'male', 'age': 22, 'address': address1}
patient1 = Patient(**patient_dict)

print(patient1)
print(patient1.address.city)


# Better organization of related data (e.g. vitals, address, insurance)

# Reusability: Use vitals in multiple models (e.g. Patient, MedicalRecord)

# Readability: Easier for developers and API consumers to understand

# Validation : Nested Models are validated automatically - no extra work needed