# -*-coding:utf-8-*- 
print("--------------------------------------------！")
import os


# files = list();
def modifySuffixName(pathName, oldSuffixName, newSuffixName):
    if os.path.exists(pathName):
        fileList = os.listdir(pathName)
        print(fileList)
        for fileName in fileList:
            file_name, file_end = os.path.splitext(fileName)
            if file_end == oldSuffixName:
                newname = file_name + newSuffixName
                finallyOrdName = (os.path.join(pathName, fileName))
                finallyNewName = (os.path.join(pathName, newname))
                os.rename(finallyOrdName, finallyNewName)


modifySuffixName(r"C:\Users\Administrator\Documents\excel模板", ".xlsx", ".xls")
