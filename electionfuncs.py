import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def getCandWithName(name, s):
    # name: desired name
    # s: series with all possible names
    # returns dataframe with candidate(s) who have name within their full name
    
    # get name parts and make upper case
    nameParts = name.upper().split(' ')
    
    # for each name, generate series of matching names
    matches = []
    for subname in nameParts:
        namesBool = s['Name'].str.contains(subname)
        # print(s[namesBool].index)
        matches.append(set(s[namesBool].index))
    
    intersectingSet = list(set.intersection(*matches))
    
    return s.loc[intersectingSet]
    
    
def get(cand, allcands, quant='Total Receipts'):
    # cand: last name or list of last names
    # infotype: quantitative info desired (total receipts, from pacs, etc)
    # returns desired quantity: single value if only one matching name, numpy list if multiple
    
    desQuant = getCandWithName(cand, allcands)[quant].values
    
    if len(desQuant) == 1:
        return desQuant[0]
    else:
        return desQuant
    
if __name__ == '__main__':
    print("No tests to perform.")
    