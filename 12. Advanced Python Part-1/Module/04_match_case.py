def Number(number: int) -> str:
    match number:
        case 0:
            return "The number is zero."
        
        case 1:
            return "The number is one."
        
        case n if n > 1 and n % 2 == 0:
            return "The number is a positive even number."
        
        case n if n > 1:
            return "The number is a positive odd number."
        
        case _:
            return "The number is negative."


print(Number(0))  
print(Number(1)) 
print(Number(4))   
print(Number(7))   
print(Number(-3))
