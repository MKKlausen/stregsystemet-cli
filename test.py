import string
import urllib3
import requests
from html.parser import HTMLParser

url = "Insert Rank URL"

response = requests.get(url, verify=False)

stringconversion = response.content.decode('UTF-8')

split = stringconversion.split("<tr class=\"ranking\">")

ranknames = (split[1].replace("\n", "").replace(" ", "").replace("<th>", "").replace("<thclass=\"ranking\"", "")).split("</th>>")
ranktotal = (split[2].replace("\n", "").replace(" ", "").replace("<td>", "").replace("<tdclass=\"ranking\"", "")).split("</td>>")
rankunits = (split[3].replace("\n", "").replace(" ", "").replace("<td>", "").replace("<tdclass=\"ranking\"", "")).split("</td>>")

ranknames[0] = "Kategorier"

stringarray = [[]]
# Print first row
print(f"{ranknames[0]} || {ranktotal[0]} || {rankunits[0]}")
for i in range(len(ranknames)):
    if i == 0:
        print("------------------------------------------")
    else:
        print(f"{ranknames[i]} || {ranktotal[i]} || {rankunits[i]}")

print("debugprint")