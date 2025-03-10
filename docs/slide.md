---
marp: true
theme: gaia_extend
paginate: true
header: #cross-lt
footer: uv; the last package manager.
---

<style>
img[alt~="center"] {
  display: block;
  margin: 0 auto;
}
</style>


<!-- _class : lead invert -->
<!-- _footer: "" -->

# uv;
## the last package manager



---

<!-- _class : lead-->

 本スライドは
[uv: Unified Python packaging](https://astral.sh/blog/uv-unified-python-packaging)のページをもとに作成されています
原典にあたりたい場合はそちらを参考にしてください！

---

<!-- _class : lead invert -->


# uvってなんなの？

聞いたことあるけど何かわからないですよね

---


<!-- _class : lead -->



## Rust製の
# 爆速な
# pythonパッケージマネージャー


---

<!-- _class: lead invert -->

# 何ができるの？


---

<!-- _class: lead -->

# コーヒー代を浮かすことができます

(依存関係の解消とかpipが関わる全てのコマンドが速すぎて、
コーヒーをのむ時間がなくなります)

---

<!-- _class: lead invert -->

というのはマジなんですが、詳しくいうと

---

<!-- _class: lead -->

## プロジェクト管理もできるし、
## コマンドラインツールの管理もできるし、
## スクリプトファイル管理もできるし、
なんなら
## python自体の管理もできる

Rustでいうところのcargoを目指した、
高速で使いやすい**パッケージマネージャ**

---


## まず、uvを作ったastralって何者？

爆速なフォーマッタ＆リンターである[Ruff](https://github.com/astral-sh/ruff)を作った会社

![center width:800px invert](https://user-images.githubusercontent.com/1309177/232603514-c95e9b0f-6b31-43de-9a80-9e844173fd6a.svg)

RustでのPython関連のツールを作って次世代の開発エコシステムを提供することをミッションと[している](https://astral.sh/about)

---

## uvで具体的に何ができるのか_1/3

- `uv pip`に置き換えるだけでキャッシュがない状態では**8-10倍**早く、キャッシュがある状態では**80-115倍**早い
  - グローバルキャッシュを持つので、再ダウンロードや再ビルドが走りにくい
- 互換性を維持しているので、`pip`の代わりに`uv pip`、`venv`の代わりに`uv venv`のような形で使える
  - で、`python -m venv`より**80倍**早い
- uvは単一のバイナリなので、pythonと切り離して管理できる
  - `pip`とか`pip3`とか`pip3.7`とか気にしなくていい

---

## uvで具体的に何ができるのか_2/3

- E2Eのプロジェクトマネジメント
  - `uv run`, `uv lock`, `uv sync`でプラットフォームを跨いで環境構築ができる
- 独立した環境にツールをインストールして、既存の依存関係に関係なく利用できるようにする
  - pipxみたいに`uv tool run ruff check`のような形で実行できる
- Python自体の管理ができる
  - pyenvみたいに`uv python install`で任意のバージョンのpythonをインストールできる

---

## uvで具体的に何ができるのか_3/3

- [PEP723](https://packaging.python.org/en/latest/specifications/inline-script-metadata/#inline-script-metadata)に準拠して、`uv run`で、単一ファイル内に記述された依存関係をもとに実行できる

```python
# /// script
# requires-python = ">=3.11"
# dependencies = ["loguru"]
# ///
from loguru import logger
logger.info("Hello, World!")
```

```bash
❯ uv run scripts/run_loguru.py
2025-03-10 13:01:18.428 | INFO     | __main__:<module>:7 - Hello, World!
```


---

## 端的に言えば`uv run`がすごい

`uv run`で実行すれば

- 隔離した環境で実行してくれるし、
- 仮想環境をわざわざactivateしなくていいし、
- 実行時に再lockと再syncしてくれるから最新化されるし、、、

**もうこれで良くない？**

`pip`で手元の環境汚れちゃう・・とか考えなくて大丈夫です、今日からあなたも`uv`信者！

---


<!-- _class: lead invert -->

## プロジェクト管理もできるし、 :arrow_left:
## コマンドラインツールの管理もできるし、
## スクリプトファイル管理もできるし、
なんなら
## python自体の管理もできる

Rustでいうところのcargoを目指した、
高速で使いやすいパッケージマネージャ

---

## プロジェクト管理_1/2

uvはpythonプロジェクト単位での管理も行える

```bash
uv init && uv add "fastapi>=0.112"
```
を行うとこんなpyproject.tomlができる
```toml
[project]
name = "hello-world"
version = "0.1.0"
readme = "README.md"
dependencies = ["fastapi>=0.112"]
```

---

## プロジェクト管理_2/2

そしてこんなクロスプラットフォームなlockfileも作られる。生成されたOSに関わらず、任意の環境での依存関係を解決できる（！）

```toml
[[package]]
name = "fastapi"
version = "0.112.1"
source = { registry = "https://pypi.org/simple" }
dependencies = [
    { name = "pydantic" },
    { name = "starlette" },
    { name = "typing-extensions" },
]
...
```


---



<!-- _class: lead invert -->

## プロジェクト管理もできるし、
## コマンドラインツールの管理もできるし、:arrow_left:
## スクリプトファイル管理もできるし、
なんなら
## python自体の管理もできる

Rustでいうところのcargoを目指した、
高速で使いやすいパッケージマネージャ

---

## `uv tool`_1/2

`uv tool install`で隔離した環境にインストールできるし、単純に`uv tool run`(`uvx`)で実行することもできる


```
❯ uvx ruff
Ruff: An extremely fast Python linter and code formatter.

Usage: ruff [OPTIONS] <COMMAND>
...
```

---

## `uv tool`_2/2

pythonの管理と自動インストールができるので、本当に手間なく、pythonのコマンドを実行できる。`uv python install 3.12`で3.12を利用できるようになる。

まっさらなubuntuのイメージで`posting`コマンドを実行するために必要なステップはたったこれだけ

```shell
$ apt-get update && apt-get install -y curl
$ curl -LsSf https://astral.sh/uv/install.sh | sh
$ source $HOME/.cargo/env
$ uvx posting
```


---



<!-- _class: lead invert -->

## プロジェクト管理もできるし、
## コマンドラインツールの管理もできるし、
## スクリプトファイル管理もできるし、:arrow_left:
なんなら
## python自体の管理もできる

Rustでいうところのcargoを目指した、
高速で使いやすいパッケージマネージャ

---

## 単一ファイルの依存性解決_1/3

`pandas`をインストールしていないと下記のスクリプトは実行できない

```python
from pandas import DataFrame

df = DataFrame({"A": [1, 2, 3], "B": [4, 5, 6]})
print(df)
```

```shell
❯ uv run scripts/run_pandas_fail.py
Traceback (most recent call last):
  File "/workspaces/entering-uv/scripts/run_pandas_fail.py", line 1, in <module>
    from pandas import DataFrame
ModuleNotFoundError: No module named 'pandas'
```

---

## 単一ファイルの依存性解決_2/3

でも`uv run --with`を使えば、スクリプトを実行する際に依存性解決ができる！

```shell
❯ uv run --with pandas scripts/run_pandas_fail.py
Installed 6 packages in 164ms
   A  B
0  1  2
1  2  5
2  3  6
```


---

## 単一ファイルの依存性解決_3/3

`uv add --script`を使って、スクリプトに依存性を記載することもできる

```shell
$ uv add --script scripts/run_pandas_fail.py "pandas"
$ cat run_pandas_fail.py
# /// script
# requires-python = ">=3.13"
# dependencies = [
#     "pandas",
# ]
# ///
from pandas import DataFrame
...
```

---



<!-- _class: lead invert -->

## プロジェクト管理もできるし、
## コマンドラインツールの管理もできるし、
## スクリプトファイル管理もできるし、
なんなら
## python自体の管理もできる:arrow_left:

Rustでいうところのcargoを目指した、
高速で使いやすいパッケージマネージャ

---

## pythonの管理

`uv python pin {version}`でpythonのバージョンを変更できる。

```shell
❯ uv run tool/cli.py hello
2025-03-10 14:15:28.553 | You are using Python 3.11.11

❯ uv python pin 3.13
Updated `.python-version` from `3.11` -> `3.13`

❯ uv run tool/cli.py hello
Using CPython 3.13.2
Removed virtual environment at: .venv
Creating virtual environment at: .venv
Installed 3 packages in 73ms
2025-03-10 14:15:46.676 | You are using Python 3.13.2
```

---

## pythonの管理

`uv run --python 3.11 tool/cli.py hello`とかでもバージョンを変更して実行できる。

```
❯ uv run --python 3.11 tool/cli.py hello
Using CPython 3.11.11
Removed virtual environment at: .venv
Creating virtual environment at: .venv
Installed 3 packages in 122ms
2025-03-10 14:17:54.210 | Hi, there! You are using Python 3.11.11
```

**便利**すぎませんか？


---

## まだまだあるuv

### 大規模開発におけるworkspace

- cargoの同様の概念から着想を得た機能
- 複数のパッケージを同時に管理する際に有効
- 同一のgitリポジトリ内で複数のパッケージがある際に、ルートの階層で単一のlockファイルを共有することで、一貫した依存関係の解消ができる

とか、あんまり使う場面に出会ったことないけど、大規模開発もちゃんとサポート。

---

<!-- _class: lead -->

## まとめ

### みんな`uv`を使って、
### ストレスのない
### python環境構築を手に入れよう！
