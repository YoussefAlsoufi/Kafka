# Data which the producer wants to publish:

from faker import Faker

fake = Faker()
    
def registered_user():
    return{
        "name" : fake.name(),
        "address": fake.address(),
        "pulished_at": fake.year()
        }

print(registered_user())