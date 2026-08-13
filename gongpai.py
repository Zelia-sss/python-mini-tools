import xlrd
import os
from MyQR import myqr

path=r"D:\python\yequbiancheng\资料.xlsx"
data=xlrd.open_workbook(path)
table=data.sheets()[0]
allNames=table.col_values(1)[1:]
allNumbers=table.col_values(3)[1:]

pathFile=r"D:\python\yequbiancheng\Selfie"
allitem=os.listdir(pathFile)
for item in allitem:
    filename=item.split(".")[0]
    if filename in allNames:
        index=allNames.index(filename)
        phonenumber=allNumbers[index]
        intnumbver=int(phonenumber)

        myqr.run(words=str(intnumbver),
                 save_name=item,
                 picture=f"D:\python\yequbiancheng\Selfie\{item}",
                 colorized=True,
                 version=10)


