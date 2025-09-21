# ジュリア集合の生成と絵画

実数部最小値min_x、実数部最大値max_x、虚数部最小値min_y、虚数部最大値max_y、複素定数comp_constを入力することで、ジュリア集合を生成し絵画することができます。
https://moeri.github.io/julia-image-app/

# Features

* 採用した臨界値：100
    * 漸化式を100回計算するうちに、無限大（1垓以上）になれば発散、そうでなければ収束と定義

* 色付け：pythonのライブラリであるmatplotlibのcolormap "seismic"を使用
    * n=0が濃青、50が白、100が濃赤であり、その間がグラデーションとなっております。

https://matplotlib.org/stable/tutorials/colors/colormaps.html#diverging

* 分割数：1000
    * 実数部、虚数部ともに、与えられた最大値と最小値の間を1000分割して計算を行います。


## エラーについて
* error1：数字以外の文字列が入力された場合（未入力含む）
* error2：最大値と最小値の大小関係がおかしい場合

どちらも400エラーを返し、エラーの内容をアラートで表示します。


# Requirement

* python 3.10.10

*numbaがpython3.11以前にしか対応していないため*

ライブラリ
* Flask 2.2.3
* matplotlib 3.7.0
* numba 0.56.4
* numpy 1.23.5


# Installation

```bash
pip install flask
pip install matplotlib
pip install numpy
pip install numba
```

# Note

* Macにて作成したため、Windowsでの動作は確認できておりません。
* ジュリア集合の図形作成の実装に関して、以下のサイトを参考にさせていただきました。
https://watlab-blog.com/2020/06/28/julia-set/

### 警告の非表示について
```app.py
import warnings
warnings.simplefilter('ignore')
```
* numbaをnumpyの計算を高速化するために使用していますが、numpyの機能の一部はnumbaに対応しておらず、API実行時ターミナルに警告表示が出ますが、動作には問題がありません。
* 全てをnumbaに対応している形式で書いた方が速いのですが、コードが長くなってしまうこと、現在のコードでも十分な速さであることから、現在のコードを採用しました。
* 以上のことから、警告を非表示にしております。


# Author

* 荒井 萌里
* moeri.arai@gmail.com
