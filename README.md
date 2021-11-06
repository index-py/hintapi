<div align="center">

<h1>Hint API</h1>

<p>
中文
|
<a href="https://github.com/abersheeran/hintapi/tree/master/README-en.md">English</a>
</p>

<p>
<a href="https://github.com/abersheeran/hintapi/actions?query=workflow%3ACI">
<img src="https://github.com/abersheeran/hintapi/workflows/CI/badge.svg" alt="Github Action Test" />
</a>

<a href="https://app.codecov.io/gh/abersheeran/hintapi/">
<img alt="Codecov" src="https://img.shields.io/codecov/c/github/abersheeran/hintapi">
</a>
</p>

<a href="https://pypi.org/project/hintapi/">
<img src="https://img.shields.io/pypi/v/hintapi" alt="PyPI" />
</a>

<a href="https://pepy.tech/project/hintapi">
<img src="https://static.pepy.tech/personalized-badge/hintapi?period=total&units=international_system&left_color=black&right_color=blue&left_text=PyPi-Downloads" alt="Downloads">
</a>
</p>

<p>
<img src="https://img.shields.io/pypi/pyversions/hintapi" alt="PyPI - Python Version" />
</p>

基于 Type hint 的 Web 框架

<a href="https://hintapi.aber.sh/stable/">hintapi 文档</a>

</div>

---

hintapi 实现了 [WSGI](http://wsgi.readthedocs.io/en/latest/) 接口，并使用 Radix Tree 进行路由查找。是[最快的 Python web 框架之一](https://github.com/the-benchmarker/web-frameworks)。一切特性都服务于快速开发高性能的 Web 服务。

- 大量正确的类型注释
- 灵活且高效的路由系统
- 可视化 API 接口与在线调试

## Install

```bash
pip install -U hintapi
```

## Example

```python
from typing_extensions import Annotated
from hintapi import HintAPI, PlainTextResponse

app = HintAPI()


@app.router.http("/")
def homepage() -> Annotated[str, PlainTextResponse[200]]:
    return "hi, this is homepage"
```
