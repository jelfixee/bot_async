import requests
import aiohttp
from bs4 import BeautifulSoup as bs
import asyncio

proxy_list = []
fine_proxies = []

def collect_proxies():
    headers = {
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
        'cache-control': 'no-cache',
        'content-type': 'application/x-www-form-urlencoded',
        'origin': 'https://www.iplocation.net',
        'priority': 'u=0, i',
        'referer': 'https://www.iplocation.net/proxy-list',
        'sec-ch-ua': '"Not(A:Brand";v="99", "Google Chrome";v="133", "Chromium";v="133"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'document',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-user': '?1',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Safari/537.36'
    }

    data = {
        'http': '1',
        'https': '1',
        'country[]': 'RU',
        'ports[]': 'any',
        'submit': 'Search',
    }

    response = requests.post('https://www.iplocation.net/proxy-list', headers=headers, data=data)
    soup = bs(response.text, "lxml")
    table = soup.find("div", class_="table-responsive").find("table").find("tbody").find_all("tr")
    for proxy in table:
        proxy_ip, proxy_port = [td.text for td in proxy.find_all("td")][:2]
        proxy_list.append(f"{proxy_ip}:{proxy_port}")

async def check_proxy(proxy):
    async with aiohttp.ClientSession() as session:
        try:
            async with session.get(url="https://google.com", proxy=f"https://{proxy}") as response:
                status_code = response.status
                if status_code == 200:
                    print(f"[INFO] {proxy} | {status_code}")
                    fine_proxies.append(proxy)
        except Exception as e:
            print(f"[INFO][ERROR] {proxy} | {e}")
            pass

async def gather_data():
    tasks = []
    for proxy in proxy_list:
        task = asyncio.create_task(check_proxy(proxy))
        tasks.append(task)
    await asyncio.gather(*tasks)

def main():
    collect_proxies()
    asyncio.run(gather_data())

if __name__ == "__main__":
    main()
