"""
openapi接口
"""
import hashlib
import json
from typing import Dict

from chinacapi.cloud_phone_api import CloudPhoneApi
from chinacapi.utils import generate_headers, request, percent_url_encode_params, percent_url_encode_str, \
    sha_hmac256_signature


class ChinacApi:
    """
    星界链API

    https://docs-api.chinac.com/
    """
    def __init__(self, access_key: str, access_key_secret: str):
        """
        星界链API
        :param access_key: 访问密钥
        :param access_key_secret: 私钥
        """
        self.access_key: str = access_key
        self.access_key_secret: str = access_key_secret
        self.open_api_url: str = 'https://api.chinac.com/v2'

        # 各个API
        self.cloud_phone_api = CloudPhoneApi(self)  # 云手机

    def request(self, action: str, body: dict = None, method: str = 'GET') -> dict:
        """
        发送请求

        https://docs-api.chinac.com/publicparam
        :param action: 执行的操作
        :param body: 请求体
        :param method: 请求方法
        :return: 返回的json
        """
        headers: dict = generate_headers()
        request_body = None
        if method == 'POST' and body:
            request_body = json.dumps(body).encode(encoding='UTF8')

        request_url = self._generate_url(action, headers, method)
        code, response_body = request(request_url, headers, request_body, method)
        if code == 200:
            return json.loads(response_body)
        raise Exception(f'request error, code: {code}, body: {response_body}')

    def _generate_url(self, action, headers, method) -> str:
        """
        生成请求地址

        https://docs-api.chinac.com/signature
        :param action: 执行的操作
        :param headers: 请求头
        :param method: 请求方法
        :return: 请求url, 请求body
        """
        params = {
            'Action': action,
            'Version': '1.0',  # 目前固定1.0
            'AccessKeyId': self.access_key,
            'Date': headers['Date']
        }
        request_query = percent_url_encode_params(params)
        res = self._generate_signature(request_query, headers, method)
        request_url = f'{self.open_api_url}?{request_query}&Signature={res}'
        return request_url

    def _generate_signature(self, request_query: str, headers: Dict[str, str], method: str) -> str:
        """
        生成签名
        :param request_query: 请求参数字符串
        :param headers: 请求头
        :param method: 请求方法
        :return: 签名
        """
        sign_string = [method, '\n']
        m = hashlib.md5()
        m.update(bytearray(request_query, 'utf-8'))
        sign_string.append(m.hexdigest())
        sign_string.append('\n')
        sign_string.append(headers['Content-Type'])
        sign_string.append('\n')
        sign_string.append(percent_url_encode_str(headers['Date']))
        sign_string.append('\n')
        sign_string = ''.join(sign_string)
        signature = percent_url_encode_str(sha_hmac256_signature(self.access_key_secret, sign_string))
        return signature
