import pycountry_convert as pc
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

AF=0
NA=0
OC=0
AN=0
AS=0
EU=0
SA=0

Cup=0
Pack=0
Tray=0
Bowl=0
Box=0
Can=0
Bar=0

raw_dataframe = pd.read_csv("ramen-ratings.csv")
print(raw_dataframe.head())
print(raw_dataframe.info())

print("\nCount of NaN data in every column:")
print(raw_dataframe.isna().sum())


def dropCols(df):
    df = df.drop("Review #",axis=1)
    df = df.drop("Top Ten",axis=1)
    return df

def edit_dataframe(df):
    df = dropCols(df)
    return df
def CountContinent(cc):
    global AF, NA, OC, AN, AS, EU, SA
    
    
    if (cc=="AF"):
        AF+=1
    elif (cc=="NA"):
        NA+=1
    elif(cc=="OC"):
        OC+=1
    elif(cc=="AN"):
        AN+=1
    elif(cc=="AS"):
        AS+=1
    elif(cc=="EU"):
        EU+=1
    elif(cc=="SA"):
        SA+=1
    else:
        None
        
def CountStyles(st):
    global Cup, Pack, Tray, Bowl, Box, Can, Bar, Other
    
    if (st=="Cup"):
        Cup+=1
    elif (st=="Pack"):
        Pack+=1
    elif(st=="Tray"):
        Tray+=1
    elif(st=="Bowl"):
        Bowl+=1
    elif(st=="Box"):
        Box+=1
    elif(st=="Can"):
        Can+=1
    elif(st=="Bar"):
        Bar+=1
    else:
        None


new_data = edit_dataframe(raw_dataframe)
print(new_data.head())
print(new_data.info())


country_names = np.array(new_data.Country.unique())
new_data["Continent"] = None
for i in range(len(country_names)):
    country_code = pc.country_name_to_country_alpha2(country_names[i], cn_name_format="default")
    continent_code = pc.country_alpha2_to_continent_code(country_code)
    CountContinent(continent_code)
    
Cont_list=[AF, NA, OC, AN, AS, EU, SA]

plt.ylim(0,20)
y = Cont_list
x = ["Africa", "North America", "Oceania", "Antartica", "Asia", "Europe", "South America"]      
plt.bar(x, y)
plt.xticks(rotation=45)
plt.title('Global Manufacturing of Ramen Noodles')
plt.xlabel('Continents') 
plt.ylabel('No. of Manufacturing Countries')
plt.show()

print("\nUnique Styles: ")
print(new_data.Style.unique())

for i in new_data.Style:
    CountStyles(i)

y = [Cup, Can, Pack, Tray, Box, Bowl, Bar]
x = ["Cup", "Can", "Pack", "Tray", "Box", "Bowl", "Bar"]      
plt.pie(y, labels=x, shadow=True,startangle=90, autopct="%1.1f%%")
plt.title('Popularity of Various Packaging Styles')
plt.show()

for i in y:
    print("Percentage of ", i , "=", (i/np.sum(y))*100)












