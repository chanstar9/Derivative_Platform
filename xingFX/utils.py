from dateutil.relativedelta import relativedelta, FR, TH ,MO
import datetime as dt
import calendar
import pandas as pd

class kfx_calendar:

    def __init__(self):
        self.now_date= int(dt.datetime.now().strftime("%Y%m%d"))

    def mat_month(self, mat_from_now=1):

        """
        nw_date = int(dt.datetime.now().strftime("%Y%m%d"))
        fst_mon = (dt.datetime.now() + relativedelta(weekday=MO(1))).date()
        fst_thur = (dt.datetime.now() + relativedelta(weekday=TH(1))).date()

        scd_mon = (dt.datetime.now() + relativedelta(weekday=MO(2))).date()
        scd_thur =  (dt.datetime.now() + relativedelta(weekday=TH(2))).date()
        """
        c = calendar.Calendar(firstweekday=calendar.SUNDAY)

        dt_now = dt.datetime.now()
        year = dt_now.year;
        month = dt_now.month;
        this_quarter = pd.Timestamp(dt_now).quarter
        #TODO
        #mat from now 이용해서 현재 대비 이전/ 이후 만기 구하기
        if this_quarter== 1 :
            month = 4 * 3
            year = year-1
        else:
            month = (this_quarter-1)*3
            year = year

        monthcal = c.monthdatescalendar(year, month)

        prev_mat_mondays = [day for week in monthcal for day in week if \
                             day.weekday() == calendar.MONDAY and \
                             day.month == month]

        prev_mat_month = [day for week in monthcal for day in week if \
                             day.weekday() == calendar.MONDAY and \
                             day.month == month]

        return prev_mat_month

    def prev_mat_week_monday(self):
        mat_mon_list = self.mat_month()
        fst_mon = int(mat_mon_list[1].strftime("%Y%m%d"))-3
        return fst_mon

    def prev_mat_day(self):
        mat_mon_list = self.mat_month()
        mat_day = int(mat_mon_list[1].strftime("%Y%m%d"))
        return mat_day

    def prev_mat_week_friday(self):
        mat_mon_list = self.mat_month()
        mat_week_friday = int(mat_mon_list[1].strftime("%Y%m%d"))+1
        return mat_week_friday

    def fst_monday(self):
        return self.prev_mat_week_monday()

#Todo 조건에 따라 선옵 코드 return
class code_maker:
    pass

