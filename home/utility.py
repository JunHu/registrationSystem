#!/usr/bin/env python
# coding=utf-8

import sys
import os
import xlwt
from registrationSystem.settings import TMP_FILES_PATH
import datetime

def cell_style(horizontal,vertical):
    """
    为CELL添加水平居中和垂直居中
    """
    alignment = xlwt.Alignment()
    if horizontal:
        alignment.horz = xlwt.Alignment.HORZ_CENTER
    elif vertical:
        alignment.vert = xlwt.Alignment.VERT_CENTER
    style = xlwt.XFStyle() # Create Style
    style.alignment = alignment # Add Alignment to Style
    return style


def info_xls_baseinformation_gen(class_type):
    workbook = xlwt.Workbook(encoding='utf-8')
    worksheet = workbook.add_sheet('sheet1')
    style = cell_style(horizontal=True,vertical=True)
    # generate header
    worksheet.write_merge(0, 0, 0, 10, '大连理工大学'+class_type,style)

    # generate body
    worksheet.write_merge(1, 1, 0, 0, '姓名')
    worksheet.col(0).width = len('姓名') * 200
    worksheet.write_merge(1, 1, 1, 1, '学号')
    worksheet.col(1).width = len('学号') * 400
    worksheet.write_merge(1, 1, 2, 2, '性别')
    worksheet.write_merge(1, 1, 3, 3, '电话')
    worksheet.col(3).width = len('电话') * 800
    worksheet.write_merge(1, 1, 4, 4, '邮箱')
    worksheet.col(4).width = len('邮箱') * 800
    worksheet.write_merge(1, 1, 5, 5, '学部')
    worksheet.col(5).width = len('学部') * 800
    worksheet.write_merge(1, 1, 6, 6, '专业')
    worksheet.col(6).width = len('专业') * 800
    worksheet.write_merge(1, 1, 7, 7, '第一志愿')
    worksheet.col(7).width = len('第一志愿') * 800
    worksheet.write_merge(1, 1, 8, 8, '第二志愿')
    worksheet.col(8).width = len('第二志愿') * 800
    worksheet.write_merge(1, 1, 9, 9, '自我介绍')
    worksheet.col(9).width = len('自我介绍') * 1000
    return worksheet, workbook

def info_xls_baseinformation(request,apply_set,class_type):
    """
    """
    def _format_number(i):
        i = str(i)
        i = '0' * (4-len(i)) + i
        return i

    xls_obj, workbook = info_xls_baseinformation_gen(class_type)

    # _index = 1
    _number= 1
    for apply_obj in apply_set:

        row = 1 + _number
        xls_obj.write(row, 0, unicode(apply_obj.student_name)) 
        xls_obj.write(row, 1, unicode(apply_obj.student_id)) 
        xls_obj.write(row, 2, unicode(apply_obj.get_sex_display())) 
        xls_obj.write(row, 3, unicode(apply_obj.tel_num)) 
        xls_obj.write(row, 4, unicode(apply_obj.email)) 
        xls_obj.write(row, 5, unicode(apply_obj.get_apartment_display())) 
        xls_obj.write(row, 6, unicode(apply_obj.get_college_display())) 
        xls_obj.write(row, 7, unicode(apply_obj.get_wish_first_display())) 
        xls_obj.write(row, 8, unicode(apply_obj.get_wish_second_display())) 
        xls_obj.write(row, 9, unicode(apply_obj.self_introduction)) 
        # _index += 1
        _number+= 1
    # write xls file
    filename = "%s%s.xls"%(str(datetime.date.today().year)+"大连理工大学",class_type+"招新统计表")
    save_path = os.path.join(TMP_FILES_PATH,filename)
    print save_path
    workbook.save(save_path)
    return "/media/tmp/"+filename

