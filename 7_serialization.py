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


# Automatically converts the pydantic model into dictionary
temp = patient1.model_dump()
temp2 = patient1.model_dump_json()

specific_field = patient1.model_dump(include=['name'])
specific_field2 = patient1.model_dump(exclude=['name'])
nested_field = patient1.model_dump(exclude={'address': ['state']})
# Simly, for the model_dump_json()
print(temp)
print(type(temp)) 