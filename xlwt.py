# -*-coding:utf-8-*- 
print("--------------------------------------------！")
import os
import xlrd
import xlwt
import xlutils
from xlutils.copy import copy

#files = list(); 
def traverseFile(pathName): 
    if os.path.exists(pathName):
        fileList = os.listdir(pathName)
        print(type(fileList))
        for fileName in fileList:
            file_name, file_end = os.path.splitext(fileName)
            if os.path.splitext(fileName)[1] == ".xls":
                #print(os.path.join(pathName,fileName))
                finallyname = (os.path.join(pathName,fileName))
                try:   
                    # 打开想要更改的excel文件
                    old_excel = xlrd.open_workbook(finallyname)
                    # 将操作文件对象拷贝，变成可写的workbook对象
                    new_excel = copy(old_excel)
                    # 获得第一个sheet的对象
                    ws = new_excel.get_sheet(0)
                    new_excel.save(finallyname)
                except Exception as e:
                    print("报错了，请检查{}文件是否打开着".format(finallyname))
                    print('出现异常:', e)
                    raise e
                break

traverseFile(r"C:\Users\Administrator\Documents\excel模板")

