import requests

from fake_useragent import UserAgent
from bs4 import BeautifulSoup

ua = UserAgent()

response = requests.get(
    "https://pacathletics.org/stats.aspx",
    headers={"User-Agent": ua.chrome},
    params={"path": "baseball", "year": 2025},
)

soup = BeautifulSoup(response.text, "html.parser")
table = soup.select("#ind_hitting .sidearm-table .sidearm-primary")[0]
columns = table.find_all(lambda tag: tag.has_attr("scope") and tag["scope"] == "col")  # type: ignore

for column in columns:
    print(column.text)
