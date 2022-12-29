from chinacapi.chinac_api import ChinacApi


# 获取本机在星界链的公网IP
print(ChinacApi.get_request_ip())
