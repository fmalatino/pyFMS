import os


def test_shared_object_exists():
    assert os.path.exists("./cFMS/libcFMS/.libs/libcFMS.so")
