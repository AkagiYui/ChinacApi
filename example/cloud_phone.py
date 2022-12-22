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

# 设置云手机ADB白名单
print(cpa.set_cloud_phone_adb_white_ip(CloudPhoneRegion.SZ, list(set(ips + [
    '1.1.1.1', '1.1.1.2', '1.1.1.3',
    '1.1.1.4', '1.1.1.5', '1.1.1.6',
]))))
ips = cpa.list_cloud_phone_adb_white_ip(CloudPhoneRegion.SZ)
print(ips)


print(cpa.reboot_cloud_phone(cp))  # 重启云手机
print(cpa.start_cloud_phone(cp))  # 开启云手机
print(cpa.stop_cloud_phone(cp))  # 关闭云手机
