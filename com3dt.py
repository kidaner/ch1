import pandas as pd

xls = pd.ExcelFile("NUCAMP.xlx")

camps = xls.sheet_names

listings = []

for camp in camps:
    listing = pd.read_excel(xls, sheet_name=camp)

    listing["camp"] = camps

    listings.append(listing)

combined_listings = pd.concat(listings)
