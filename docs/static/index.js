function get_func() {
    let input_data = document.getElementById("data");
    let formData = new FormData(input_data);
    input_data.reset();
    let content_area = document.getElementById("image_result");
    content_area.textContent = null;

    let message = document.createElement("p");
    message.textContent = "画像生成中...";
    content_area.appendChild(message);

    fetch("https://julia-image-app-1.onrender.com/julia/post", {
        method: "POST",
        body: formData,
    })
        .then((response) => {
        return response.text();
        })
        .then(function (data) {
        if (data == "error1") {
            content_area.textContent = null;
            alert("数値を入力してください");
        } else if (data == "error2") {
            content_area.textContent = null;
            alert("最大値には、最小値より大きな値を設定してください");
        } else {
            let img_element = document.createElement("img");
            img_element.src = "data:image/png;base64, " + data;
            img_element.alt = "ジュリア集合";
            content_area.textContent = null;
            content_area.appendChild(img_element);
        }
    });
}
