import csv
import pandas as pd
import fetcher as fc
import accesion as ac
#Accession ID must pulled from fethOneInfo in order to loop through url's



def main():
    names = fc.fetcher()
    items = ac.accesion()
    columns = ['Bacteriophage Name', 'Accession ID', 'Articles']
    
    data = { 'Bacteriophage Name': names, 'Accession ID': items, 'Articles': ['ID Placeholder'] * len(items) }
    
    df = pd.DataFrame(data, columns=columns) 
    df.to_csv('table3.csv', index=False)
            
if __name__ == "__main__":
    main()
