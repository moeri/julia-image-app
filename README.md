# ジュリア集合の生成と描画

本アプリは、実数部最小値（min_x）、実数部最大値（max_x）、虚数部最小値（min_y）、虚数部最大値（max_y）、複素定数（comp_const_x, comp_const_y）を入力することで、ジュリア集合を生成し、画像として描画します。

- フロントエンド（入力フォーム・画像表示）は [GitHub Pages](https://moeri.github.io/julia-image-app/) で公開
- バックエンド（画像生成 API）は [Render](https://julia-image-app-1.onrender.com/) で稼働

---

## Features

- **臨界値（最大繰り返し数）**: 100
  100 回の漸化式計算で無限大（1e20 以上）になれば発散、そうでなければ収束と判定
- **色付け**: matplotlib の colormap "seismic"
  n=0 が濃青、50 が白、100 が濃赤のグラデーション
- **分割数**: 300
  実数部・虚数部ともに指定範囲を 300 分割して計算（メモリ節約のため）

---

## 使い方

1. [GitHub Pages のサイト](https://moeri.github.io/julia-image-app/)にアクセス
2. 各パラメータを入力し、「生成」ボタンをクリック
3. ジュリア集合の画像が表示されます

### 推奨パラメータ例

- min_x: `-1.5`
- max_x: `1.5`
- min_y: `-1.5`
- max_y: `1.5`
- comp_const_x: `-0.8`
- comp_const_y: `0.156`

---

## エラーについて

- **error1**：数字以外の文字列が入力された場合（未入力含む）→ 400 エラー
- **error2**：最大値と最小値の大小関係が逆の場合 → 400 エラー

どちらもアラートで内容を表示します。

---

## Requirement

- Python 3.10.10
  ※numba が Python 3.11 以前にしか対応していません

### 使用ライブラリ

- Flask 2.2.3
- Flask-CORS
- matplotlib 3.7.0
- numba 0.56.4
- numpy 1.23.5
- gunicorn

---

## Installation（ローカルで API を動かす場合）

```bash
pip install -r requirements.txt
```

---

## 構成

- `/docs` … フロントエンド（HTML, CSS, JS）
  GitHub Pages で公開
- `/app.py` … バックエンド（Flask API）
  Render でデプロイ

---

## 注意

- Mac で作成・動作確認済み。Windows では未検証です。
- ジュリア集合の実装は [watlab-blog.com/2020/06/28/julia-set/](https://watlab-blog.com/2020/06/28/julia-set/) を参考にしています。

---

## Author

- 荒井 萌里
- moeri.arai@gmail.com
