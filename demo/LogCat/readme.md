# LogCat 使用说明

## 类名 LogCat

## 方法

1. start(level = 'W')

   开始记录日志，存到同目录下的 logcat.txt 文件中

   若要修改文件名，请修改 ```__init__()```中```self.logpath```后的路径

   ------

   参数

   level : 字符 'W' 或者 'E'，默认为'W'

   当参数是'W'时，记录Warning 和 Error 的日志，

   当参数是'E'时，记录Error的日志

2. close()

   结束记录日志， ！！！此函数必须在结束时调用，否则进程会在软件关闭后继续运行

   如果出现程序中途退出无法正常调用```close()```的情况，可以到任务管理器中找到```adb.exe```并结束进程

## 样例

```python
from logcat import *
a = LogCat()
a.start('W')
#.........
a.close()
```

