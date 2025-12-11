import pandas as pd
import os, glob, re

def getHeaders(path, csvname): 
    df = pd.read_csv(path, header = None, on_bad_lines="skip") #make pandas data frame
    print("YEAR" + csvname[0])

    #df is [column][row] so doing df[0] gives the first COLUMN. 
    #first two rows are what matters. 
    #df.loc[1,:] -> get all columns for row 1 
    header_row0 = df.iloc[0]
    header_row1 = df.iloc[1]
    header_row2 = df.iloc[2] #do i still need u
    
    #get democratic
    dem_cols = df.columns[df.iloc[0] == "Democratic"] #please work

    #get republican
    rep_cols = df.columns[df.iloc[0] == "Republican"]

    df = df.iloc[3:]  #i forget is this needed sitll...
    df = df.dropna(how="all")  #drop blank garbage row
    
    clean_df = pd.DataFrame()
    clean_df["state"] = df[0]
    clean_df["total_votes"] = df[1]

    clean_df["dem_votes"] = df[dem_cols[0]] #votes
    clean_df["dem_pct"] = df[dem_cols[1]] #percent
    clean_df["dem_ev"] = df[dem_cols[2]] #electroal vote

    clean_df["rep_votes"] = df[rep_cols[0]]
    clean_df["rep_pct"] = df[rep_cols[1]]
    clean_df["rep_ev"] = df[rep_cols[2]]
    
    clean_df["year"] = csvname[0]

    clean_df["dem_pct"] = clean_df["dem_pct"].astype(str).str.replace("%", "").astype(float) #because theres fucking percents because it hatesme
    clean_df["rep_pct"] = clean_df["rep_pct"].astype(str).str.replace("%", "").astype(float)

    clean_df = clean_df[clean_df["state"] != "Totals"]  #remove Totals row

    print(clean_df)
    clean_df.to_csv("states/"+csvname[0] +".csv", index=False)


directory = "each_year_states"
for filename in os.listdir(directory):
    if filename.endswith(".csv"):
        getHeaders(directory + '/' + filename, re.findall(r'_(.{4})_', filename))
