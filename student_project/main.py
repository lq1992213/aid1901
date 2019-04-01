
# file:main.py
from menu import show_menu
from student_indo import *

def main():
    infos=[]   # 此列表用来保存学生信息的数据
    while True:
        show_menu()
        s=input("请选择：")
        if s=='1':
            infos+=input_student()
            print("添加成功")
        elif s=='2':
            output_student(infos)  
        elif s=='3':   
            delete_student(infos)   # 删除信息
        elif s=='4':
            modify_student_score(infos)    # 修改成绩
        elif s=='5':
            print("按学生成绩高-低显示学生信息")
            output_student_by_score_reduce(infos)
        elif s=='6':
            print("按学生成绩低-高显示学生信息")
            output_student_by_score_increase(infos)
        elif s=='7':
            print("按学生年龄高-低显示学生信息")
            output_student_by_age_reduce(infos)
        elif s=='8':
            print("按学生年龄低-高显示学生信息")
            output_student_by_age_increase(infos)
        elif s=='9':
            infos=read_from_file()     # 从文件中读取数据
        elif s=='10':
            save_to_file(infos)        # 保存到文件
        elif s=='q':
            break
        
main()
   