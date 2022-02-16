## 内置命令

hintapi 内置了一些命令方便使用。

### `hintapi`

`hintapi` 是 `index` 内置的根命令，所有其余命令均为 `hintapi` 的子命令。

### `hintapi display-urls`

使用 `hintapi display-urls main:app` 命令，可以显示 `main:app` 的所有 URL 以及对应的视图函数的位置。

### `hintapi serve`

!!! notice
    此命令需要安装 [waitress](https://github.com/Pylons/waitress) 和 [hupper](https://github.com/Pylons/hupper)。
    你也可以使用 `pip install hintapi[serve]` 命令安装。

```bash
❯ hintapi serve --help
Usage: hintapi uvicorn [OPTIONS] APPLICATION

  Use waitress to serve hintapi application

Options:
  --bind TEXT                     A string of the form: HOST:PORT, unix:PATH.
                                  [default: 127.0.0.1:4190]
  --log-level [critical|error|warning|info|debug]
                                  [default: info]
  --autoreload / --no-autoreload  Reload the application on python module
                                  changes  [default: autoreload]
  --help                          Show this message and exit.
```

此命令可以便捷的使用 Waitress 启动 hintapi 项目。例如：`hintapi serve main:app`。

有三个选项可以使用：

- `--bind`：指定绑定的地址，例如："0.0.0.0:80"、"unix:./uvicorn.sock"

- `--autoreload / --no-autoreload`：指定 Python 文件变更时，是否自动重启服务。

- `--log-level`：指定输出日志的最低等级。

## 自定义命令

hintapi 使用了 [click](https://palletsprojects.com/p/click/) 来提供命令支持。

所以如果需要自定义命令，你只需要在项目根目录下新建一个 `commands.py` 文件，在其中按照 click 的规则编写自己的命令。

### 样例

在项目根目录下的 `commands.py` 里写入以下内容

```python
from hintapi.cli import index_cli


@index_cli.command(help='Custom command')
def only_print():
    print('Custom command')
```

然后使用 `hintapi --help` 能看到命令已经被加入了

```
❯ hintapi --help
Usage: hintapi [OPTIONS] COMMAND [ARGS]...

Options:
  --help  Show this message and exit.

Commands:
  only-print  Custom command
```

### 引入第三方模块命令

在需要使用其他人封装好的第三方模块命令时，只需要在上述的 `commands.py` 文件中编写 `import` 语句导入第三方模块中编写的命令模块即可。

这一设计是为了让用户显式地知悉自己从哪些第三方模块里导入了命令。
