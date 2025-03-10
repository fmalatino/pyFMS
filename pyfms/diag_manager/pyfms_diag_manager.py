import ctypes
from typing import Optional

import numpy as np
from numpy.typing import NDArray

from pyfms.pyfms_data_handling import(
    setarray_Cint32,
    setscalar_Cint32,
    set_Cchar,
)

class pyFMS_diag_manager:
    
    def __init__(self, clibFMS: ctypes.CDLL = None):
        self.clibFMS = clibFMS

    def diag_init(
            self,
            diag_model_subset: Optional[int] = None,
            time_init: Optional[NDArray] = None,
            calendar_type: Optional[int] = None,
    ) -> str:
        err_msg = ""

        _cfms_diag_init = self.clibFMS.cFMS_diag_init

        diag_model_subset_c, diag_model_subset_t = setscalar_Cint32(diag_model_subset)
        time_init_p, time_init_t = setarray_Cint32(time_init)
        calendar_type_c, calendar_type_t = setscalar_Cint32(calendar_type)
        err_msg_c, err_msg_t = set_Cchar(err_msg)

        _cfms_diag_init.argtypes = [
            diag_model_subset_t,
            time_init_t,
            calendar_type_t,
            err_msg_t,
        ]
        _cfms_diag_init.restype = None

        _cfms_diag_init(
            diag_model_subset_c,
            time_init_p,
            calendar_type_c,
            err_msg_c
        )

        return err_msg_c.value.decode('utf-8')
    
    def diag_send_complete(
            self,
            diag_field_id: int,
    ) -> str:
        err_msg = ""

        _cfms_diag_send_complete = self.clibFMS.CFMS_diag_send_complete

        diag_field_id_c, diag_field_id_t = setscalar_Cint32(diag_field_id)
        err_msg_c, err_msg_t = set_Cchar(err_msg)

        _cfms_diag_send_complete.argtypes = [
            diag_field_id_t,
            err_msg_t
        ]
        _cfms_diag_send_complete.restype = None

        _cfms_diag_send_complete(diag_field_id_c, err_msg_c)

        return err_msg_c.value.decode('utf-8')
    
    def diag_set_field_init_time(
            self,
            year: int,
            month: int,
            day: int,
            hour: int,
            minute: int,
            second: Optional[int],
            tick: Optional[int],
    ) -> str:
        err_msg = ""

        _cfms_diag_set_field_init_time = self.clibFMS.cFMS_diag_set_field_init_time

        year_c, year_t = setscalar_Cint32(year)
        month_c, month_t = setscalar_Cint32(month)
        day_c, day_t = setscalar_Cint32(day)
        hour_c, hour_t = setscalar_Cint32(hour)
        minute_c, minute_t = setscalar_Cint32(minute)
        second_c, second_t = setscalar_Cint32(second)
        tick_c, tick_t = setscalar_Cint32(tick)
        err_msg_c, err_msg_t = set_Cchar(err_msg)

        _cfms_diag_set_field_init_time.argtypes = [
            year_t,
            month_t,
            day_t,
            hour_t,
            minute_t,
            second_t,
            tick_t,
            err_msg_t,
        ]
        _cfms_diag_set_field_init_time.restype = None

        _cfms_diag_set_field_init_time(
            year_c,
            month_c,
            day_c,
            hour_c,
            minute_c,
            second_c,
            tick_c,
            err_msg_c
        )

        return err_msg_c.value.decode('utf-8')
    
    def diag_set_field_timestep(
            self,
            diag_field_id: int,
            dseconds: int,
            ddays: Optional[int],
            dticks: Optional[int],
    ) -> str:
        
        err_msg = ""

        _cfms_diag_set_field_timestep = self.clibFMS.cFMS_diag_set_field_timestep

        diag_field_id_c, diag_field_id_t = setscalar_Cint32(diag_field_id)
        dseconds_c, dseconds_t = setscalar_Cint32(dseconds)
        ddays_c, ddays_t = setscalar_Cint32(ddays)
        dticks_c, dticks_t = setscalar_Cint32(dticks)
        err_msg_c, err_msg_t = set_Cchar(err_msg)

        _cfms_diag_set_field_timestep.argtypes = [
            diag_field_id_t,
            dseconds_t,
            ddays_t,
            dticks_t,
            err_msg_t,
        ]
        _cfms_diag_set_field_timestep.restype = None

        _cfms_diag_set_field_timestep(
            diag_field_id_c,
            dseconds_c,
            ddays_c,
            dticks_c,
            err_msg_c
        )

        return err_msg_c.value.decode('utf-8')
    
    def diag_advance_field_time(
            self,
            diag_field_id: int,
    ):
        _cfms_diag_advance_field_time = self.clibFMS.cFMS_diag_advance_field_time

        diag_field_id_c, diag_field_id_t = setscalar_Cint32(diag_field_id)

        _cfms_diag_advance_field_time.argtypes = [diag_field_id_t]
        _cfms_diag_advance_field_time.restype = None

        _cfms_diag_advance_field_time(diag_field_id_c)

    def diag_set_time_end(
            self,
            year: Optional[int],
            month: Optional[int],
            day: Optional[int],
            hour: Optional[int],
            minute: Optional[int],
            second: Optional[int],
            tick: Optional[int],
            err_msg: Optional[str],
    ):
        _cfms_set_time_end = self.clibFMS.diag_set_time_end

        year_c, year_t = setscalar_Cint32(year)
        month_c, month_t = setscalar_Cint32(month)
        day_c, day_t = setscalar_Cint32(day)
        hour_c, hour_t = setscalar_Cint32(hour)
        minute_c, minute_t = setscalar_Cint32(minute)
        second_c, second_t = setscalar_Cint32(second)
        tick_c, tick_t = setscalar_Cint32(tick)
        err_msg_c, err_msg_t = set_Cchar(err_msg)

        _cfms_set_time_end.argtypes = [
            year_t,
            month_t,
            day_t,
            hour_t,
            minute_t,
            second_t,
            tick_t,
            err_msg_t,
        ]
        _cfms_set_time_end.restype = None

        _cfms_set_time_end(
            year_c,
            month_c,
            day_c,
            hour_c,
            minute_c,
            second_c,
            tick_c,
            err_msg_c,
        )

    
