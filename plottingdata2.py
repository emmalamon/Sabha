import matplotlib.pyplot as plt
import pandas as pd


file_path = 'cleandata2.csv'
data = pd.read_csv(file_path, na_values=['no data'], encoding= 'utf-8')

df = pd.DataFrame(data)

X = list(df.iloc[:,2])
Y = list(df.iloc[:,3])

plt.bar(X, Y, color='b') 
plt.title("Sleep hours in relation to attendance ") 
plt.xlabel("Sleep hours") 
plt.ylabel("Attendance(%)") 
  
# Show the plot 
plt.show()


X = list(df.iloc[:,1])
Y = list(df.iloc[:,4])

plt.scatter(X, Y, color='g') 
plt.title("Study hours in relation to grades") 
plt.xlabel("Study hours") 
plt.ylabel("Grades") 
plt.show()

