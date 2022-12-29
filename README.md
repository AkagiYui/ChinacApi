# ChinacApi 星界链API

[![pypi](https://img.shields.io/pypi/v/chinacapi.svg)](https://pypi.org/project/chinacapi/)
![support-version](https://img.shields.io/pypi/pyversions/chinacapi) 
[![license](https://img.shields.io/github/license/AkagiYui/ChinacApi)](https://github.com/AkagiYui/ChinacApi/blob/master/LICENSE)  
[![commit](https://img.shields.io/github/last-commit/AkagiYui/ChinacApi)](https://github.com/AkagiYui/ChinacApi/commits/master)

[星界链OpenApi](https://docs-api.chinac.com/) Python SDK

支持

- [x] 获取云手机列表
- [ ] 获取云手机详情
- [x] 重启云手机
- [x] 开启/关闭云手机
- [x] 获取云手机ADB白名单IP列表
- [x] 设置云手机ADB白名单IP
- [x] 获取本机在星界链的公网IP

## 安装

```shell
pip install chinacapi -i https://pypi.tuna.tsinghua.edu.cn/simple
```

## 使用

你需要先在[星界链控制台](https://console.chinac.com/iam)申请访问密钥。

```python
from chinacapi.cloud_phone_region import CloudPhoneRegion
from chinacapi.entity.cloud_phone import CloudPhone
from chinacapi.chinac_api import ChinacApi


# 创建 ChinacApi 实例
ca = ChinacApi('your_access_key', 'your_access_secret')
cpa = ca.cloud_phone_api  # 云手机API

# 列出所有云手机
cpl = cpa.list_cloud_phone()
for cp in cpl:
    print(cp)

# 通过ID构造云手机对象
cp = CloudPhone({
    'id': 'cp-xxxxxxxxxxxxxx',
    'region': CloudPhoneRegion.SZ,
})

# 获取云手机详情
print(cpa.describe_cloud_phone(cp.region, cp.id))

# 列出云手机ADB白名单
ips = cpa.list_cloud_phone_adb_white_ip(CloudPhoneRegion.SZ)
print(ips)

# 获取本机在星界链的公网IP
my_ip = ChinacApi.get_request_ip()
print(my_ip)

# 设置云手机ADB白名单
print(cpa.set_cloud_phone_adb_white_ip(CloudPhoneRegion.SZ, list(set(ips + my_ip))))
ips = cpa.list_cloud_phone_adb_white_ip(CloudPhoneRegion.SZ)
print(ips)


print(cpa.reboot_cloud_phone(cp))  # 重启云手机
print(cpa.start_cloud_phone(cp))  # 开启云手机
print(cpa.stop_cloud_phone(cp))  # 关闭云手机
```

---

[更新日志](https://github.com/AkagiYui/ChinacApi/blob/master/Changelog.md)
