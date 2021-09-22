import pymysql

db = pymysql.connect(
host="192.168.44.39",
port=3306,
user="linchubin",
passwd="linchubin123456",
database='ezsale-warehouse-test',
charset='UTF8')

cursor = db.cursor()# 返回字典数据类型  cursor=pymysql.cursors.DictCursor
# 执行
sql = "SELECT * FROM wh_goods_shelves` WHERE `encode` LIKE '%S11-11-181%';"
# execute函数可以加格式化字符参数
res = cursor.execute(sql) #返回值r为受影响的行数
ret1 = cursor.fetchall()
print("res:{}".format(res))
print("ret1:{}".format(ret1))
print(type(ret1))

# 执行结束后要关闭光标和连接
cursor.close()
db.close()