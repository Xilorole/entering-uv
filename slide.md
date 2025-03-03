---
marp: true
theme: thin-gaia
size: 16:9
paginate: true
---



<style>
img[alt~="center"] {
  display: block;
  margin: 0 auto;
}
</style>

<!-- _class: lead invert -->


## uv:<br>Python開発者のための<br>究極のパッケージマネージャー

*「pip install の待ち時間、今日で終わりにしませんか？」*


BAD AEU 岩野
2025/03/04

---

<!-- _header: はじめに -->

- Marp とは **Markdown** で**スライド**を作成するためのソフトウェアである。
  - 基本的な Markdown のシンタックスがサポートされている。
- Markdown 上で `---` という区切り線を入れるだけで、次のページに移動することができる。$^1$

> 1: Marp は CommonMark という Markdown の仕様に沿って開発されているため、CommonMark に含まれていない「脚注」の文法（`[^1]` を使うもの）が提供されていない。そこで、https://github.com/marp-team/marp/discussions/150#discussioncomment-1302384 を参照して擬似的に脚注を実現した。
>
---


<!-- _header: Pythonパッケージ管理の「あるある」問題 -->


- 「pip install …（3分経過）」⏳
- 「あれ、仮想環境有効化してたっけ？」🤔
- 「Poetryのロックファイル、また壊れた？」😩
- 「Pythonのバージョン違いでまた動かない…」😱

### → **「この問題、uvなら全部解決できます！」** 🎉

---

### uv の基本機能
- **爆速**: pipの10〜100倍高速 🚀
- **統合**: 仮想環境、パッケージ管理、Pythonバージョン管理がこれ1つでOK 🛠️
- **シンプル**: 設定不要、手順が少ない 🧩
- **互換性**: 既存のPython環境とスムーズに連携 🔄

---

### Poetry vs pip vs uv の比較
- 「uvのインストール時間 < pipが1つのパッケージをインストールする時間」📊
- グラフで圧倒的なスピードを視覚化 📈

---

### uv の特別な機能

1. **uvx**: pipx の代わりにCLIツールを管理（uvx install black でOK）🖥️
2. **uv run**: どこでも依存関係を気にせずスクリプト実行 🏃
3. **グローバルキャッシュ**: 1度インストールしたら再利用 ♻️

---

### uv の使い方

1. `curl -LsSf https://astral.sh/uv/install.sh | sh`
2. `uv init my_project`
3. `uv add fastapi`
4. `uv run main.py`
- **仮想環境の有効化も、pyenvの設定も不要！** 🎉

---

### 既存ツールとの比較

- **pip + virtualenv** → 遅い、管理が面倒 🐢
- **Poetry** → 便利だけど遅い 🐌
- **uv** → 速くて、簡単で、全部できる 🚀

---

### Python開発の未来

- もう「pip install の待ち時間」でスマホいじらなくていい 📱
- 環境構築で時間を無駄にしない ⏳
- **「PythonのCargo」を目指す uv、試してみませんか？** 🚀

---

### Call to Action

- **uv 公式サイト**: astral.sh/uv
- **試すなら今！** `curl -LsSf https://astral.sh/uv/install.sh | sh`
- *「pip install の時間を、もっと楽しいことに使おう！」* 🎉

---
