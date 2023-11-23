import requests

cookies = {
    'deviceId': 'f9d74070-a9dc-c3fb-1417-562591909a86',
    '_by_l_g_d': 'f99cf85e-9599-b9a4-ddca-56aba306992b',
    'b_t_c_k': '',
    '_gcl_au': '1.1.1734450553.1700642245',
    '_ga': 'GA1.1.808882825.1700642247',
    '_ym_uid': '170064224745076190',
    '_ym_d': '1700642247',
    'BYBIT_REG_REF_prod': '{"lang":"ru-RU","g":"f99cf85e-9599-b9a4-ddca-56aba306992b","referrer":"www.google.com/","source":"google.com","medium":"other","url":"https://www.bybit.com/ru-RU/help-center/article/How-to-retrieve-API-documentations"}',
    'BYBIT_REG_REF_local': '{"lang":"ru-RU","g":"f99cf85e-9599-b9a4-ddca-56aba306992b","referrer":"www.bybit.com/fiat/trade/otc/?actionType=1&token=USDT&fiat=RUB&paymentMethod=","source":"bybit.com","medium":"other","url":"https://www.bybit.com/future-activity/ru-RU/developer"}',
    'sensorsdata2015jssdkcross': '%7B%22distinct_id%22%3A%2218bf62d331037d-08742a6bbcdb688-26031051-2073600-18bf62d3311cbf%22%2C%22first_id%22%3A%22%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%2C%22%24latest_referrer%22%3A%22%22%2C%22_a_u_v%22%3A%220.0.5%22%7D%2C%22identities%22%3A%22eyIkaWRlbnRpdHlfY29va2llX2lkIjoiMThiZjYyZDMzMTAzN2QtMDg3NDJhNmJiY2RiNjg4LTI2MDMxMDUxLTIwNzM2MDAtMThiZjYyZDMzMTFjYmYifQ%3D%3D%22%2C%22history_login_id%22%3A%7B%22name%22%3A%22%22%2C%22value%22%3A%22%22%7D%2C%22%24device_id%22%3A%2218bf62d331037d-08742a6bbcdb688-26031051-2073600-18bf62d3311cbf%22%7D',
    '_abck': '93FE6D3509D0256B419F0D67D48112A0~0~YAAQjoVlX48fes2LAQAAUdR9/AqA2jebgQXRtxUh3SGPK8DZWYyUlAKU3TpUgDg8yBlEscdvuzDfgf3np2kXFsEg1uwLkg/Ln0nNrVP/a0fs3yH8qpZn0xapoylKwQogSsCJS1mTNIO+OcGAA1JWU87UtxKNZdtW8HHrMvEPXZPhQXVNdqYzXQT9+8RwS26fVGzo4ruArOdDdmtfzLZS8FU8mE0ECAi5OpOkqR4J8LbtO+4EqXAAMTJlDDyE+GKrLaaOMUytp2/cjb8YakuHzSX919KjoHfvWbqEXD0WwGVmZqOpTutQ8ZQ5f6gJ6cZMqUYF7nftyPCUSFMS9Yfp0vOzmKZchEhz+Hyfr3NNEEZz8l/Pfa0UlKUjZbiWMVFM53xsYKYZiMzCMvWUR/fry88+pOl2t6k=~-1~-1~-1',
    'bm_sz': 'D295E8C98589445D43E30DAC54DCF217~YAAQjoVlX5Ifes2LAQAAUdR9/BVxTNWsXAEsg92TfMdbMZ6cGo61LkOBNdBIKrWmDyK7bc1xBjx+HXC/SjGc7VudZjtOMQZmRqGWYN5K4sevvzBQQNCvQdiI606LpKYgo+vaHLFu+5YYdUX6xDfKQj81A/b1fPIWDcLyULRTXYKhBMS6vwhrD8Fa/Y2Oc0tYqpe7L0GI07f6UaaKP41pIWO4ldRyHwCtV25+zgFiviI4fy9PxwS9iCQyVocJ0QjmZEl+Wk/ndksL2Yf2x+E5KeGWxk9CXH56F39nPvvi7trMag==~4535621~3225144',
    'ak_bmsc': 'D12071A925767CE9B72B1933C24CFFCD~000000000000000000000000000000~YAAQjoVlX6Qfes2LAQAAut59/BWom779fJYCpTdLv8xY9tmr5mkHEqsWi24Blo7Hnc//23CUOEtMlC9tA78PrV0MCwOgauSYiS7M/rh78GfHP/3G+UBieWSRfVz27A/FO5lrfrUpq7TFDy83IEeuMEHJ243z0YSZKJtXB7lyrQHsS3ANxteId5yRbBuaKTH0fGP+QjKdymP2iNCuepkilNxKAv6RL3YQ2bH2keGaYNmTW4ORiLv0fNiaptv3kLDIUZd2zEwgOXifvRGS+wyZucSGmYWGtPS730f3Y1DkSatgzJtk6HpFiuw/aoVHSZblLoInkxP0xV6l+DCPpe+frcp5izHwWN8w2AALU0PUcyDvwsPWxGG4Ye9UKFYJD1+5qNO/neZgfWYLGgEDJNSeaOJ1MA635hqBrk2JD5mbdvAL9DPv/4PFjsINy62LKziSgvTOZ8h43a6am8ayu2A/GNrXms39qRvn9leEsH8RF0DgK0mBiG+36e8TIm5alyqU',
    '_ym_isad': '2',
    '_ga_SPS4ND2MGC': 'GS1.1.1700748187.3.1.1700748236.11.0.0',
    'bm_sv': '989237779FD23EEF7ECAAEA91F52AF24~YAAQXZbvUEPG2tqLAQAAP7Z+/BVkaOtrWsfRFQk+6i2wYwpnZBpimJAV1CIQCU0rTf81hQa/lqb7lmyIXwRR81AT3YbqDnBmG8To+iNiZchB06bFTzD9U9fsMn20RQyGUmqvKgctiYZwEPqM1Dn3Wt9G6eAIHR9w2cJdU2slJoIk+8nzOw/LXXTflXSMPEsSw8Jpse+2CvnC2Saria+Kh4AJE43Rc96KHKAZ7CXMYbxlu5s3QNvdTjSb5AiVIyhb~1',
}

headers = {
    'authority': 'api2.bybit.com',
    'accept': 'application/json',
    'accept-language': 'ru-RU',
    'cache-control': 'no-cache',
    'content-type': 'application/json;charset=UTF-8',
    # 'cookie': 'deviceId=f9d74070-a9dc-c3fb-1417-562591909a86; _by_l_g_d=f99cf85e-9599-b9a4-ddca-56aba306992b; b_t_c_k=; _gcl_au=1.1.1734450553.1700642245; _ga=GA1.1.808882825.1700642247; _ym_uid=170064224745076190; _ym_d=1700642247; BYBIT_REG_REF_prod={"lang":"ru-RU","g":"f99cf85e-9599-b9a4-ddca-56aba306992b","referrer":"www.google.com/","source":"google.com","medium":"other","url":"https://www.bybit.com/ru-RU/help-center/article/How-to-retrieve-API-documentations"}; BYBIT_REG_REF_local={"lang":"ru-RU","g":"f99cf85e-9599-b9a4-ddca-56aba306992b","referrer":"www.bybit.com/fiat/trade/otc/?actionType=1&token=USDT&fiat=RUB&paymentMethod=","source":"bybit.com","medium":"other","url":"https://www.bybit.com/future-activity/ru-RU/developer"}; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%2218bf62d331037d-08742a6bbcdb688-26031051-2073600-18bf62d3311cbf%22%2C%22first_id%22%3A%22%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%2C%22%24latest_referrer%22%3A%22%22%2C%22_a_u_v%22%3A%220.0.5%22%7D%2C%22identities%22%3A%22eyIkaWRlbnRpdHlfY29va2llX2lkIjoiMThiZjYyZDMzMTAzN2QtMDg3NDJhNmJiY2RiNjg4LTI2MDMxMDUxLTIwNzM2MDAtMThiZjYyZDMzMTFjYmYifQ%3D%3D%22%2C%22history_login_id%22%3A%7B%22name%22%3A%22%22%2C%22value%22%3A%22%22%7D%2C%22%24device_id%22%3A%2218bf62d331037d-08742a6bbcdb688-26031051-2073600-18bf62d3311cbf%22%7D; _abck=93FE6D3509D0256B419F0D67D48112A0~0~YAAQjoVlX48fes2LAQAAUdR9/AqA2jebgQXRtxUh3SGPK8DZWYyUlAKU3TpUgDg8yBlEscdvuzDfgf3np2kXFsEg1uwLkg/Ln0nNrVP/a0fs3yH8qpZn0xapoylKwQogSsCJS1mTNIO+OcGAA1JWU87UtxKNZdtW8HHrMvEPXZPhQXVNdqYzXQT9+8RwS26fVGzo4ruArOdDdmtfzLZS8FU8mE0ECAi5OpOkqR4J8LbtO+4EqXAAMTJlDDyE+GKrLaaOMUytp2/cjb8YakuHzSX919KjoHfvWbqEXD0WwGVmZqOpTutQ8ZQ5f6gJ6cZMqUYF7nftyPCUSFMS9Yfp0vOzmKZchEhz+Hyfr3NNEEZz8l/Pfa0UlKUjZbiWMVFM53xsYKYZiMzCMvWUR/fry88+pOl2t6k=~-1~-1~-1; bm_sz=D295E8C98589445D43E30DAC54DCF217~YAAQjoVlX5Ifes2LAQAAUdR9/BVxTNWsXAEsg92TfMdbMZ6cGo61LkOBNdBIKrWmDyK7bc1xBjx+HXC/SjGc7VudZjtOMQZmRqGWYN5K4sevvzBQQNCvQdiI606LpKYgo+vaHLFu+5YYdUX6xDfKQj81A/b1fPIWDcLyULRTXYKhBMS6vwhrD8Fa/Y2Oc0tYqpe7L0GI07f6UaaKP41pIWO4ldRyHwCtV25+zgFiviI4fy9PxwS9iCQyVocJ0QjmZEl+Wk/ndksL2Yf2x+E5KeGWxk9CXH56F39nPvvi7trMag==~4535621~3225144; ak_bmsc=D12071A925767CE9B72B1933C24CFFCD~000000000000000000000000000000~YAAQjoVlX6Qfes2LAQAAut59/BWom779fJYCpTdLv8xY9tmr5mkHEqsWi24Blo7Hnc//23CUOEtMlC9tA78PrV0MCwOgauSYiS7M/rh78GfHP/3G+UBieWSRfVz27A/FO5lrfrUpq7TFDy83IEeuMEHJ243z0YSZKJtXB7lyrQHsS3ANxteId5yRbBuaKTH0fGP+QjKdymP2iNCuepkilNxKAv6RL3YQ2bH2keGaYNmTW4ORiLv0fNiaptv3kLDIUZd2zEwgOXifvRGS+wyZucSGmYWGtPS730f3Y1DkSatgzJtk6HpFiuw/aoVHSZblLoInkxP0xV6l+DCPpe+frcp5izHwWN8w2AALU0PUcyDvwsPWxGG4Ye9UKFYJD1+5qNO/neZgfWYLGgEDJNSeaOJ1MA635hqBrk2JD5mbdvAL9DPv/4PFjsINy62LKziSgvTOZ8h43a6am8ayu2A/GNrXms39qRvn9leEsH8RF0DgK0mBiG+36e8TIm5alyqU; _ym_isad=2; _ga_SPS4ND2MGC=GS1.1.1700748187.3.1.1700748236.11.0.0; bm_sv=989237779FD23EEF7ECAAEA91F52AF24~YAAQXZbvUEPG2tqLAQAAP7Z+/BVkaOtrWsfRFQk+6i2wYwpnZBpimJAV1CIQCU0rTf81hQa/lqb7lmyIXwRR81AT3YbqDnBmG8To+iNiZchB06bFTzD9U9fsMn20RQyGUmqvKgctiYZwEPqM1Dn3Wt9G6eAIHR9w2cJdU2slJoIk+8nzOw/LXXTflXSMPEsSw8Jpse+2CvnC2Saria+Kh4AJE43Rc96KHKAZ7CXMYbxlu5s3QNvdTjSb5AiVIyhb~1',
    'guid': 'f99cf85e-9599-b9a4-ddca-56aba306992b',
    'lang': 'ru-RU',
    'origin': 'https://www.bybit.com',
    'platform': 'PC',
    'pragma': 'no-cache',
    'referer': 'https://www.bybit.com/',
    'risktoken': 'dmVyMQ|ZWFkYzhmMDAzZG0wNjBhZDI0Y2gzdnpnM2MyZjRhYTEyZGU3ZDI=||v2:gRoGLDjzDH/JzU3VNJHpT2Meqs0ZpzAeRxSTCBPR0HE5y/4Nu59FUvQJO57+4m5BNV7tKJedghd5P99YKxAd6U42SeYakK/FuUdNW4ol38OH046sxDGYnLbIAnHI8xcIxyi+7CloM6jGng4SCLW4fjjtKdAlnXAzLtoTR7EZYhxcWChLujgPpGQMQJ09eWt8nB1TGlpXB/I8tZW+hX4ocmK/9eRsILGQihRIsV6rnA==',
    'sec-ch-ua': '"Google Chrome";v="119", "Chromium";v="119", "Not?A_Brand";v="24"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'traceparent': '00-656d2ef0e0d1bbb01a06d0032f30ec4e-42b07969244da87f-01',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36',
}

json_data = {
    'userId': '',
    'tokenId': 'USDT',
    'currencyId': 'KZT',
    'payment': [
        '150',
    ],
    'side': '0',
    'size': '10',
    'page': '1',
    'amount': '',
    'authMaker': False,
    'canTrade': False,
}


def get_sell_kzt():
    s = requests.Session()
    response = s.post('https://api2.bybit.com/fiat/otc/item/online', cookies=cookies, headers=headers, json=json_data)

    return response.json()


if __name__ == '__main__':
    get_sell_kzt()
