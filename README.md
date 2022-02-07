# work_day

## robot framework

安装：
- 1.先安装 robot framework：`py -3.7 -m pip install robotframework`
    - 这种安装会安装最新的版本，需要考虑安装 python 的版本是否支持，[官方文档](https://github.com/robotframework/robotframework) 说支持 Python 2.7 and Python 3.5+
- 2.安装 seleniumlibrary：`py -3.7 -m pip install --upgrade robotframework-seleniumlibrary`
    - 这种安装会安装最新的版本，需要考虑和 robot framework 的支持，[官方文档](https://github.com/robotframework/SeleniumLibrary/) 说 SeleniumLibrary 5.1 支持 Python 3.6+
- 3.安装对应浏览器的驱动，方式有两种
    - 第一种直接去官方上下载对应浏览器版本的驱动程序
    - 第二种使用 webdrivermanager 下载
        - 安装：`py -3.7 -m pip install webdrivermanager`
        - 下载对应的驱动到指定目录：`webdrivermanager firefox chrome --linkpath /usr/local/bin`，linkpath 后接保存驱动的地方，前面的 firefox chrome 表示要下载的驱动

## Pycharm 

使用技巧：
- 设置自己想运行的命令：设置->工具->外部工具
    - 名称起一个和执行命令相关的
    - 程序填入执行程序的绝对路径，比如`D:\python37\Scripts\robot.exe`
    - 参数可以填入一些特殊的标识，比如`-d $ContentRoot$\tmp\ $FilePath$`
    - 工作目录一般就是 `$ProjectFileDir$`，当前项目的绝对路径


