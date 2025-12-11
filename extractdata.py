#extract data from link 
import pandas as pd
year = 2024 #define year variable 


'''
while (year >= 1916): 
    print("get data for year" + str(year))
    url = "https://www.presidency.ucsb.edu/statistics/elections/"+str(year)
    df = pd.read_html(url)[0]
    df.to_csv("election_"+str(year)+"_states.csv", index=False)
    year= int(year)-4
'''
year = 1976
url = "https://www.presidency.ucsb.edu/statistics/elections/"+str(year)
df = pd.read_html(url)[0]
df.to_csv("election_"+str(year)+"_states.csv", index=False)