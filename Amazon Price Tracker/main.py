from bs4 import BeautifulSoup
import requests,smtplib,creds
from email.mime.text import MIMEText


headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/143.0.0.0 Safari/537.36",
    "Accept-Language": "en-US,en;q=0.9",
}
response = requests.get(url="https://www.amazon.in/Instant-Pot-Duo-Mini-Programmable/dp/B06Y1YD5W7/ref=sr_1_4?nsdOptOutParam=true&sr=8-4",headers=headers)
webpage = response.text

soup = BeautifulSoup(webpage, "html.parser")
price_whole = soup.find("span", class_="a-price-whole")
price_fraction = soup.find("span", class_="a-price-fraction")

if price_whole and price_fraction:
    price_str = price_whole.text + price_fraction.text
    pot_price = float(price_str.replace("$", "").replace(",", "").strip())
else:
    print("❌ Price not found. Amazon may have blocked the request.")
    pot_price = None
    exit(0)
print(pot_price)
product_info = soup.find("span",id="productTitle").text
product_link = "https://www.amazon.com/dp/B075CYMYK6"
target_price = 10000.00
product_info = " ".join(product_info.split())
print(product_info)

body = (
    f"{product_info} is now ${pot_price}\n"
    f"Here is the link: {product_link}"
)

msg = MIMEText(body, "plain", "utf-8")
msg["Subject"] = "Amazon Price Alert!"
msg["From"] = creds.email
msg["To"] = "madhukiran.golla.personal@gmail.com"

if pot_price < target_price:
    # send email
    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        connection.starttls()
        connection.login(creds.email, creds.password)
        connection.sendmail(from_addr=creds.email,
                            to_addrs="madhukiran.golla.personal@gmail.com",
                            msg=msg.as_string())