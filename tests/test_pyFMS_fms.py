import os

from pyfms import pyFMS


def test_pyfms_init():
    assert os.path.exists("./cFMS/libcFMS/.libs/libcFMS.so")

    pyfmsobj = pyFMS(clibFMS_path="./cFMS/libcFMS/.libs/libcFMS.so")

    assert isinstance(pyfmsobj, pyFMS)

    pyfmsobj.pyfms_end()
