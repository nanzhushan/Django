#coding:utf8
danger = ('rm', 'reboot', 'init ', 'shutdown')
arg = 'rm'
argcheck = arg not in danger


# host = ('11','33','44','78')
# tgt = '33'
# tgtcheck = tgt  in host

tgtcheck = "5"

# if tgtcheck:
#     print "有值"
# else:
#     print "没有值"

print bool(tgtcheck)

# if argcheck and tgtcheck:     ##如果两个check都为真，就执行语句。
#     print "执行语句，不是危险命令，主机也存在"
#
# elif not tgtcheck:   ##不在host里为真
#     print "tgtcheck取反为真，也就是主机不在host列表里"
#
# elif not  argcheck:
#     print "这是危险命令"


