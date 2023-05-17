import ctypes
import os


def is_cudnn__version_available(version: int = 8) -> bool:
    try:
        cudnn_lib = "libcudnn.so"
        if os.name == "nt":
            cudnn_lib += f"{version}.dll"
        elif os.sys.platform == "darwin":
            cudnn_lib = "libcudnn." + f"{version}.dylib"
        else:
            cudnn_lib += f"{version}.so"
        ctypes.CDLL(cudnn_lib)
        return True
    except OSError:
        return False


def id_cudnn_available() -> bool:
    for version in [7, 8, 9, 10, 11, 12]:
        if is_cudnn__version_available(version=version):
            return True
    return False
