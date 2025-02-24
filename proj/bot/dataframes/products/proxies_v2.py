import requests
import aiohttp
from bs4 import BeautifulSoup as bs
import asyncio

proxy_list = []
fine_proxies = []

def collect_proxies():
    url = "https://www.proxynova.com/proxy-server-list/country-ru"
    response = requests.get(url=url)
    soup = bs(response.text, "lxml")
    proxy_table = soup.find("table", id="tbl_proxy_list").find("tbody")
    proxies = proxy_table.find_all("tr")
    for proxy in proxies:
        for column in proxy.find_all("td"):
            print(column)

async def check_proxy(proxy):
    async with aiohttp.ClientSession() as session:
        try:
            async with session.get(url="https://google.com", proxy=f"http://{proxy}") as response:
                status_code = response.status
                if status_code == 200:
                    print(f"[INFO] {proxy} | {status_code}")
                    fine_proxies.append(proxy)
        except Exception as e:
            print(f"[INFO][ERROR] {proxy} | {e}")
            pass

async def gather_data():
    tasks = []
    with open("proxies.txt", "r") as file:
        proxies = [proxy.strip() for proxy in file.readlines()]
        for proxy in proxies:
            task = asyncio.create_task(check_proxy(proxy))
            tasks.append(task)
    await asyncio.gather(*tasks)

def main():
    collect_proxies()
    gather_data()

if __name__ == "__main__":
    main()
