from student import Student

def input_student():
    L=[]
    while True:
        n=input("请输入姓名：")
        if not n:
            break
        try:
            a=int(input("请输入年龄："))
            if not a:
                break
            s=int(input("请输入成绩："))
            if not s:
                break
        except ValueError:
            print("您输入有误,请重新输入:")
        d=Student(n,a,s)
        L.append(d)
    return L

def output_student(L):
    print("+-------------+-------------+-------------+")
    print("|    姓名     |     年龄    |     成绩    |")
    print("+-------------+-------------+-------------+")
    for d in L:
        name,age,score=d.get_infos()
        sn=name
        sa=str(age)       # 将年龄绑成字符串
        ss=str(score)     # 将成绩绑成字符串
        print('|'+sn.center(13)+'|'+sa.center(13)+'|'+ss.center(13)+'|')
    print("+-------------+-------------+-------------+")


def delete_student(L):
    name=input("请输入删除学生的姓名：")
    for i in range(len(L)):      # i代表索引
        d=L[i]
        if d.get_name()==name:
            del L[i]
            print("成功删除了",name)
            return
    print("这个学生不存在，删除失败")


def modify_student_score(L):
    name=input("请输入修改成绩的学生姓名：")
    for i in range(len(L)):
        d=L[i]
        if d.get_name()==name:
            score=int(input("请输入要修改学生的成绩："))
            d.set_score(score)
            print("修改成绩成功")
            return
    print("这个学生不存在，修改失败")


def output_student_by_score_reduce(L):
    def get_score(d):
        return d.get_score()
    L = sorted(L, key=get_score,reverse=True)
    output_student(L)
 
def output_student_by_score_increase(L):
    def get_score(d):
        return d.get_score()
    L = sorted(L,key=get_score,reverse=False)
    output_student(L)

def output_student_by_age_reduce(L):
    L = sorted(L, key=lambda d: d.get_age(),reverse=True)
    output_student(L)

def output_student_by_age_increase(L):
    L = sorted(L, key=lambda d: d.get_age(),reverse=False)
    output_student(L)


def read_from_file():
    L = []
    try:
        f = open('si.txt')
        for line in f:
            s = line.strip()  # 去掉末尾换行符
            n, a, s = s.split(',')  # ['xiaozhang', '20', '100']
            a = int(a)
            s = int(s)
            stu = Student(n, a, s)  # 创建对象用来记住信息
            L.append(stu)
        f.close()
        print("读取文件成功!")
        return L
    except OSError:
        print("读取文件失败")

def save_to_file(L):
    try:
        fw = open("si.txt", 'w')
        # 保存
        for s in L:
            # 方法2 把文件交给学生，由学生信息来写
            s.write_infos(fw)


            # 方法1 在当前函数来写文件
            # fw.write(s.get_name())
            # fw.write(',')
            # fw.write(str(s.get_age()))
            # fw.write(',')
            # fw.write(str(s.get_score()))
            # fw.write('\n')

        fw.close()
        print("保存成功")
    except OSError:
        print("保存失败")


