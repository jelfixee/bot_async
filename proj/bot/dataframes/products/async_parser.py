import aiohttp
from bs4 import BeautifulSoup as bs


async def ashan(cat, proxy):
    url = "https://www.auchan.ru/v1/catalog/products?merchantId=1&page=1&perPage=40&orderField=price&orderDirection=asc&deliveryAddressSelected=0"

    json_data = {
        'filter': {
            'category': cat,
            'promo_only': False,
            'active_only': False,
            'cashback_only': False,
        },
    }

    headers = {
        'Accept': 'application/json, text/plain, */*',
        'Accept-Language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
        'Connection': 'keep-alive',
        'Content-Type': 'application/json;charset=UTF-8',
        'Origin': 'https://www.auchan.ru',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36',
        'X-NewRelic-ID': 'undefined',
        'X-Token-CMD': '',
        'newrelic': 'eyJ2IjpbMCwxXSwiZCI6eyJ0eSI6IkJyb3dzZXIiLCJhYyI6IjEwMDAwMDAiLCJhcCI6IjMzMjQxMTMiLCJpZCI6ImEzODE1YmRkYjg5Y2ZiOTkiLCJ0ciI6IjdmZjZmZGY4ZGNmMDhlYzUxZWU5MGQ5ZDY5NzlhNDMwIiwidGkiOjE3Mjk0Mzc3MzkxNzF9fQ==',
        'sec-ch-ua': '"Google Chrome";v="129", "Not=A?Brand";v="8", "Chromium";v="129"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'traceparent': '00-7ff6fdf8dcf08ec51ee90d9d6979a430-a3815bddb89cfb99-01',
        'tracestate': '1000000@nr=0-1-1000000-3324113-a3815bddb89cfb99----1729437739171',
    }

    async with aiohttp.ClientSession() as session:
        async with session.post(url=url,
                                headers=headers,
                                json=json_data,
                                proxy=proxy) as response:
            json_file = await response.json()
            products = json_file["items"]
            product_list = []
            for product in products:
                price = int(float(product["price"]["value"])*100)
                title = product["title"]
                product_list.append([price, title])

    return product_list

async def lenta(cat, proxy):
    headers = {
        'Accept': 'application/json',
        'Accept-Language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7,es;q=0.6,fi;q=0.5',
        'Connection': 'keep-alive',
        'Content-Type': 'application/json',
        'DeviceID': '6416fe53-b312-e964-a230-08288c57684f',
        'Experiments': 'exp_recommendation_cms.false, exp_apigw_purchase.test, exp_lentapay.test, exp_omni_price.test, exp_profile_bell.test, exp_newui_cancel_order.test, exp_newui_history_active_action.test_stars, exp_comment_picker_and_courier.test, exp_general_editing_page.test, exp_cl_omni_support.test, exp_cl_omni_authorization.test, exp_onboarding_sbp.default, exp_fullscreen.test, exp_profile_login.false, exp_new_notifications_show_unauthorized.test, exp_assembly_cost_location.cart, exp_search_bottom.default, exp_onboarding_editing_order.test, exp_cart_new_carousel.default, exp_newui_cart_cancel_editing.test, exp_newui_cart_button.test, exp_new_promov3., exp_sbp_enabled.test, exp_new_my_goods.test, exp_ui_catalog.test, exp_search_out_of_stock.default, exp_profile_settings_email.default, exp_cl_omni_refusalprintreceipts.test, exp_cl_omni_refusalprintcoupons.test, exp_accrual_history.test, exp_personal_recommendations.default, exp_newui_chips.test, exp_loyalty_categories.test, exp_growthbooks_aa.control, exp_test2.true, exp_search_suggestions_popular_sku.default, exp_test3.false',
        'Origin': 'https://lenta.com',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
        'SessionToken': '41D2A2D1F050367D5D7D809D944F565F',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36',
        'X-Delivery-Mode': 'pickup',
        'X-Device-Brand': '',
        'X-Device-ID': '6416fe53-b312-e964-a230-08288c57684f',
        'X-Device-Name': '',
        'X-Device-OS': 'iOS',
        'X-Device-OS-Version': '12.4.8',
        'X-Domain': 'moscow',
        'X-Organization-ID': '',
        'X-Platform': 'omniweb',
        'X-Retail-Brand': 'lo',
        'baggage': 'sentry-environment=production,sentry-release=web-11.0.412,sentry-public_key=b99355c72549498d9e9075cc3d4006a2,sentry-trace_id=fb0cbd7519c3450db011940e7e06781b,sentry-replay_id=ebdff8f20a93421b80903da9a6aa2e9b,sentry-sample_rate=1,sentry-transaction=%2Fcatalog%2F%3AcategoryId%2F,sentry-sampled=true',
        'sec-ch-ua': '"Google Chrome";v="129", "Not=A?Brand";v="8", "Chromium";v="129"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"macOS"',
        'sentry-trace': 'fb0cbd7519c3450db011940e7e06781b-8280b0d41e84f2e8-1',
        'traceparent': '00-eb588ec98004b9a74e1bfe3d34780c2e-7ccd5f56ee0ec55c-01',
        'x-span-id': '7ccd5f56ee0ec55c',
        'x-trace-id': 'eb588ec98004b9a74e1bfe3d34780c2e',
    }

    json_data = {
        'categoryId': cat,
        'limit': 40,
        'offset': 0,
        'sort': {
            'type': 'price',
            'order': 'asc',
        },
        'filters': None,
    }

    async with aiohttp.ClientSession() as session:
        async with session.post(url='https://lenta.com/api-gateway/v1/catalog/items',
                                headers=headers,
                                json=json_data,
                                proxy=proxy) as response:
            product_list = []
            json_file = await response.json()
            products = json_file["items"]
            for product in products:
                price = int(product["prices"]["cost"])
                title = product["name"]
                product_list.append([price, title])
    return product_list

async def magnit(cat, proxy):
    url = "https://magnit.ru/webgate/v2/goods/search"

    cookies = {
        '_ym_uid': '170802001196085177',
        '_ym_d': '1727451571',
        'nmg_udi': '1DEB82A4-B9A9-8789-D233-BF28F102DF9A',
        'x_device_id': '1DEB82A4-B9A9-8789-D233-BF28F102DF9A',
        'mg_uac': '1',
        'cookies-modal': '1',
        'x_shop_type': 'MM',
        'nmg_sp': 'Y',
        'nmg_sid': '161866',
        'shopId': '161866',
        '_ga_MEJT7QPK6J': 'GS1.1.1727799697.1.0.1727799697.60.0.0',
        '_ga': 'GA1.1.393520055.1727451571',
        '_ym_isad': '1',
        '_ga_L0N0B74HJP': 'GS1.1.1729763335.19.0.1729763335.60.0.0',
        '_ym_visorc': 'b',
        'shopCode': '767694',
    }

    headers = {
        'Accept-Language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
        'Connection': 'keep-alive',
        'Origin': 'https://magnit.ru',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36',
        'accept': 'application/json',
        'content-type': 'application/json',
        'sec-ch-ua': '"Chromium";v="130", "Google Chrome";v="130", "Not?A_Brand";v="99"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'x-app-version': '7.0.0',
        'x-client-name': 'magnit',
        'x-device-id': '1DEB82A4-B9A9-8789-D233-BF28F102DF9A',
        'x-device-platform': 'Web',
        'x-device-tag': 'disabled',
        'x-new-magnit': 'true',
        'x-platform-version': 'Windows Chrome 130',
    }

    json_data = {
        'sort': {
            'order': 'asc',
            'type': 'price',
        },
        'pagination': {
            'limit': 33,
            'offset': 0,
        },
        'categories': [
            cat,
        ],
        'includeAdultGoods': True,
        'storeCode': '767694',
        'storeType': '1',
        'catalogType': '1',
    }

    async with aiohttp.ClientSession() as session:
        async with session.post(url=url,
                                cookies=cookies,
                                headers=headers,
                                json=json_data,
                                proxy=proxy) as response:
            product_list = []
            json_file = await response.json()
            products = json_file["items"]
            for product in products:
                price = int(product["price"])
                title = product["name"]
                product_list.append([price, title])
    return product_list

async def metro(cat, proxy):
    headers = {
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
        'cache-control': 'no-cache',
        'priority': 'u=0, i',
        'referer': 'https://online.metro-cc.ru/',
        'sec-fetch-dest': 'document',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-user': '?1',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36',
    }

    async with aiohttp.ClientSession() as session:
        async with session.get(url=cat,
                               headers=headers,
                               proxy=proxy) as response:
            soup = bs(await response.text(), "lxml")
            products = soup.find_all("div", class_="product-card__content")
            product_list = []
            for product in products:
                name = product.find("span", class_="product-card-name__text").text.strip()
                parts = product.find("span", class_="product-price__sum")
                if parts.find("span", class_="product-price__sum-penny"):
                    p1 = parts.find("span", class_="product-price__sum-rubles").text
                    p2 = parts.find("span", class_="product-price__sum-penny").text
                    price = p1 + p2
                    try:
                        int(float(price)*100)
                    except:
                        price = int(float("".join([i for i in price if i.isdigit()]))*100)
                else:
                    price = int(float("".join(i for i in parts.find("span", class_="product-price__sum-rubles").text if i.isdigit()))*100)
                product_list.append([price, name])
    return product_list

async def okei(cat, proxy):

    url = 'https://www.okeydostavka.ru/webapp/wcs/stores/servlet/ProductListingView'

    cookies = {
        'spid': '1728073950007_93e919916f4dea9090b5f133025904ab_m1l1a9k71m19cbck',
        'WC_SESSION_ESTABLISHED': 'true',
        'WC_AUTHENTICATION_-1002': '-1002%2CzZHlyRjQcgWKqNcfDjyX4iZ02zjcQoyDurbFiQxFNVk%3D',
        '_ga': 'GA1.1.1587796706.1728073953',
        '_ym_uid': '1695646725534549903',
        '_ym_d': '1728073953',
        'isNative': '1',
        'storeGroup': 'msk1',
        'ffcId': '13151',
        'WC_USERACTIVITY_-1002': '-1002%2C10151%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2C1877362032%2Cver_null%2CFiV6Js0qKXjqpS4KxY83MRWICuTU2u2kOsV1Y1hiUnW3iqj8SZxy5C3u3zGbIyN1t4qZzE873oOZfb62C88Ygz0VUhifRk5Zp0hz88HCMpha6QP0BQzy0VTpWGVeZYpVmALvEBGGlsRoj6se%2B7Z%2FLNdK1kPC90Rh%2FCZ6bnP74plFG8Hduhay1RZaa4bVBbcgrWYpJeKg76oiyoMkB9naZ0TSJy9kMJ1WmPy%2Bz79LL2FrJhHGcukNV6lWYqn4LAgx',
        'WC_GENERIC_ACTIVITYDATA': '[7462334018%3Atrue%3Afalse%3A0%3AzZ%2BXmMjHypIGu80OmZ8VtA%2Bhc7kTR0C2f0HkIQBKRHE%3D][com.ibm.commerce.context.entitlement.EntitlementContext|4000000000000000003%264000000000000000003%26null%26-2000%26null%26null%26null][com.ibm.commerce.context.audit.AuditContext|null][com.ibm.commerce.context.globalization.GlobalizationContext|-20%26RUB%26-20%26RUB][com.ibm.commerce.store.facade.server.context.StoreGeoCodeContext|null%26null%26null%26null%26null%26null][com.ibm.commerce.catalog.businesscontext.CatalogContext|10551%26null%26false%26false%26false][com.ibm.commerce.context.experiment.ExperimentContext|null][com.ibm.commerce.context.ExternalCartContext|null][com.ibm.commerce.context.bcsversion.BusinessContextVersionContext|null][CTXSETNAME|Store][com.ibm.commerce.context.base.BaseContext|10151%26-1002%26-1002%26-1][com.ibm.commerce.giftcenter.context.GiftCenterContext|null%26null%26null]',
        'selectedCity': '%D0%9C%D0%BE%D1%81%D0%BA%D0%B2%D0%B0',
        '_ym_isad': '1',
        'solarfri': 'ab844f3bb154a5ee',
        'spsc': '1729945573624_fef6519a19ca9c9e20c19e7b6a8be5fe_e6cfb3ea8f0a0fa28cc6ebefdcae8ea5',
        'JSESSIONID': '00002R96-97hD9XcLrtEBK3gzm0:-1',
        'WC_ACTIVEPOINTER': '-20%2C10151',
        'gtmListKey': 'GTM_LIST_CATALOG',
    }

    headers = {
        'accept': '*/*',
        'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
        'content-type': 'application/x-www-form-urlencoded',
        'origin': 'https://www.okeydostavka.ru',
        'priority': 'u=1, i',
        'referer': "https://www.okeydostavka.ru/msk/",
        'sec-ch-ua': '"Chromium";v="130", "Google Chrome";v="130", "Not?A_Brand";v="99"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36',
        'x-requested-with': 'XMLHttpRequest',
    }

    params = {
        'lm': '',
        'ajaxStoreImageDir': '/wcsstore/OKMarketSAS/',
        'searchType': '1000',
        'advancedSearch': '',
        'filterTerm': '',
        'storeId': '10151',
        'manufacturer': '',
        'ddkey': 'ProductListingView_6_-1011_3074457345618259713',
        'sType': 'SimpleSearch',
        'metaData': '',
        'catalogId': '10551',
        'searchTerm': '',
        'resultsPerPage': '72',
        'filterFacet': '',
        'resultCatEntryType': '',
        'gridPosition': '',
        'emsName': '',
        'disableProductCompare': 'true',
        'langId': '-20',
        'facet': '',
        'categoryId': cat,
        'custom_view': 'true',
    }

    data = {
        'contentBeginIndex': '0',
        'productBeginIndex': '0',
        'beginIndex': '0',
        'orderBy': '3',
        'facetId': '',
        'pageView': 'grid',
        'resultType': 'products',
        'orderByContent': '',
        'searchTerm': '',
        'facet': '',
        'facetLimit': '',
        'pageSize': '72',
        'langId': '-20',
        'totalPages': '2.0',
        'requestType': 'filter',
        'objectId': '_6_-1011_3074457345618259713',
        'requesttype': 'ajax',
    }

    async with aiohttp.ClientSession() as session:
        async with session.post(url=url,
                                headers=headers,
                                data=data, params=params,
                                cookies=cookies,
                                proxy=proxy) as response:
            soup = bs(await response.text(), "lxml")
            product_list = []
            product_listing_widget = soup.find("div", class_="productListingWidget")
            product_listing_container = product_listing_widget.find("div", class_="product_listing_container")
            products = product_listing_container.find_all("div", class_="product ok-theme")
            for product in products:
                mob_acts = product.find("div", class_="mobile-actions")
                price = int(float(mob_acts.find("div", class_="product-cart").find("a").get("data-price"))*100)
                product_name = product.find("div", class_="product-name")
                title = product_name.find("a").get("title")
                if price:
                    product_list.append([price, title])
                else:
                    continue
    return product_list

async def perekryostok(cat, proxy):

    headers = {
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
        'auth': 'Bearer eyJhbGciOiJSUzI1NiIsInR5cCIgOiAiSldUIiwia2lkIiA6ICJFRlBVcWRLamZTVG9vR09POWRpLURKQk4zWkgyaUxlcE5yWTF3dXgyNHFvIn0.eyJleHAiOjE3MzAxMjg3NDAsImlhdCI6MTczMDEyODM4MCwiYXV0aF90aW1lIjoxNzMwMTI4Mzc4LCJqdGkiOiJkNjcxNDA2ZC0xNzAyLTQ3MmYtYTc3Yi03ZTZmYzM5YjdiZTYiLCJpc3MiOiJodHRwczovL2lkLng1LnJ1L2F1dGgvcmVhbG1zL3Nzb3g1aWQiLCJhdWQiOiJhY2NvdW50Iiwic3ViIjoiZjo2NmI5YWQ2MC00Y2I0LTRlZTEtYjlhMC0wNTI4ZmRlYWMyYjE6MzQxNTE4MjUiLCJ0eXAiOiJCZWFyZXIiLCJhenAiOiJ0Y3hfd2ViIiwic2Vzc2lvbl9zdGF0ZSI6ImIzMTc4NDc5LWU1NGYtNGVhZS1hNDY3LTRmYzBlMjYxZTkyZiIsImFjciI6IjEiLCJyZWFsbV9hY2Nlc3MiOnsicm9sZXMiOlsib2ZmbGluZV9hY2Nlc3MiLCJ1bWFfYXV0aG9yaXphdGlvbiJdfSwicmVzb3VyY2VfYWNjZXNzIjp7ImFjY291bnQiOnsicm9sZXMiOlsibWFuYWdlLWFjY291bnQiLCJ2aWV3LXByb2ZpbGUiXX19LCJzY29wZSI6Im9wZW5pZCBvZmZsaW5lX2FjY2VzcyBwcm9maWxlIGVtYWlsIiwic2lkIjoiYjMxNzg0NzktZTU0Zi00ZWFlLWE0NjctNGZjMGUyNjFlOTJmIiwic291cmNlX2RldGFpbCI6IndlYiIsInBlcm1pc3Npb25NYXJrZXRpbmciOiJOIiwiZW1haWxfdmVyaWZpZWQiOmZhbHNlLCJuYW1lIjoi0JLQu9Cw0LTQuNGB0LvQsNCyIiwicHJlZmVycmVkX3VzZXJuYW1lIjoiNzk4MTcxNjU3MzEiLCJjaXBfaWQiOiJJRFguMzQxNTE4MjUiLCJnaXZlbl9uYW1lIjoi0JLQu9Cw0LTQuNGB0LvQsNCyIiwiZW1haWwiOiJtdmxhZDE3MzE3M0BnbWFpbC5jb20iLCJ4NWlkIjoiMzQxNTE4MjUifQ.KgEC2hotrdea5rLcdAsO_PS9WihowX3xSjGozYw_9-COo3kMnp9IlHpFppQJYdZ_YtbCL3WavAKxWxgBY-yc2yAGhHjyG0Knez9yVPa_DAvC1nyi8709h383KEU5VKHua3u-bWae4NUvAGzWxvKpdoV-cXNOdwPqfi88Ez3JTxUpSABft_tQ-_RC9q4hMYEWI1wXgB6PDDtQsGw5GQKIAzMdLOwYaUfRTZod8C1whrIoZh0vAYnv_6iyup0rNd3BzC0gJ8da9E4c3__7M-_bEDm6aPV0E9cTGVtYjEmAKwblkaY8gifr9QqIwrXlK-gdIfRtU6kRIVCozrS7_lAM5w',
        'content-type': 'application/json',
        'origin': 'https://www.perekrestok.ru',
        'priority': 'u=1, i',
        'sec-ch-ua': '"Chromium";v="130", "Google Chrome";v="130", "Not?A_Brand";v="99"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36',
    }

    json_data = {
        'page': 1,
        'perPage': 48,
        'orderBy': 'price',
        'orderDirection': 'asc',
        'filter': {
            'category': 122,
            'onlyWithProductReviews': False,
        },
        'withBestProductReviews': False,
    }

    url = "https://www.perekrestok.ru/api/customer/1.4.1.0/catalog/product/grouped-feed"

    async with aiohttp.ClientSession() as session:
        async with session.post(url=url, headers=headers, json=json_data, proxy=proxy) as response:
            json_file = await response.json()
            groups = json_file["content"]["items"]
            product_list = []
            for group in groups:
                if group["group"]["id"] == cat:
                    products = group["products"]
                    for product in products:
                        price = int(product["priceTag"]["price"])
                        title = product["title"]
                        product_list.append([price, title])
                    break
    return product_list

async def pyatyorochka(cat):

    headers = {
        'accept': '*/*',
        'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
        'content-type': 'text/plain;charset=UTF-8',
        'origin': 'https://5ka.ru',
        'priority': 'u=1, i',
        'referer': 'https://5ka.ru/',
        'sec-ch-ua': '"Google Chrome";v="129", "Not=A?Brand";v="8", "Chromium";v="129"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'cross-site',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36',
    }

    async with aiohttp.ClientSession() as session:
        async with session.get(url=cat, headers=headers) as response:
            json_file = await response.json()
            products = json_file["products"]
            product_list = []
            for product in products:
                if product["prices"]["discount"]:
                    price = int(float(product["prices"]["discount"])*100)
                else:
                    price = int(float(product["prices"]["regular"])*100)
                title = product["name"]
                product_list.append([price, title])
    return product_list

async def dixy(cat, proxy):
    headers = {
        'Accept': '*/*',
        'Accept-Language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
        'Connection': 'keep-alive',
        'Referer': 'https://dixy.ru/',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36',
        'sec-ch-ua': '"Google Chrome";v="131", "Chromium";v="131", "Not_A Brand";v="24"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
    }

    params = {
        'block': 'product-list',
        'sid': cat,
        'perPage': '999',
        'sort': 'price_asc',
        'filterData': '',
        'searchQuery': '',
    }

    url = 'https://dixy.ru/ajax/listing-json.php'

    product_list = []
    async with aiohttp.ClientSession() as session:
        async with session.get(url=url, params=params, headers=headers, proxy=proxy) as response:
            json_data_list = await response.json()
            for json_data in json_data_list:
                products = json_data["cards"]
                for product in products:
                    title = product["title"]
                    price = product["priceSimple"]
                    if price.isdigit():
                        price = int(price)
                    else:
                        price = int(float(price.replace(" ",""))*100)
                    product_list.append([price, title])
    return product_list
