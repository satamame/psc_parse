# psc-parse

## 依存するパッケージ

- pyknp==0.4.1
- scikit-learn

## 必要な外部アプリケーション

- JUMAN++ 2.0.0-rc3

## インストール

```
> pip install git+https://github.com/satamame/psc_parse#egg=psc-parse
```

pipenv の場合もコマンド以外は同様です。  
Windows の場合は、「ワールドワイド言語サポートで Unicode UTF-8 を使用」を ON にしてください。

## モジュール

- features.py
    - 台本ファイルから各行の特徴量を作るためのモジュール。
- juman_psc.py
    - JUMAN++ を台本解析用に拡張したサブクラス JumanPsc を定義。
    - 形態素解析の実行時に、なるべくエラーを避ける。
- model.py
    - 台本ファイルの行の種類を予測するためのモジュール。
- mrph_match.py
    - 形態素列のパターンマッチングをするためのモジュール。
- mrph_test.py
    - テキストファイルが形態素解析可能か調べるためのモジュール。
- psc_class.py
    - 台本の行の種類の定義。

# 特徴量設計

特徴量ファイルにはヘッダはなく、以下の順に数値が格納されている。  
パターンについては、`mrph_match` モジュールの `RPH_MTCH_PTN` を参照。

1. 0001
    - パターン 0001 にマッチするか (0/1)
1. 0002
    - パターン 0002 にマッチするか (0/1)
1. 0003
    - パターン 0003 にマッチするか (0/1)
1. 0004
    - パターン 0004 にマッチするか (0/1)
1. 0005
    - パターン 0005 にマッチするか (0/1)
1. 0006
    - パターン 0006 にマッチするか (0/1)
1. symbol_follows
    - パターンの後続単語がセリフっぽい記号 (…・！!) か (0/1)
1. interj_follows
    - パターンの後続単語が感動詞か (0/1)
1. is_first_line
    - 最初の行か (0/1)
1. is_last_line
    - 最後の行か (0/1)
1. is_empty
    - 空または空白文字のみか (0/1)
1. ends_w_bracket
    - 最後が '」'か (0/1)
1. sentence_ends
    - 最後が文末文字 (。？?！!) か (0/1)
1. states_charsheadline
    - 「登場人物」を含むか (0/1)
1. leading_spc
    - 行頭の空白文字の数 (正規化オプション有り)
1. leading_spc_delta
    - 行頭の空白文字の数の増減 (整数)
1. prev_is_empty
    - 前の行が空行か (0/1)
1. prev_ends_w_bracket
    - 前の行の最後が '」'か (0/1)
1. prev_sentence_ends
    - 前の行の最後が文末文字 (。？?！!) か (0/1)
1. ptn_line_count
    - この行と同じパターンにマッチした行数 (正規化オプション有り)
1. str_line_count
    - この行と同じ文字列にパターンマッチした行数 (正規化オプション有り)
1. spc_line_count
    - この行と行頭の空白の数が同じ行の数 (正規化オプション有り)
1. bracket_line_rate
    - ファイル全体の '「' を含む行の割合 (小数)
1. prev_is_CHARACTER
    - 前の行が <登場人物> か (0/1)
1. prev_is_CHARACTER_CONTINUED
    - 前の行が <登場人物の2行目以降> か (0/1)
1. prev_is_DIRECTION
    - 前の行が <ト書き> か (0/1)
1. prev_is_DIRECTION_CONTINUED
    - 前の行が <ト書きの2行目以降> か (0/1)
1. prev_is_DIALOGUE
    - 前の行が <セリフ> か (0/1)
1. prev_is_DIALOGUE_CONTINUED
    - 前の行が <セリフの2行目以降> か (0/1)
1. prev_is_COMMENT
    - 前の行が <コメント> か (0/1)
1. prev_is_COMMENT_CONTINUED
    - 前の行が <コメントの2行目以降> か (0/1)
1. charsheadline_used
    - 登場人物見出しが出た後か (0/1)
1. h1_used
    - 柱 (レベル1) が出た後か (0/1)
1. direction_used
    - 書きが出た後か (0/1)
1. dialogue_used
    - セリフが出た後か (0/1)
