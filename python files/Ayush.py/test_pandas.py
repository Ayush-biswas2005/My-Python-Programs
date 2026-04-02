import pandas as pd

std_data=[(1, 'varun', 30, 'male', 'chandigarh'),(2, 'ravi', 31, 'male', 'delhi'),(3,'preeti', 29, 'female', 'jaipur'),(4,'amrit', 32, 'male', 'mumbai'),(5, 'pinki', 28, 'female', 'banglore')]

df=pd.DataFrame (std_data, columns=['stud_id', 'name', 'age', 'gender', 'adress'])

print(df)