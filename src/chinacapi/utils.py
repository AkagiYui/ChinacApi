import base64
import hashlib
import hmac
import time
import urllib.parse
import urllib.request
from dataclasses import dataclass
from typing import Tuple, Dict, Mapping

from chinacapi.cloud_phone_region import CloudPhoneRegion
from chinacapi.entity.cloud_phone_status import CloudPhoneStatus


def request(request_url, headers: dict = None, body: bytes = None, method='GET') -> Tuple[int, str]:
    """
    发送请求
    :param request_url:  请求地址
    :param headers: 请求头
    :param body: 请求体
    :param method: 请求方法
    :return: 状态码，响应体
    """
    req = urllib.request.Request(
        request_url,
        data=body,
        headers=headers or {},
        method=method,
    )
    res = urllib.request.urlopen(req)
    return res.getcode(), res.read().decode('utf-8')


def sha_hmac256_signature(key: str, msg: str) -> str:
    """
    base64 hmac256加密
    :param key: 密钥
    :param msg: 消息
    :return: 加密后的字符串
    """
    h = hmac.new(bytearray(key, 'utf-8'), bytearray(msg, 'utf-8'), hashlib.sha256)
    return str(base64.encodebytes(h.digest()).strip(), 'utf-8')


def generate_headers() -> Dict[str, str]:
    """
    生成请求头
    :return: 请求头
    """
    return {
        'Content-Type': 'application/json;charset=UTF-8',
        'Accept-Encoding': '*',
        'Date': time.strftime("%Y-%m-%dT%H:%M:%S +0800", time.localtime())
    }


def percent_encode(url_string: str) -> str:
    """
    转成url通信标准RFC 3986
    :param url_string: 原始url
    :return: 转换后的url
    """
    url_string = url_string.replace('+', '%20')
    url_string = url_string.replace('*', '%2A')
    url_string = url_string.replace('%7E', '~')
    return url_string


def percent_url_encode_params(params: Mapping) -> str:
    """
    encodeurl参数
    :param params: 参数
    :return: 转换后的参数
    """
    url_string = urllib.parse.urlencode(params)
    return percent_encode(url_string)


def percent_url_encode_str(url_string: str) -> str:
    """
    encodeurl字符串
    :param url_string: 字符串
    :return: 转换后的字符串
    """
    url_string = urllib.parse.quote(url_string)
    return percent_encode(url_string)


def camel_key_to_snake(ori_dict: dict) -> dict:
    """驼峰转下划线"""
    import re
    return {re.sub(r'([a-z])([A-Z])', r'\1_\2', k).lower(): v for k, v in ori_dict.items()}


def dataclass_ex(cls):
    cls = dataclass(cls)

    def __init__(self, ori: dict):
        annotations: Dict[str, type] = self.__annotations__
        for k, v in ori.items():
            if k in annotations:
                type_in_annotations: type = annotations[k]
                if type_in_annotations == 'CloudPhoneRegion':
                    self.__dict__[k] = CloudPhoneRegion(v)
                elif type_in_annotations == 'CloudPhoneStatus':
                    self.__dict__[k] = CloudPhoneStatus(v)
                else:
                    self.__dict__[k] = type_in_annotations(v)

    cls.__init__ = __init__
    return cls
