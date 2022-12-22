from enum import Enum


class CloudPhoneStatus(Enum):
    START = 'START'  # 运行中
    STOP = 'STOP'  # 已关闭
    ERROR = 'ERROR'  # 异常
    CREATING = 'CREATING'  # 创建中
    STARTING = 'STARTING'  # 开机中
    STOPING = 'STOPING'  # 关机中
    PAUSING = 'PAUSING'  # 暂停中
    PAUSED = 'PAUSED'  # 已暂停
    UNPAUSING = 'UNPAUSING'  # 取消暂停
    REBOOTING = 'REBOOTING'  # 重启中
    RESIZE = 'RESIZE'  # 变更中
    MIGRATE = 'MIGRATE'  # 迁移中
    DELETED = 'DELETED'  # 已删除
    DELETING = 'DELETING'  # 删除中
    DELETE_ERROR = 'DELETE_ERROR'  # 异常
    REBUILDING = 'REBUILDING'  # 重装中
    RESIZING = 'RESIZING'  # 配置变更中
