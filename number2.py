__author__ = 'may'
#/usr/bin/env python
# -*- coding: utf-8 -*-

1 #!/usr/bin/env python
2
 3'makeTextFile.py -- create text file'
#第1–3行
#UNIX 启动行之后是模块的文档字符串。应该坚持写简洁并有用的文档字符串。
#这里我们写 的有点短,不过对这段代码已经够用。(建议读者看一下标准库中 cgi 模块的文档字符串,那 是一个很好的示例
 4
 5import os
 6 ls = os.linesep
#第5–6行
#之后我们导入 os 模块, 在第 6 行我们为 os.linesep 属性取了一个新别名。这样做一方 面可以缩短变量名, 另一方面也能改善访问该变量的性能。
  # 核心技巧:使用局部变量替换模块变量
#类似 os.linesep 这样的名字需要解释器做两次查询:(1)查找 os 以确认它是一个模块,
#(2)在这个模块中查找 linesep 变量。因为模块也是全局变量, 我们多消耗了系统资源。
#如 果你在一个函数中类似这样频繁使用一个属性,我们建议你为该属性取一个本地变量别名。
#变 量查找速度将会快很多--在查找全局变量之前, 总是先查找本地变量。 这也是一个让你的
#程序跑的更快的技巧: 将经常用到的模块属性替换为一个本地引用。代码跑得更快,而也不用 老是敲那么长的变量名了
#。在我们的代码片段中,并没有定义函数,所以不能给你定义本地别 名的示例。不过我们有一个全局别名,至少也减少了一次名字查询
 7
8# get filename
9 while True:
10
11 if os.path.exists(fname):
12 print "ERROR: '%s' already exists" % fname
13 else:
14 break
#第 8–14行
#显然这是一个无限循环, 也就是说除非我们在 while 语句体􏰀供 break 语句, 否则它会 一直循环下去。
#while 语句根据后面的表达式决定是否进行下一次循环,而 True 则确保它一直循环下去。
#第 10-14 行􏰀示用户输入一个未使用的文件名。 raw_input() 内建函数接受一个“􏰀示 字符串”参
# 数,作为对用户的􏰀示信息。raw_input()返回用户输入的字符串,也就是为 fname
赋值。 如果用户不小心输入了一个已经存在的文件的名字,我们要􏰀示这个用户重新输入另一 个名字
#。 os.path.exists() 是 os 模块中一个有用的函数,
#帮助我们确认这一点。 当有输 入一个不存在的文件名时, os.path.exists()
#才会返回 False, 这时我们中断循环继续下面 的代码。

15
16 # get file content (text) lines
17 all = []
18 print "\nEnter lines ('.' by itself to quit).\n"
19
20 # loop until user terminates input
21 while True:
22 entry = raw_input('> ')
23 if entry == '.':
24 break
25 else:
26 all.append(entry)
27
28 # write lines to file with proper line-ending
29 fobj = open(fname, 'w')
30 fobj.writelines(['%s%s' % (x, ls) for x in all])
31 fobj.close()
32 print 'DONE!'



第16–26 行
这部分代码􏰀供用户指令,引导用户输入文件内容,一次一行。我们在第十七行初始化了 列表 all,它用来保存每一行文本。
第 21 行开始另一个无限循环, 􏰀示用户输入每一行文本, 一行仅输入一个句点 '.' 表示输入结束。 23-26 行的 if-else
语句判断是否满足结束条件 以中止循环(行 24), 否则就再添加新的一行。
第 28–32 行
现在所有内容都保存在内存当中, 我们需要将它们保存到文件。 第 29 行打开文件准备进 行写操作,
第 30 行将内存中的内容逐行写入文件。每个文件都需要一个行结束符(或文件结束 字符)。 第 30 行的结构称为列表解析,
它做以下事: 对我们文件的每一行, 根据程序运行
平台添加一个合适的行结束符。 '%s%s' 为每一行添加行结束符,(x, ls)表示每一行及其行 结束符,对 Unix 平台,是'\n',
对 DOS 或 win32 平台,则是 '\r\n'。通过使用 os.lineseq , 我们不必关心程序运行在什么平台,也不必要根据不同的平
台决定使用哪种行结束符。 文件 对象的 writelines() 方法接收包含行结束符的结果列表,并将它写入文件
