import ctypes

import numpy as np
from numpy.typing import NDArray

from pyfms.pyfms_data_handling import setarray_Cdouble, setscalar_Cint32


def get_grid_area(
    nlon: int,
    nlat: int,
    lon: NDArray,
    lat: NDArray,
    clibFMS: ctypes.CDLL,
) -> NDArray:

    _cfms_get_grid_area = clibFMS.cFMS_get_grid_area

    area = np.empty(shape=nlon * nlat, dtype=np.float64, order="C")

    nlon_c, nlon_t = setscalar_Cint32(nlon)
    nlat_c, nlat_t = setscalar_Cint32(nlat)
    lon_p, lon_t = setarray_Cdouble(lon)
    lat_p, lat_t = setarray_Cdouble(lat)
    area_p, area_t = setarray_Cdouble(area)

    _cfms_get_grid_area.argtypes = [
        nlon_t,
        nlat_t,
        lon_t,
        lat_t,
        area_t,
    ]
    _cfms_get_grid_area.restype = None

    _cfms_get_grid_area(
        nlon_c,
        nlat_c,
        lon_p,
        lat_p,
        area_p,
    )

    return area
