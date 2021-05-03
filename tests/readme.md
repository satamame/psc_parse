# テストの実行方法

## 設定

`tests` ディレクトリの中の `juman_settings.py` を、環境に応じて書き換える。

- JUMAN_COMMAND: JUMAN++ を実行するためのコマンド
- JUMAN_OPTION: JUMAN++ を実行する時のコマンドオプション

例
```python
JUMAN_COMMAND = 'jumanpp_v2'
JUMAN_OPTION = r'--config=C:\ProgramData\jumanpp\model\jumandic.conf'
```

## テスト実行の流れ

1. `pyknp` がインストールされている仮想環境に入る。
    ```
    > .venv/Scripts/activate
    ```
1. `unittest` を実行する (以下は全テストを実行する場合)。
    ```
    (.venv) > python -m unittest -v
    ```
