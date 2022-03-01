import pandas as pd

xls = pd.ExcelFile("NUCAMP.xlx")

camps = xls.sheet_names

listings = []

for camp in camps:
    listing = pd.read_excel(xls, sheet_name=camp)

    listing["camp"] = camps

    listings.append(listing)

combined_listings = pd.concat(listings)

# Import the NYSE and NASDAQ listings
nyse = pd.read_excel('listings.xlsx', sheet_name='nyse', na_values='n/a')
nasdaq = pd.read_excel('listings.xlsx', sheet_name='nasdaq', na_values='n/a')

# Inspect nyse and nasdaq
nyse.info()
nasdaq.info()

# Add Exchange reference columns
nyse['Exchange'] = 'NYSE'
nasdaq['Exchange'] = 'NASDAQ'

# Concatenate DataFrames
combined_listings = pd.concat([nyse, nasdaq])
