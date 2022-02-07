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




