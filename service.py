
from dao import save_data

def get_addition(n1, n2):
    print("---Service Layer : Adding Numbers---")
    addition = n1 + n2
    # Save to database
    resp = save_data(n1, n2, addition)
    return addition
