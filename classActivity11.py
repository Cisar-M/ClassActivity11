import pandas as pd
import matplotlib.pyplot as plt 
import numpy as np
# 1. Read in information
titanic = pd.read_csv("titanic.csv")
print(titanic)

# 2. Calculate the fare as a percentage compared to the sum total of all fairs
Total = titanic['fare'].sum()
print(Total)

titanic["FareAsPercentage"] = titanic["fare"]/Total*100
print("Added columns")
print(titanic)


# 3. Subsets for male and female
female = titanic[titanic.sex == "female"]
print(female) 

male = titanic[titanic.sex == "male"]
print(male)

# 4. correlation
corr = female["age"].corr(female["survived"])
print("4. The correlation coefficient is: ")
print(corr)

# 5. Data visualisation
plt.bar("Female", np.mean(female["survived"]*10))
plt.bar("Male", np.mean(male["survived"]*10))


plt.xlabel("Gender")
plt.ylabel("Survive")
plt.title("Compare survival rate between genders out of 10")
plt.show()




 






