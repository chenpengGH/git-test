#coding:utf8
# 时间工具
import pandas as pd
import datetime
import json

import requests


def judgedate(datenum):
    """
    检查具体日期是否为节假日，工作日对应结果为 0, 休息日对应结果为 1, 节假日对应的结果为 2；
    :param datenum:
    :return:
    """
    url='http://tool.bitefu.net/jiari/?d={}'.format(datenum)
    html = requests.get(url=url).content
    data = json.loads(html.decode('utf-8'))
    # value=data['data']
    return data

def weekend(day):
    weekday = datetime.datetime.strptime(day, '%Y%m%d').weekday()
    if weekday == 5:
        return True
    else:
        return False

def getnum(datenum):
    date = datetime.datetime.strptime(datenum, '%Y%m%d')
    num = date.timetuple().tm_yday
    return num

def getBetweenDay(begin_date, end_date):
    date_list = []
    begin_date = datetime.datetime.strptime(begin_date, '%Y%m%d')
    end_date = datetime.datetime.strptime(end_date, '%Y%m%d')
    while begin_date <= end_date:
        date_str = begin_date.strftime("%Y%m%d")
        date_list.append(date_str)
        begin_date += datetime.timedelta(days=1)
    return date_list

def get_date_match_list(begin_date, end_date):
    date_list = getBetweenDay(begin_date, end_date)
    num_list = []
    match_list = []
    remark_list = []
    day = 0
    for date in date_list:
        print(date)
        num=getnum(date)
        match = num
        value = judgedate(date)
        remark = ''
        if value == 0:
            match = match - day
            remark = '工作日'
        elif value == 1:
            day += 1
            match = 0
            remark = '休息日'
        elif value == 2:
            day += 1
            match = 0
            remark = '法定节假日'


        # if value == 0:
        #     match = match - day
        #     remark = '工作日'
        # elif value == 1:
        #     day += 1
        #     match = 0
        #     remark = '法定节假日'
        # elif value == 2:
        #     match = match - day
        #     remark = '调休工作日'
        # elif value == 3:
        #     is_saturday = weekend(date)
        #     if is_saturday:
        #         match = match - day
        #         remark='周六加班'
        #     else:
        #         day += 1
        #         match = 0
        #         remark = '周日休息'
        num_list.append(num)
        match_list.append(match)
        remark_list.append(remark)
    
    date_match_list = pd.DataFrame({'date': date_list, 'num': num_list, 'match': match_list, 'remark': remark_list})
    return date_match_list

def main():
    """
    主函数
    :return:
    """
    date_match_list = get_date_match_list('20200101','20201231')
    # dataset写入csv
    date_match_list.to_csv('date_match.csv')

if __name__ == '__main__':
    main()

    # url = 'http://tool.bitefu.net/jiari/?d=20200101'
    # html = requests.get(url=url).content
    # print(html.decode('utf-8'))