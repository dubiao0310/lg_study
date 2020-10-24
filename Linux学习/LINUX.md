### 1.进程
##### 1.1 top命令
+ top -b <br/>以批处理模式显示程序信息
+ top -n 10 <br/>表示更新10次后终止更新显示
+ top -d 3 <br/>表示每隔３秒刷新一次
+ top -c <br/>显示完整命令
+ top -p 129 <br/>显示进程号为129的进程信息，CPU、内存占用率等

练习：统计阿里云盾进程的性能，每1s统计一次，统计他的cpu、mem的利用率，用tab隔开，并在最后空出一行打印下两个指标的平均值。

```top -b -n 10 -d 1 | grep -i "AliYunDun$" | awk '{print $9,$10};{a+=$9;b+=$10}END{print "";print a/NR,b/NR}'```

##### 1.2 ps命令
+ **ps -ef** <br/>显示所有命令，连带命令行
+ **ps -aux** <br/>显示所有包含其他使用者的行程
+ ps -a <br/>显示所有终端机下执行的程序，除了阶段作业领导者之外
+ ps a <br/>显示现行终端机下的所有程序，包括其他用户的程序。
+ ps -A <br/>显示所有进程信息
+ ps -u root <br/>显示root进程用户信息

### 2.网络
##### netstat
netstat：打印Linux网络系统的状态信息
+ netstat -t 列出所有tcp
+ netstat -u 列出所有udp
+ netstat -l 只显示监听端口
+ netstat -n 以数字形式显示地址和端口号
+ netstat -p 显示进程的pid和名字

常用命令
+ netstat -tnp
+ netstat -tlnp

### 3.常用的数据统计命令

##### 3.1 数据检索：　less more cat head tail
+ less <br/>less 工具也是对文件或其它输出进行分页显示的工具，应该说是linux正统查看文件内容的工具，功能极其强大。less 的用法比起 more 更加的有弹性。 在 more 的时候，我们并没有办法向前面翻， 只能往后面看，但若使用了 less 时，就可以使用 [pageup] [pagedown] 等按 键的功能来往前往后翻看文件，更容易用来查看一个文件的内容！除此之外，在 less 里头可以拥有更多的搜索功能，不止可以向下搜，也可以向上搜。
    + ps -ef | less -N <br/>ps查看进程信息并通过less分页显示同时显示行号
    
    + 屏幕导航
        1. ctrl + F - 向前移动一屏
        2. ctrl + B - 向后移动一屏
        3. ctrl + D - 向前移动半屏
        4. ctrl + U - 向后移动半屏
        5. j - 向前移动一行
        6. k - 向后移动一行
        7. G - 移动到最后一行
        8. g - 移动到第一行

+ cat test.log  <br/>显示所有日志内容

+ more <br/>more功能类似 cat ，cat命令是整个文件的内容从上到下显示在屏幕上。 more会以一页一页的显示方便使用者逐页阅读，而最基本的指令就是按空白键（space）就往下一页显示，按 b 键就会往回（back）一页显示，而且还有搜寻字串的功能 。more命令从前向后读取文件，因此在启动时就加载整个文件。
  + more +3 test.log <br/>从第三行开始显示日志内容
  
+ head 查看开始的几行
    + head -n 10 file <br/> 查看文件的前十行
    
    + head -n -10 file <br/> 查看文件除了最后三行的所有内容
    
+ tail  <br/>打印文件的尾部内容
    + tail -n 3 file <br>打印最后三行
    + tail -n +3 file  <br>打印第三行开始的所有内容 
    + tail -f file <br/> 实时监控文件的更新内容了
    + tail -f -s 5 test2.txt <br>如每隔５秒查看一次test2.txt的内容是否更新

  
##### 3.2 数据操作：　wc sort uniq

+ wc命令:默认的情况下，wc将计算指定文件的行数、字数，以及字节数
    + wc filename <br> 3 92 598 testfile       # testfile文件的行数为3、单词数92、字节数598 
    + -c或--bytes或--chars <br>只显示Bytes数。
    + -l或--lines <br>只显示行数。
    + -w或--words <br>只显示字数。
    
+ sort 命令将以默认的方式将文本文件的第一列以ASCII 码的次序排列，并将结果输出到标准输出
    + -n 依照数值的大小排序
    + -r 以相反的顺序来排序
    + -t<分隔字符> 指定排序时所用的栏位分隔字符。
    + sort -t ‘ ‘ -k 1 facebook.txt 按第一个域进行排序
    
+ uniq 命令用于检查及删除文本文件中重复出现的行列，一般与 sort 命令结合使用<br>**当重复的行并不相邻时,uniq 命令是不起作用的**
    + uniq testfile     删除重复行后的内容  
    + uniq -c testfile 检查文件并删除文件中重复出现的行，并在行首显示该行重复出现的次数
    + sort testfile1 | uniq -c 统计各行在文件中出现的次数
    + sort testfile1 | uniq -d  在文件中找出重复的行
    + sort testfile1 | -u或--unique 仅显示出一次的行列
    + -w<字符位置>或--check-chars=<字符位置> 指定要比较的字符

### 4. linux三剑客

##### 4.1 grep 
+  grep pattern file 
+  grep -n pattern file 显示行号
+ grep -i pattern file 忽略大小写
+ grep -v pattern file 反过来（invert），只打印没有匹配的，而匹配的反而不打印。
+ grep -o pattern file 只显示被模式匹配到的字符串。
+ grep -c pattern file  显示总共有多少行被匹配到了，而不是显示被匹配到的内容，注意如果同时使用-cv选项是显示有多少行没有被匹配到
+ grep -E pattern file  开启扩展（Extend）的正则表达式。
+ grep pattern -r dir/ 递归搜索
+ grep -A -B -C pattern file 打印命中数据的上下文

#####4.2 awk
学习博客：https://www.cnblogs.com/ginvip/p/6352157.html
https://blog.csdn.net/qq_36119192/article/details/82982732

+ awk 'BEGIN{}END{}' 开始和结束
+ awk '/bbb/' 正则匹配
+ awk '/aa/,/bb/' 区间选择
+ awk '$2~/aaa/' 字段匹配
+ awk '$2=="aaa"' 字段等于
+ awk 'NR==2' 取第二行
+ awk 'NR>1' 去掉第一行

+ FS 字段分隔符
+ OFS 输出数据的字段分隔符
+ RS 记录分隔符
