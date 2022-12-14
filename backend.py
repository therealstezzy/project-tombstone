import pandas as pd

class Person():
    def __init__(self, name, dob, dod, des) -> None:
        self.fullName = name
        self.dob = dob
        self.dod = dod
        self.description = des
    
    def getDescription(self):
        return self.description
        

    
data = [10,20,30,40,50,60]
df = pd.DataFrame(data, columns=['Numbers'])

print(df)
