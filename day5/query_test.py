# 查询示例

# 1） 导入pymsql模块
import pymysql

# 2） 创建数据库连接
host='localhost'   # 主机
user='root'        # 用户名
passwd='666666'    # 用户密码
dbname='eshop'     # 库名称
conn=pymysql.connect(host,user,passwd,dbname)   # 返回一个连接对象

# 3） 创建游标(cursor)对象
cursor=conn.cursor()

# 4） 使用游标对象提供的方法，执行SQL语句
sql='select * from orders'
cursor.execute(sql)
result=cursor.fetchall()     # 提取所有数据

# 5） 打印数据
for r in result:       # result 返回的是元组
    order_id=r[0]    # 订单编号
    cust_id=r[1]     # 客户编号
    amt=r[5]         # 订单金额
    print("订单编号：%s,客户编号：%s,金额：%.2f"\
        %(order_id,cust_id,amt))
    


# 5） 关闭游标
cursor.close()

# 6） 关闭数据库连接对象
conn.close()