#Create DataFrame from dictionary & rename columns
import pandas as pd
data={'name':['Ayush','Ayush','Ayush'],
      'age':[20,21,22],
      'city':['Delhi','Mumbai','Kolkata']}
df=pd.DataFrame(data)
df.rename(columns={'name':'Name','age':'Age','city':'City'},inplace=True)
print(df)