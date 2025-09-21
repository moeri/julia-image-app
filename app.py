import base64
import numpy as np
from numba import jit
from io import BytesIO

import matplotlib

import matplotlib.pyplot as plt
from matplotlib.colors import Normalize

from flask import Flask, render_template, request

# 一部numbaのjitに対応していない部分があり、警告が表示されるため非表示
import warnings
from flask_cors import CORS

app = Flask(__name__)
CORS(app, origins=["https://moeri.github.io"])

matplotlib.use("agg")
warnings.simplefilter("ignore")


# ジュリア集合の計算
@jit
def julia(z_real, z_imag, n_max, a, b):
    # 実部Reと虚部Imの組み合わせを計算
    Re, Im = np.meshgrid(z_real, z_imag)
    # 組み合わせの総数
    n_grid = len(Re.ravel())
    # データ格納用空配列
    z = np.zeros(n_grid)

    # ジュリア集合に属するか否かを計算し、Zに格納
    for i in range(n_grid):
        c = complex(a, b)
        n = 0
        z0 = complex(Re.ravel()[i], Im.ravel()[i])

        # z0が無限大(1垓以上)になるか、最大繰り返し数になるまでループする
        while np.abs(z0) < 1e20 and not n == n_max:
            # 漸化式を計算
            z0 = z0**2 + c
            # 繰り返し数を増分
            n += 1

        # z0が無限大に発散する場合はn, 収束する場合は0を格納
        if n == n_max:
            z[i] = 0
        else:
            z[i] = n

    # 2次元配列にリシェイプ
    z = np.reshape(z, Re.shape)
    # imshow()で上下逆になるので予め上下反転
    z = z[::-1]
    return z


@app.route("/julia")
def index():
    return render_template("index.html")


@app.route("/julia/post", methods=["POST"])
def post():
    try:
        min_x = float(request.form["min_x"])
        max_x = float(request.form["max_x"])
        min_y = float(request.form["min_y"])
        max_y = float(request.form["max_y"])
        a = float(request.form["comp_const_x"])
        b = float(request.form["comp_const_y"])
    # 数値が入力されていないエラー
    except ValueError:
        return "error1", 400

    # 最大値が最小値よりも小さいエラー
    if min_x >= max_x or min_y >= max_y:
        return "error2", 400

    # 分割数
    resolution = 1000

    # 実部と虚部の軸データ配列
    z_real = np.linspace(min_x, max_x, resolution)
    z_imag = np.linspace(min_y, max_y, resolution)
    # 最大繰り返し数
    n_max = 100

    # 計算
    z = julia(z_real, z_imag, n_max, a, b)

    # 図形作成
    plt.figure()
    plt.imshow(
        z,
        cmap="seismic",
        norm=Normalize(vmin=0, vmax=n_max),
        extent=[min_x, max_x, min_y, max_y],
    )
    # 軸を消去
    plt.axis("off")
    plt.tight_layout()

    # png画像を保存
    buffer = BytesIO()
    plt.savefig(buffer, format="png", bbox_inches="tight", pad_inches=0)
    buffer.seek(0)
    img = buffer.getvalue()

    # png画像をbase64に変換
    graph = base64.b64encode(img)
    buffer.close()

    return graph


if __name__ == "__main__":
    app.run(port=8080)
