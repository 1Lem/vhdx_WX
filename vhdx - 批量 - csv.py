import subprocess
import os
import csv

def output_documents(result,outIP):
    for disk_n in result:
        try:
            cmd = []
            cmd.append(r'E:\OfficeSoftware\7-Zip\7z.exe')
            cmd.append('x')
            filename=disk_n+'.vhdx'
            cmd.append(filename)
            cmd.append("documents")
            cmd.append('-o{}'.format(disk_n))
            subprocess.call(cmd)
            outIP=outIP
            #解压完文件才会执行文件读取操作，替换result只读取磁盘编号,提前进行文件读取
            WeChat_id(disk_n,outIP)
            WXWork_id(disk_n,outIP)
            WeChat_id_csv(disk_n,outIP)
            WXWork_id_csv(disk_n,outIP)
        except:
            print(disk_n+'error!')


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



def WXWork_id(disk_n,outIP): 
    WXWork="E:\\Desktop\\vhdx\\"+ disk_n+"\\documents\\WXWork" 
    try:
        names = os.listdir(WXWork)  #路径
        i=0  #用于统计文件数量是否正确，不会写到文件里
        #train_val = open(outIP+'_'+disk_n+'_统计企业微信号 .txt','w')
        train_val = open(outIP+'_统计微信.txt','a')
        for name in names:
            index = name.rfind('.')
            name = name[:index]
            train_val.write(outIP+','+disk_n+',')
            train_val.write(name+'\n')
            i=i+1
        print (i)
    except:
        print(outIP+'_'+disk_n+'_'+'没有WXWork目录')

def WeChat_id(disk_n,outIP): 
    WeChatdir="E:\\Desktop\\vhdx\\"+ disk_n+"\\documents\\WeChat Files"   #需要校验文件夹是否存在
    try:
        names = os.listdir(WeChatdir)  #路径
        i=0  #用于统计文件数量是否正确，不会写到文件里
        #train_val = open(outIP+'_'+disk_n+'_统计微信号 .txt','w')
        train_val = open(outIP+'_统计微信.txt','a')
        for name in names:
            index = name.rfind('.')
            name = name[:index]
            train_val.write(outIP+','+disk_n+',')
            train_val.write(name+'\n')
            i=i+1
        print (i)
    except :
        print(outIP+'_'+disk_n+'_'+'没有WeChat Files目录')

def WeChat_id_csv(disk_n,outIP): 
    WeChatdir="E:\\Desktop\\vhdx\\"+ disk_n+"\\documents\\WeChat Files"   #需要校验文件夹是否存在
    try:
        names = os.listdir(WeChatdir)  #路径
        i=0  #用于统计文件数量是否正确，不会写到文件里
        #csvfilename=outIP+'_'+a+'_统计微信号'
        f= open('csvfilename.csv','a',encoding='utf-8')
        csv_writer = csv.writer(f)
        for name in names:

                index = name.rfind('.')
                name = name[:index]
                csv_writer.writerow(["outIP","disk","number"])
                csv_writer.writerow([outIP,disk_n,name])
                i=i+1
        print (i)
        f.close()
    except:
        print(outIP+'_'+disk_n+'_'+'没有WeChat Files目录')

def WXWork_id_csv(disk_n,outIP): 
    WXWorkdir="E:\\Desktop\\vhdx\\"+ disk_n+"\\documents\\WXWork"   #需要校验文件夹是否存在
    try:
        names = os.listdir(WXWorkdir)  #路径
        i=0  #用于统计文件数量是否正确，不会写到文件里
        #csvfilename=outIP+'_'+a+'_统计微信号'
        f= open('csvfilename.csv','a',encoding='utf-8')
        csv_writer = csv.writer(f)
        for name in names:

                index = name.rfind('.')
                name = name[:index]
                csv_writer.writerow(["outIP","disk","number"])
                csv_writer.writerow([outIP,disk_n,name])
                i=i+1
        print (i)
        f.close()
    except:
        print(outIP+'_'+disk_n+'_'+'没有WXWork目录')
if __name__ == '__main__':
    vhdxlist()



