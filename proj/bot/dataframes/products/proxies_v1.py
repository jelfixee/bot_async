import requests
import aiohttp
import asyncio
from bs4 import BeautifulSoup as bs

proxy_list = []
fine_proxies = []

def collect_proxies():

    url_p = "https://proxylist.geonode.com/api/proxy-list?protocols=http%2Chttps&limit=500&page=1&sort_by=lastChecked&sort_type=desc"

    headers = {
        'accept': '*/*',
        'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
        'content-type': 'application/x-www-form-urlencoded',
        'origin': 'https://geonode.com',
        'priority': 'u=1, i',
        'referer': 'https://geonode.com/',
        'sec-ch-ua': '"Not(A:Brand";v="99", "Google Chrome";v="133", "Chromium";v="133"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'cross-site',
        'sec-fetch-storage-access': 'active',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Safari/537.36',
    }

    flag = True
    with requests.Session() as session:
        req = session.get(url=url_p, headers=headers)
        if req.status_code == 200:
            json = req.json()
            proxies = json["data"]
            for proxy in proxies:
                ip = proxy["ip"]
                port = proxy["port"]
                print(f"[INFO][HANDLED] {ip}:{port}")
                proxy_list.append(f"{ip}:{port}")
            return flag
        else:
            flag = False
            print("TRY AGAIN")
            return flag

def t_2ip(proxy):
    url = "https://2ip.ru/"

    headers = {
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
        'cache-control': 'no-cache',
        'priority': 'u=0, i',
        'sec-ch-ua': '"Not(A:Brand";v="99", "Google Chrome";v="133", "Chromium";v="133"',
        'sec-ch-ua-arch': '"x86"',
        'sec-ch-ua-full-version-list': '"Not(A:Brand";v="99.0.0.0", "Google Chrome";v="133.0.6943.127", "Chromium";v="133.0.6943.127"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-ch-ua-platform-version': '"10.0.0"',
        'sec-fetch-dest': 'document',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'cross-site',
        'sec-fetch-user': '?1',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Safari/537.36'
    }

    proxy_dict = {
        "http": f"http://{proxy}",
        "https": f"http://{proxy}"
    }

    response = requests.get(url=url, headers=headers, proxies=proxy_dict)
    soup = bs(response.text, "lxml")
    ip = soup.find("div", class_="ip").text
    print(ip)

# async def check_proxy(proxy):
#     async with aiohttp.ClientSession(trust_env=True, connector=aiohttp.TCPConnector(limit=0)) as session:
#         try:
#             async with session.get(url="https://google.com", proxy=f"http://{proxy}") as response:
#                 status_code = response.status
#                 if status_code == 200:
#                     print(f"[INFO]~[SUCCESS] {proxy} | {status_code}")
#                     t_2ip(proxy)
#                     fine_proxies.append(proxy)
#         except Exception as e:
#             print(f"[INFO]![ERROR] {proxy} | {e}")
#             pass

async def check_proxy_(proxy):
    async with aiohttp.ClientSession(trust_env=True, connector=aiohttp.TCPConnector(limit=0)) as session:
        try:
            async with session.get(url="https://google.com", proxy=f"http://{proxy}") as response:
                status_code = response.status
                if status_code == 200:
                    print(f"[INFO]~[SUCCESS] {proxy} | {status_code}")
                    return proxy
        except Exception as e:
            print(f"[INFO]![ERROR] {proxy} | {e}")
            pass

async def gather_data():
    tasks = []
    for proxy in proxy_list:
        task = asyncio.create_task(check_proxy_(proxy)) # DON'T FORGET TO CHANGE THE METHOD
        tasks.append(task)
    await asyncio.gather(*tasks)

def get_proxy():
    if collect_proxies():
        print("[COLLECTING PROXIES]")
        asyncio.run(gather_data())


if __name__ == "__main__":
    get_proxy()
    print("END")
