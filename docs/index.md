# Hint API

这是一个同步 web 框架，设计目的在于快速的构建需要的 web 服务，无论是 Templates 还是 API。到目前为止，hintapi 不内置数据库、缓存等其他功能。选择困难者请直接使用 [Django](https://www.djangoproject.com/)。

如果你发现了任何的 BUG，欢迎访问 [Github Issues](https://github.com/abersheeran/hintapi/issues) 反馈；如果你有需要与其他人共同分享、讨论的事情或希望增加的特性，欢迎访问 [Github Discussions](https://github.com/abersheeran/hintapi/discussions) 发起讨论。

## 设计灵感

在 [Index.py](https://index-py.aber.sh) 的使用过程里，发现 asyncio 生态并不完善，但又无法舍弃 Type hint 自动校验参数、生成文档的功能。所以裁剪了一些功能，并基于 [BáiZé](https://baize.aber.sh) 健壮的 WSGI 支持创建了此项目。

## 安装方法

hintapi 要求 Python 的版本至少是 3.7，对系统无要求。如果不能/不愿升级 Python 版本，可以使用 docker 来运行 hintapi。

安装 [pypi](https://pypi.org) 上的包

```bash
pip install -U hintapi
```
