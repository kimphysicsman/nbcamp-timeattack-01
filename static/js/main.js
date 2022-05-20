function upload_img(event) {
  let reader = new FileReader();
  reader.onload = (event) => {
    let img = document.querySelector("#image_file");
    let src = event.target.result;
    img.setAttribute("src", src);
  };
  reader.readAsDataURL(event.target.files[0]);
}

function upload() {
    let file = $('#image')[0].files[0];
    let form_data = new FormData()
    form_data.append('img', file)

    $.ajax({
        type: "POST",
        url: '/img',
        data: form_data,
        cache: false,
        contentType: false,
        processData: false,
        success: function (response) {
            console.log(response)
        }
    })
}