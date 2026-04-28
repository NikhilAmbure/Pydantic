# 1. Type Validation Problem
# 2. Data Validation Problem

# def insert_into_db(name: str, age: int):
    # print(f"Inserting {name} with age {age} into the database.")

# insert_into_db("Alice", "30") # It will still work : Problem


# Solution : But not scalable
def insert_into_db(name: str, age: int):
    if type(name) == str and type(age) == int:
        if age < 0:
            raise ValueError("Age cant be neg.")
        else:
            print(f"Inserting {name} with age {age} into the database.")
    else:
        raise TypeError("Incorrect type")

insert_into_db("Alice", 30)
