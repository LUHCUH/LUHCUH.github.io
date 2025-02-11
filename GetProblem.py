import urllib
import sys
import urllib.request
from bs4 import BeautifulSoup

def GetNextCommand():
    pass
class Command:
    def __init__(self):
        Command.cnt=-1
        Command.s=sys.argv
    def have(self=None):
        if(Command.cnt+1==len(Command.s)):
            return False
        else:
            return True
    def Get(self=None):
        if(not Command.have()):
            return None;
        Command.cnt+=1
        return Command.s[Command.cnt]
command=Command()
def NewPage(title,name,website):
    print(f"创建 {website} 的题目 {title}")
def RelateUrl(url):
    print(f"解析地址：{url} ")
    if "https://www.luogu.com.cn/problem" in url:
        title=BeautifulSoup(urllib.request.urlopen(url).read(), 'lxml').title.string
        title=title[0:-5]
        print(title)
        s=str.split(url,'/')[-1]
        if s[0]=="P":
            NewPage(title,s,"LG")
        elif s[0:2]=="CF":
            NewPage(title,s,"CF")
        elif s[0:2]=="AT":
            NewPage(title,s,"AT")
        elif s[0:2]=="SP":
            NewPage(title,s,"SP")
        elif s[0:3]=="UVA":
            NewPage(title,s,"UVA")
        else:
            print(f"无法解析这是那里的题目")
    elif "47.92.197.167:5283/contest" in url:
        s=str.split(url,'/')
        if s[-2]=="contest":
            print(f"你这个比赛链接，是足以不支持你传建题目的！")
        if s[-2]=="problem":
            NewPage(chr(ord('A')+int(s[-1])-1),chr(ord('A')+int(s[-1])-1),"ACCNOI")
    elif "codeforces.com/problemset/problem":
        s=str.split(url,'/')
        name="CF"+s[-2]+s[-1]
        title=BeautifulSoup(urllib.request.urlopen("https://www.luogu.com.cn/problem/"+name).read(), 'lxml').title.string
        title=title[0:-5]
        NewPage(title,s,"CF")
def main():
    while(command.have()):
        s=command.Get()
        if s=="-new" or s=="-n":
            print(s)
            RelateUrl(command.Get())
if __name__ == "__main__":
    main()