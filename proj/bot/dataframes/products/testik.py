import requests
import aiohttp
import asyncio

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
            with open("proxies.txt", "w") as file:
                for proxy in proxies:
                    ip = proxy["ip"]
                    port = proxy["port"]
                    print(f"[INFO][HANDLED] {ip}:{port}")
                    file.write(f"{ip}:{port}\n")
            return flag
        else:
            flag = False
            print("TRY AGAIN")
            return flag

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
    if collect_proxies():
        print("COLLECTING PROXIES")
        asyncio.run(gather_data())
        with open("proxies.txt", "w") as file:
            for proxy in fine_proxies:
                file.write(proxy)

if __name__ == "__main__":
    main()
    print("END")

# headers_l = {
#     'Accept': '*/*',
#     'Accept-Language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
#     'Connection': 'keep-alive',
#     'Content-Type': 'text/plain;charset=UTF-8',
#     'Origin': 'https://lenta.com',
#     'Referer': 'https://lenta.com/',
#     'Sec-Fetch-Dest': 'empty',
#     'Sec-Fetch-Mode': 'cors',
#     'Sec-Fetch-Site': 'cross-site',
#     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Safari/537.36',
#     'sec-ch-ua': '"Not(A:Brand";v="99", "Google Chrome";v="133", "Chromium";v="133"',
#     'sec-ch-ua-mobile': '?0',
#     'sec-ch-ua-platform': '"Windows"',
# }
#
# url_l = "https://lenta.com/"
#
#
# def get_proxies():
#     with requests.Session() as session:
#         req = session.get(url=url_p, headers=headers_p)
#         if req.status_code == 200:
#             json = req.json()
#             proxies = json["data"]
#             for proxy in proxies:
#                 ip = proxy["ip"]
#                 port = proxy["port"]
#                 with open("proxies.txt", "w") as file:
#                     file.write(f"{ip}:{port}")
#         else:
#             print("TRY AGAIN")
#
# async def fetch(proxy):
#     # print(proxy)
#     pr = f"http://{proxy}"
#     try:
#         async with aiohttp.ClientSession() as ses:
#             req = await ses.get(url=url_l, proxy=pr, headers=headers_l)
#             print()
#             print(proxy, req)
#             print()
#     except Exception as e:
#         print(f"[ERROR] {proxy} |", e)
#
# async def gather_data():
#     with open("proxies.txt", "r") as file:
#         proxies = [line.strip() for line in file.readlines()]
#     tasks = []
#     for proxy in proxies:
#         task = asyncio.create_task(fetch(proxy))
#         tasks.append(task)
#
#     await asyncio.gather(*tasks)
#
# def main():
#     get_proxies()
#     asyncio.run(gather_data())
#
# if __name__ == "__main__":
#     main()

# #
# # # headers_m = {
# # #     'accept': '*/*',
# # #     'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
# # #     'content-type': 'application/x-www-form-urlencoded',
# # #     'origin': 'https://magnit.ru',
# # #     'priority': 'u=1, i',
# # #     'referer': 'https://magnit.ru/',
# # #     'sec-ch-ua': '"Not(A:Brand";v="99", "Google Chrome";v="133", "Chromium";v="133"',
# # #     'sec-ch-ua-mobile': '?0',
# # #     'sec-ch-ua-platform': '"Windows"',
# # #     'sec-fetch-dest': 'empty',
# # #     'sec-fetch-mode': 'cors',
# # #     'sec-fetch-site': 'cross-site',
# # #     'sec-fetch-storage-access': 'active',
# # #     'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Safari/537.36'
# # # }
# #
# # # url = "https://magnit.ru/"
#
#
# with open("proxies.txt", "r") as file:
#     proxies = [line.strip() for line in file.readlines()]
#
# for proxy in proxies:
#     try:
#         response = requests.get(url=f"http://{proxy}", verify=False)
#         response.raise_for_status()
#         print(response.text)
#     except Exception as e:
#         print(proxy, "|", e)
#
# pr = {
#     "http": "http://212.69.125.33:80",
#     "https": "http://212.69.125.33:80",
# }
#
# req = requests.get(url="https://lenta.com", proxies=pr).text
#
# print(req)
