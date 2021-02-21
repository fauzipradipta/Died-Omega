#Fever, Shortness of breath, loss of taste, Sore throat
#underlying illness, age, 

import pandas as pd
import random
from datetime import datetime
from faker import Faker
from faker.providers import BaseProvider

fake = Faker()

# This custom Provider inherits from the BaseProviderr
class Provider(BaseProvider):

    # You can change these values as needed.
    Fever = [0,1]    
    Shortness_of_breath = [0,1]
    loss_of_taste = [0,1]    
    sore_throat = [0,1]    
    underlying_illness = [0,1]

    def fever(self):
        return random.choice(self.Fever)

    def ShortnessofBreath(self):
        return random.choice(self.Shortness_of_breath)

    def LossofTaste(self):
        return random.choice(self.loss_of_taste)

    def SoreThroat(self):
        return random.choice(self.sore_throat)

    def underlying(self):
        return random.choice(self.underlying_illness)

    def age(self):
        return random.randint(5, 100)
# Add the Provider to our faker object
fake.add_provider(Provider)

def create_fake_data(fake, no_of_rows):
    columns = ['age', 'underlying', 'fever', 'ShortnessofBreath', 'LossofTaste', 'SoreThroat']
    data = {column: [getattr(fake, column)() for _ in range(no_of_rows)] for column in columns}
    df = pd.DataFrame(data=data)
    df = df[columns]
    return df

df = create_fake_data(fake, 1000)
print(df)
