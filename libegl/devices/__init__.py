from .generic import GenericEGLDevice
from .gbm import GBMDevice


def probe():
    for cls in (GenericEGLDevice, GBMDevice):
        for device in cls.probe():
            yield device
