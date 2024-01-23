import pandas as pd 
import numpy as np

#Task 1
columns = ['Name', 'Age', 'Gender', 'GPA']
data = [['Toilybay', 18, 'Male', 3.57],
        ['Aruana', 18, 'Female', 3.0],
        ['Adilkhan', 18, 'Male', 3.6],
        ['Almat', 18, 'Male', 3.21],
        ['Aida', 19, 'Female', 3.78]]

df = pd.DataFrame(data, columns=columns)
print(df)

#Task 2
print(df['Name'])

females = df[df['Gender'] == 'Female']
print(females)

top_students = df[max(df['GPA']) == df['GPA']]
print(top_students)

#Task 3
updated_data = df
updated_data['Age'] = updated_data['Age'] + 1
print(updated_data)

youngest_students = df[min(df['Age']) == df['Age']]
new_gpa = youngest_students['GPA'] + 0.3 
youngest_students['GPA'] = np.where(new_gpa > 4.0, 4.0, new_gpa)
print(youngest_students)

#Task 4
new_student = pd.Series(['Nazerke', 19, 'Female', 3.4], index=df.columns)
df = df._append(new_student, ignore_index=True)
print(df)

#Task 5
new_df = df
new_df['GPA'] = new_df['GPA'].apply(lambda x: 4.0 if x + 0.5 > 4.0 else x + 0.5)
print(new_df)

#Task 6
sorted_df = df.sort_values(by='Age', ascending=False)
print(sorted_df)

new_sorted_df = sorted_df.sort_values(by='GPA', ascending=True)
print(new_sorted_df)

#Task 7
new_sorted_df.to_csv('data.csv', index=False)