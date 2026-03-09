from bs4 import BeautifulSoup
import pandas as pd

with open("indiamart.html", "r", encoding="utf-8") as file:
    soup = BeautifulSoup(file, "html.parser")

cards = soup.select("div.card.brs5")

print("Total cards found:", len(cards))

Names = []
Prices = []
Mobiles = []
Companies = []
Reviews = []

for card in cards:

    name = card.find("span", class_="elps elps2")
    price = card.find("p", class_="price")
    mobile = card.find("span", class_="fs10")
    company = card.find("div", class_="companyname")
    review = card.find("span", class_="bo color")

   
if name:
    Names.append(name.text.strip())
else:
    Names.append("")

if price:
    Prices.append(price.text.strip())
else:
    Prices.append("")

if mobile:
    Mobiles.append(mobile.text.strip())
else:
    Mobiles.append("")

if company:
    Companies.append(company.text.strip())
else:
    Companies.append("")

if review:
    Reviews.append(review.text.strip())
else:
    Reviews.append("")

df = pd.DataFrame({
    "Names": Names,
    "Prices": Prices,
    "Mobile No": Mobiles,
    "Company Name": Companies,
    "Reviews": Reviews
})

df.to_excel("indiamart_data.xlsx", index=False)

print("Data saved to Excel")