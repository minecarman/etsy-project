import pandas as pd
from IPython.display import display

etsydata = pd.read_csv('etsy-mens-t-shirts-11-15-2017.csv')
def mostExpensive(data: pd.DataFrame):
    return data.nlargest(1, 'product_price')

print(mostExpensive(etsydata)['url'])