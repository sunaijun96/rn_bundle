# -*- coding:utf-8 -*-
import os
import sys
import time


class Execute:
    def __init__(self, *args):
        pass

    def cmd_command(self, *args):
        print(args[0])
        self.cmd = os.system(command=args[0])
        return self.cmd

    def cd_jjlive(self, *args):
        try:
            os.chdir(r'F:\rn_bundle')   # os.chdir()指定默认路径
            print(os.getcwd())  # 返回当前进程的工作目录
        except IndexError:
            self.cmd_command('cd ' + args[0])
            print(os.getcwd())

    def cd_back(self):
        try:
            os.chdir(r'F:\rn_bundle\jjlive')   # os.chdir()指定默认路径，进入framework下
            print(os.getcwd())
        except:
            pass

    def git_branch(self):
        branch = None
        self.cmd_command('git branch')
        r = os.popen('git branch')
        for line in r.readlines():
            branch = line
            print('当前的分支名称为：\n\t\t\t  '+line)
        return branch

    def git_checkout(self, *args):
        self.git_pull()
        self.cmd_command('git branch -a')
        time.sleep(2)
        self.cmd_command('git checkout '+args[0])
        print('------分支{}切换成功------'.format(args[0]))
        self.git_branch()

    def git_pull(self):
        self.cmd_command('git pull -r')

    def git_status(self):
        self.cmd_command('git status')

    def git_push(self):
        self.cmd_command('git push')

    def git_add(self):
        self.cmd_command('git add .')

    def git_commit(self):
        text = input('输入提交内容：'+'\n')
        # com = 'git commit -m "[reviewed by wangdy] {}"'.format(text)
        # print(com)
        self.cmd_command('git commit -m "[reviewed by wangdy] {}"'.format(text))    # 提示输入需要提交的文本

    def git_log(self):
        his = self.cmd_command('git log -2')
        # print(type(his))

    def execute(self):
        a = input('需要切换分支吗？y/n\n')
        if a == 'y':
            branchName = input('分支名称：\n')
            self.git_checkout(branchName)
        else:
            self.execute()
        self.cd_jjlive()
        self.git_pull()


if __name__ == '__main__':
    exe = Execute()
    # exe.git_pull()
    exe.git_checkout('dev')