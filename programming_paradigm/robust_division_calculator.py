#Script which contains the division logic including error handling
def safe_divide(numerator, denominator):
    try:
        # Convert inputs to float
        num = float(numerator)
        denom = float(denominator)
        
        # Perform division and handle division by zero
        if denom == 0:
            return "Error: Cannot divide by zero."
        
        result = num / denom
        return f"The result of the division is {result}"
    
    except ValueError:
        # Handle non-numeric inputs
        return "Error: Please enter numeric values only."