import os

import numpy as np
import pytest

from pyfms import pyDomain, pyFMS, pyFMS_mpp, pyFMS_mpp_domains


@pytest.mark.create
def test_create_input_nml():
    inputnml = open("input.nml", "w")
    inputnml.close()
    assert os.path.isfile("input.nml")


@pytest.mark.parallel
def test_update_domains():

    nx = 8
    ny = 8
    npes = 4
    whalo = 2
    ehalo = 2
    nhalo = 2
    shalo = 2
    domain_id = 0

    pyfms = pyFMS(cFMS_path="./cFMS/libcFMS/.libs/libcFMS.so")
    mpp = pyFMS_mpp(cFMS=pyfms.cFMS)
    mpp_domains = pyFMS_mpp_domains(cFMS=pyfms.cFMS)

    global_indices = [0, (nx - 1), 0, (ny - 1)]
    cyclic_global_domain = 2

    layout = mpp_domains.define_layout(global_indices=global_indices, ndivs=npes)

    domain = pyDomain(
        global_indices=global_indices,
        layout=layout,
        mpp_domains_obj=mpp_domains,
        domain_id=domain_id,
        whalo=whalo,
        ehalo=ehalo,
        shalo=shalo,
        nhalo=nhalo,
        xflags=cyclic_global_domain,
        yflags=cyclic_global_domain,
    )

    answers = np.array(
        [
            [
                [88, 98, 28, 38, 48, 58, 68, 78],
                [89, 99, 29, 39, 49, 59, 69, 79],
                [82, 92, 22, 32, 42, 52, 62, 72],
                [83, 93, 23, 33, 43, 53, 63, 73],
                [84, 94, 24, 34, 44, 54, 64, 74],
                [85, 95, 25, 35, 45, 55, 65, 75],
                [86, 96, 26, 36, 46, 56, 66, 76],
                [87, 97, 27, 37, 47, 57, 67, 77],
            ],
            [
                [84, 94, 24, 34, 44, 54, 64, 74],
                [85, 95, 25, 35, 45, 55, 65, 75],
                [86, 96, 26, 36, 46, 56, 66, 76],
                [87, 97, 27, 37, 47, 57, 67, 77],
                [88, 98, 28, 38, 48, 58, 68, 78],
                [89, 99, 29, 39, 49, 59, 69, 79],
                [82, 92, 22, 32, 42, 52, 62, 72],
                [83, 93, 23, 33, 43, 53, 63, 73],
            ],
            [
                [48, 58, 68, 78, 88, 98, 28, 38],
                [49, 59, 69, 79, 89, 99, 29, 39],
                [42, 52, 62, 72, 82, 92, 22, 32],
                [43, 53, 63, 73, 83, 93, 23, 33],
                [44, 54, 64, 74, 84, 94, 24, 34],
                [45, 55, 65, 75, 85, 95, 25, 35],
                [46, 56, 66, 76, 86, 96, 26, 36],
                [47, 57, 67, 77, 87, 97, 27, 37],
            ],
            [
                [44, 54, 64, 74, 84, 94, 24, 34],
                [45, 55, 65, 75, 85, 95, 25, 35],
                [46, 56, 66, 76, 86, 96, 26, 36],
                [47, 57, 67, 77, 87, 97, 27, 37],
                [48, 58, 68, 78, 88, 98, 28, 38],
                [49, 59, 69, 79, 89, 99, 29, 39],
                [42, 52, 62, 72, 82, 92, 22, 32],
                [43, 53, 63, 73, 83, 93, 23, 33],
            ],
        ],
        dtype=np.float32,
    )

    xdatasize = whalo + nx + ehalo
    ydatasize = shalo + ny + nhalo

    isc = domain.compute_domain.xbegin.value
    jsc = domain.compute_domain.ybegin.value
    xsize_c = domain.compute_domain.xsize.value
    ysize_c = domain.compute_domain.ysize.value
    xsize_d = domain.data_domain.xsize.value
    ysize_d = domain.data_domain.ysize.value

    global_data = np.zeros(shape=(xdatasize, ydatasize), dtype=np.float32)
    for ix in range(nx):
        for iy in range(ny):
            global_data[whalo + ix][shalo + iy] = (iy + shalo) * 10 + (ix + whalo)

    idata = np.zeros(shape=(xsize_d, ysize_d), dtype=np.float32)
    for ix in range(xsize_c):
        for iy in range(ysize_c):
            idata[ix + whalo][iy + whalo] = global_data[isc + ix][jsc + iy]

    mpp_domains.update_domains(
        field=idata,
        domain_id=domain_id,
        whalo=whalo,
        ehalo=ehalo,
        shalo=shalo,
        nhalo=nhalo,
    )

    assert np.array_equal(idata, answers[mpp.pe()])

    pyfms.pyfms_end()


@pytest.mark.remove
def test_remove_input_nml():
    os.remove("input.nml")
    assert not os.path.isfile("input.nml")


if __name__ == "__main__":
    test_update_domains()
