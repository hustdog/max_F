import os
import pandas as pd

#os.chidr()方法用于改变当前工作目录到指定的路径
os.chdir(r'D:\documents\my work\微生物固化钙质砂实验\MICP(勿删)2020.1.4\探究固化时间—6组每轮4天\5')
#获取当前的工作目录
file_chdir=os.getcwd()
#获取指定目录下所有的txt文件名称
#获取工作路径下txt文件的文件名
filetxt_list = []
#os.walk()方法用于通过在目录树中游走输出在目录中的文件名，向上或者向下，此方法是一个简单易用的文件，目录遍历器，可以帮助我们高校的处理文件，目录方面的事情
#root所指地是当前正在遍历的这个文件夹本身的地址
#dir是一个list，内容是该文件夹中所有的文件夹的名字
#files同样是list，内容是该文件夹中所有的文件
for root,dirs,files in os.walk(file_chdir):
    for file in files:
        if os.path.splitext(file)[1]== '.txt':
            filetxt_list.append(file)
# print(filetxt_list)
#导入文件
data = pd.DataFrame()
txt_list = []
maximun_list = []

for txt in filetxt_list:
    data = pd.read_csv(txt,header=0,encoding='gbk')
    #print(data)
    maximun = pd.DataFrame(data)['Load (kN)'].max()
    txt_list.append(txt.split('.')[0])
    maximun_list.append(maximun)
data_total = dict(zip(txt_list, maximun_list))#将两个list合并为一个字典，为下一步创建df数据库做准备
print(data_total)
# data_total = {'编号'=txt_list,'Load (kN)'=maximun_list}
df_total = pd.DataFrame.from_dict(data_total, orient='index',columns=['Load (kN)'])#使用DataFrame.from_dict函数创建df，一个key只有一个value的字典如果直接转化成数据框会报错

#↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓报错情况下的解决办法有三种：↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓
# 1、使用DataFrame函数时指定字典的索引index
# import pandas as pd
#
# my_dict = {'i': 1, 'love': 2, 'you': 3}
# my_df = pd.DataFrame(my_dict,index=[0]).T
#
# print(my_df)
#
# 2、把字典dict转为list后传入DataFrame
# import pandas as pd
#
# my_dict = {'i': 1, 'love': 2, 'you': 3}
# my_list = [my_dict]
# my_df = pd.DataFrame(my_list).T
#
# print(my_df)
#
# 3、 使用DataFrame.from_dict函数
#
# import pandas as pd
#
# my_dict = {'i': 1, 'love': 2, 'you': 3}
# my_df = pd.DataFrame.from_dict(my_dict, orient='index')
#
# print(my_df)
#↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑报错情况下的解决办法有三种：↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑

df_total.to_excel('excel_output.xls')

# 将索引值改为样品编号，并增加一列新索引值
# df_total = df_total.reset_index().rename(columns={'index':'number'})
# df_total.to_excel('excel_output2.xls')
print(df_total)

