from typing import List, Tuple, Dict, Union

# A list of integers
num: List[int] = [1, 2, 3, 4, 5]

# A tuple containing a string and an integer
person: Tuple[str, int] = ("Fahmid", 24)

# A dictionary with string keys and integer values
Result: Dict[str, int] = {"Fahmid": 80, "Fahmel": 89}

# A union that can be either an integer or a string
identifier: Union[int, str] = "FAHMID404"

print("Numbers: ", num)
print("Person: ", person)
print("Result: ", Result)
print("Identifier: ", identifier)


# These annotations help in making the code self-documenting and allow developers to understand the data structures used at a glance.