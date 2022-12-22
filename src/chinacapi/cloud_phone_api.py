from typing import TYPE_CHECKING, List, Union

from .cloud_phone_region import CloudPhoneRegion
from .entity.cloud_phone import CloudPhone
from .exception import NotStopError, RequestOperateResourceLockedError
from .utils import camel_key_to_snake

if TYPE_CHECKING:
    from .chinac_api import ChinacApi


class CloudPhoneApi:
    def __init__(self, chinac_api: 'ChinacApi'):
        self.chinac = chinac_api

    def list_cloud_phone(self) -> List[CloudPhone]:
        """列出云手机"""
        res = self.chinac.request('ListCloudPhone', method='POST')
        if res['code'] != 10000:
            raise Exception(f'list cloud phone error, code: {res["code"]}, message: {res["message"]}')
        phones: List[dict] = res['data']['List']
        phones: List[CloudPhone] = [CloudPhone(camel_key_to_snake(phone)) for phone in phones]
        return phones

    def describe_cloud_phone(self, region: CloudPhoneRegion, phone_id: str) -> CloudPhone:
        """
        获取云手机详情(WIP)
        :param region: 手机所在区域
        :param phone_id: 手机ID
        :return: 手机详情
        """
        body = {
            'Region': region.value,
            'Id': phone_id,
        }
        res = self.chinac.request('DescribeCloudPhone', body, method='POST')
        if res['code'] != 10000:
            raise Exception(f'describe cloud phone error, code: {res["code"]}, message: {res["message"]}')
        return CloudPhone(camel_key_to_snake(res['data']['BasicInfo']))

    def reboot_cloud_phone(self, cloud_phones: Union[CloudPhone, List[CloudPhone]], remark: str = None) -> str:
        """
        重启云手机
        :param cloud_phones: 手机列表
        :param remark: 备注
        :return: 任务ID
        """
        if isinstance(cloud_phones, CloudPhone):
            cloud_phones = [cloud_phones]
        body = {
            'CloudPhones': [{'Id': phone.id, 'Region': phone.region.value} for phone in cloud_phones],
            'Remark': remark,
            'Operate': 'reboot',
        }
        res = self.chinac.request('RebootCloudPhone', body, method='POST')
        if res['code'] != 10000:
            raise Exception(f'reboot cloud phone error, code: {res["code"]}, message: {res["message"]}')
        return res['data']['TaskId']

    def list_cloud_phone_adb_white_ip(self, region: CloudPhoneRegion) -> List[str]:
        """
        列出云手机ADB白名单
        :param region: 手机所在区域
        :return: 白名单列表
        """
        body = {
            'Region': region.value,
        }
        res = self.chinac.request('ListCloudPhoneAdbWhiteIp', body, method='POST')
        if res['code'] != 10000:
            raise Exception(f'list cloud phone adb white ip error, code: {res["code"]}, message: {res["message"]}')
        return res['data']['Ips']

    def set_cloud_phone_adb_white_ip(self, region: CloudPhoneRegion, ips: List[str]) -> str:
        """
        设置云手机ADB白名单
        :param region: 手机所在区域
        :param ips: 白名单列表
        :return: 任务ID
        """
        body = {
            'Region': region.value,
            'Ips': ips,
        }
        res = self.chinac.request('SetCloudPhoneAdbWhiteIp', body, method='POST')
        if res['code'] != 10000:
            raise Exception(f'set cloud phone adb white ip error, code: {res["code"]}, message: {res["message"]}')
        return res['data']['TaskId']

    def operate_cloud_phone(self, cloud_phones: Union[CloudPhone, List[CloudPhone]], operate: str, remark: str = None) -> str:
        """
        操作云手机
        :param cloud_phones: 手机列表
        :param operate: 操作类型
        :param remark: 备注
        :return: 任务ID
        """
        if isinstance(cloud_phones, CloudPhone):
            cloud_phones = [cloud_phones]
        body = {
            'CloudPhones': [{'Id': phone.id, 'Region': phone.region.value} for phone in cloud_phones],
            'Remark': remark,
            'Operate': operate,
        }
        res = self.chinac.request('OperateCloudPhone', body, method='POST')
        code = res['code']
        if code != 10000:
            message = res['message']
            message = f'operate cloud phone error, code: {code}, message: {message}'
            if code == 'IncorrectInstanceStatus.NotStop':
                raise NotStopError(message)
            elif code == 'RequestOperateResourceLocked':
                raise RequestOperateResourceLockedError(message)
            raise Exception(message)
        return res['data']

    def start_cloud_phone(self, cloud_phones: Union[CloudPhone, List[CloudPhone]], remark: str = None) -> str:
        """
        启动云手机
        :param cloud_phones: 手机列表
        :param remark: 备注
        :return: 任务ID
        """
        return self.operate_cloud_phone(cloud_phones, 'start', remark)

    def stop_cloud_phone(self, cloud_phones: Union[CloudPhone, List[CloudPhone]], remark: str = None) -> str:
        """
        停止云手机
        :param cloud_phones: 手机列表
        :param remark: 备注
        :return: 任务ID
        """
        return self.operate_cloud_phone(cloud_phones, 'stop', remark)
