# -*- coding: utf-8 -*-
# convert a date to string arab+.
# -------------------------------------------------------------
# Arab              paython code
# -------------------------------------------------------------

import datetime

ONES_19_ARA_day = ['������' , '������', '������', '������', '������', '������', '������', '������',
          '������', '������', '������', '������ ���',   '������ ���', '������ ���', '������ ���',
          '������ ���', '������ ���', '������ ���', '������ ���', '������ ��� ']
ONES_19_ARA_year = ['' , '����', '�����', '�����', '�����', '����', '���', '����',
          '������', '����', '����', '���� ���',   '���� ���', '����� ���', '����� ���',
          '���� ���', '��� ���', '���� ���', '������ ���', '���� ��� ']
ONES_9_ARA = ['����', '�����', '����', '����', '���', '��', '���', '����', '���']
TENS_ARA  = ['�����', '������', '������', '�����', '����', '�����', '������', '�����']
HUNDREDS_THOUSANDS_ARA = ['���', '�����', '���', '�����' , '����']
MONTHS_ARA = ['�����', '�����', '����', '�����', '���', '����', '������', '���', '������', '������', '������', '������']


def _convert_dateTostr_Ar(val):

    '''(str_day+ ' �� ��� '+ str_month+ ' ��� ' + str_year)

    :param val: type datetime
    :return: string contains the date in arabic letters
    '''

    # Extracting day, month, year
    day, month, year = (val.day, val.month, val.year)

    str_day = ''
    str_month = MONTHS_ARA[month - 1] # For months
    str_year = ''

    #------------------------
    if day == 1:
        str_day = ONES_19_ARA_day[0]
    elif day < 20:
        str_day = ONES_19_ARA_day[day]
    else:
        if (day % 10) == 0 :
            str_day = '��' + TENS_ARA[(day / 10) - 2]
        else:
            str_day= ONES_19_ARA_day[(day % 10)] + ' �' + '��' + TENS_ARA[day / 10 - 2]
    # pour l annee -------------------------------------------------
    # ---------------------------------------------------------
    if year > 999:
        if year / 1000 < 3:
            str_year=HUNDREDS_THOUSANDS_ARA[1 + year / 1000]
        else:str_year= ONES_9_ARA[year / 1000 - 1] + ' ' + HUNDREDS_THOUSANDS_ARA[4]

    # Hundrends in year
    if year > 99:
        if (len(str_year) >= 3) and ((year % 1000)/100 !=0): str_year=str_year+ ' �'
        if (year % 1000)/100 in (1,2) :
            str_year=str_year + HUNDREDS_THOUSANDS_ARA[(year % 1000) / 100 - 1]
        else :
            if ((year % 1000)/100) != 0:
                str_year=str_year  + ONES_9_ARA[(year % 1000) / 100 - 1] + HUNDREDS_THOUSANDS_ARA[0]

    # Tens in year
    if (year % 100)!= 0:
        if (len(str_year) >= 3) and ((year % 100)%10 !=0): str_year=str_year+ ' �'
        if (year % 100) ==10:
                str_year = str_year  +  '����'
        else:
            if ((year % 100)%10!= 0) :
                    if (year % 100)<20:
                     str_year = str_year + ONES_19_ARA_year[year % 100]
                    else:
                        str_year = str_year + ONES_9_ARA[(year % 100)% 10  -1] + ' �' + TENS_ARA[(year % 100) / 10 - 2]
            else:
                if (year % 100)%10 == 0:
                    str_year = str_year + TENS_ARA[(year%100) / 10  - 2]


    return (str_day+ ' �� ��� '+ str_month+ ' ��� ' + str_year)+'.'

