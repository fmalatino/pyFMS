import ctypes

import numpy as np
from numpy.typing import NDArray

from pyfms.pyfms_data_handling import setarray_Cdouble, setscalar_Cint32


class XGridData:
    def __init__(self, maxxgrid: int):
        self.i_in = np.empty(shape=maxxgrid, dtype=np.float64, order="C")
        self.j_in = np.empty(shape=maxxgrid, dtype=np.float64, order="C")
        self.i_out = np.empty(shape=maxxgrid, dtype=np.float64, order="C")
        self.j_out = np.empty(shape=maxxgrid, dtype=np.float64, order="C")
        self.xgrid_area = np.empty(shape=maxxgrid, dtype=np.float64, order="C")


def create_xgrid_2dx2d_order1(
    clibFMS: ctypes.CDLL,
    nlon_in: int,
    nlat_in: int,
    nlon_out: int,
    nlat_out: int,
    lon_in: NDArray,
    lat_in: NDArray,
    lon_out: NDArray,
    lat_out: NDArray,
    mask_in: NDArray,
    grid_data: XGridData,
) -> int:
    _cfms_create_xgrid_2dx2d_order1 = clibFMS.cFMS_create_xgrid_2dx2dx_order1

    nlon_in_c, nlon_in_t = setscalar_Cint32(nlon_in)
    nlat_in_c, nlat_in_t = setscalar_Cint32(nlat_in)
    nlon_out_c, nlon_out_t = setscalar_Cint32(nlon_out)
    nlat_out_c, nlat_out_t = setscalar_Cint32(nlat_out)
    lon_in_p, lon_in_t = setarray_Cdouble(lon_in)
    lat_in_p, lat_in_t = setarray_Cdouble(lat_in)
    lon_out_p, lon_out_t = setarray_Cdouble(lon_out)
    lat_out_p, lat_out_t = setarray_Cdouble(lat_out)
    mask_in_p, mask_in_t = setarray_Cdouble(mask_in)
    i_in_p, i_in_t = setarray_Cdouble(grid_data.i_in)
    j_in_p, j_in_t = setarray_Cdouble(grid_data.j_in)
    i_out_p, i_out_t = setarray_Cdouble(grid_data.i_out)
    j_out_p, j_out_t = setarray_Cdouble(grid_data.j_out)
    xgrid_area_p, xgrid_area_t = setarray_Cdouble(grid_data.xgrid_area)

    _cfms_create_xgrid_2dx2d_order1.argtypes = [
        nlon_in_t,
        nlat_in_t,
        nlon_out_t,
        nlat_out_t,
        lon_in_t,
        lat_in_t,
        lon_out_t,
        lat_out_t,
        mask_in_t,
        i_in_t,
        j_in_t,
        i_out_t,
        j_out_t,
        xgrid_area_t,
    ]
    _cfms_create_xgrid_2dx2d_order1.restype = ctypes.c_int32

    return _cfms_create_xgrid_2dx2d_order1(
        nlon_in_c,
        nlat_in_c,
        nlon_out_c,
        nlat_out_c,
        lon_in_p,
        lat_in_p,
        lon_out_p,
        lat_out_p,
        mask_in_p,
        i_in_p,
        j_in_p,
        i_out_p,
        j_out_p,
        xgrid_area_p,
    )


def get_maxxgrid(clibFMS: ctypes.CDLL) -> int:
    _cfms_get_maxxgrid = clibFMS.cFMS_get_maxxgrid

    _cfms_get_maxxgrid.argtypes = None
    _cfms_get_maxxgrid.restype = ctypes.c_int32

    return _cfms_get_maxxgrid()
