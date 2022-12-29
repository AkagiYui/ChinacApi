from typing import TYPE_CHECKING

from chinacapi.utils import dataclass_ex

if TYPE_CHECKING:
    from chinacapi.cloud_phone_region import CloudPhoneRegion
    from chinacapi.entity.cloud_phone_status import CloudPhoneStatus


@dataclass_ex
class CloudPhone:
    adb_host_port: str
    adb_status: str
    is_enable: bool
    region: 'CloudPhoneRegion'
    id: str
    status: 'CloudPhoneStatus'
