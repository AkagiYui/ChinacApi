from enum import Enum


class CloudPhoneRegion(Enum):
    JS = 'cn-jsha-cloudphone'  # 华东：江苏一区（电信）
    JS2 = 'cn-jsha-cloudphone-2'  # 华东：江苏二区（电信）
    JS3 = 'cn-jsha-cloudphone-3'  # 华东：江苏三区（电信）
    FJ = 'cn-fjqz-cloudphone'  # 华东：福建一区（电信）
    SZ = 'cn-szyh-cloudphone'  # 华南：深圳一区（电信）
    HK = 'cn-hk-cloudphone'  # 香港：香港一区（海外）
    HK2 = 'cn-hk-cloudphone-2'  # 香港：香港二区（海外）
