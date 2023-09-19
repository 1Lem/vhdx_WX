import subprocess
import os
import csv

def output_documents(result,outIP):
	for a in result:
		cmd = []
		cmd.append(r'E:\OfficeSoftware\7-Zip\7z.exe')
		cmd.append('x')
		filename=a+'.vhdx'
		cmd.append(filename)
		cmd.append("documents")
		cmd.append('-o{}'.format(a))
		subprocess.call(cmd)
		outIP=outIP
		#先解压完所有文件才会执行文件读取操作
	WeChat_id(result,outIP)
	WXWork_id(result,outIP)
	WeChat_id_csv(result,outIP)
	WXWork_id_csv(result,outIP)


def vhdxlist():
    result = [] 
    outIP=input('input outIP:')
    with open(r'统计.txt' ,'r') as f:
        for line in f:
         result.append(line.strip().split(',')[0])  #a.append(b)：是将b原封不动的追加到a的末尾上，会改变a的值
            #strip()用于移除字符串头尾指定的字符（默认为空格或者换行符）或字符序列
        print(result) 
    print(result[0])
    print(outIP)
    output_documents(result,outIP)



def WXWork_id(result,outIP): 
    for a in result:
        WXWork="E:\\Desktop\\vhdx\\"+ a+"\\documents\\WXWork" 
        try:
            names = os.listdir(WXWork)  #路径
            i=0  #用于统计文件数量是否正确，不会写到文件里
            train_val = open(outIP+'_'+a+'_统计企业微信号 .txt','w')
            for name in names:
                index = name.rfind('.')
                name = name[:index]
                train_val.write(name+'\n')
                i=i+1
            print (i)
        except:
            print(outIP+'_'+a+'_'+'没有WXWork目录')

def WeChat_id(result,outIP): 
    for a in result:
        WeChatdir="E:\\Desktop\\vhdx\\"+ a+"\\documents\\WeChat Files"   #需要校验文件夹是否存在
        try:
            names = os.listdir(WeChatdir)  #路径
            i=0  #用于统计文件数量是否正确，不会写到文件里
            train_val = open(outIP+'_'+a+'_统计微信号 .txt','w')
            for name in names:
                index = name.rfind('.')
                name = name[:index]
                train_val.write(name+'\n')
                i=i+1
            print (i)
        except :
            print(outIP+'_'+a+'_'+'没有WeChat Files目录')

def WeChat_id_csv(result,outIP): 
    for a in result:
        WeChatdir="E:\\Desktop\\vhdx\\"+ a+"\\documents\\WeChat Files"   #需要校验文件夹是否存在
        try:
            names = os.listdir(WeChatdir)  #路径
            i=0  #用于统计文件数量是否正确，不会写到文件里
            #csvfilename=outIP+'_'+a+'_统计微信号'
            f= open('csvfilename.csv','w',encoding='utf-8')
            csv_writer = csv.writer(fF)
           # 3. 构建列表头
            #csv_writer.writerow(["outIP","disk","number"])
            #train_val = open(outIP+'_'+a+'_统计微信号 .txt','w')
            for name in names:

                    index = name.rfind('.')
                    name = name[:index]
                    #train_val.write(name+'\n')
                    # 2. 基于文件对象构建 csv写入对象
                    #csv_writer = csv.writer(f)
                    # 3. 构建列表头
                    csv_writer.writerow(["outIP","disk","number"])
                    # 4. 写入csv文件内容
                    csv_writer.writerow([outIP,a,name])
                    i=i+1
            print (i)
        except:
            print(outIP+'_'+a+'_'+'没有WeChat Files目录')

def WXWork_id_csv(result,outIP): 
    for a in result:
        WXWorkdir="E:\\Desktop\\vhdx\\"+ a+"\\documents\\WXWork"   #需要校验文件夹是否存在
        try:
            names = os.listdir(WXWorkdir)  #路径
            i=0  #用于统计文件数量是否正确，不会写到文件里
            #csvfilename=outIP+'_'+a+'_统计微信号'
            f= open('csvfilename.csv','w',encoding='utf-8')
            csv_writer = csv.writer(fF)
           # 3. 构建列表头
            #csv_writer.writerow(["outIP","disk","number"])
            #train_val = open(outIP+'_'+a+'_统计微信号 .txt','w')
            for name in names:

                    index = name.rfind('.')
                    name = name[:index]
                    #train_val.write(name+'\n')
                    # 2. 基于文件对象构建 csv写入对象
                    #csv_writer = csv.writer(f)
                    # 3. 构建列表头
                    csv_writer.writerow(["outIP","disk","number"])
                    # 4. 写入csv文件内容
                    csv_writer.writerow([outIP,a,name])
                    i=i+1
            print (i)
        except:
            print(outIP+'_'+a+'_'+'没有WXWork目录')
if __name__ == '__main__':
    vhdxlist()



