$(document).ready(function () {
    $('.sidenav').sidenav();

    $("button.del_img").on('click', function (e) {
        e.preventDefault();
        let box = $(`div[imgid=${$(this).attr('imgid')}]`)
        let url = $(this).attr('url')
        swal({
            title: "Are you sure?",
            text: "你確定要刪除此圖片嗎?",
            type: "warning",
            showCancelButton: true,
            confirmButtonColor: "#DD6B55",
            confirmButtonText: "確認刪除",
            cancelButtonText: "取消此動作",
            closeOnConfirm: false,
        },
            function (isConfirm) {
                if (isConfirm) {
                    $.ajax({
                        type: "post",
                        url: url,
                        data: {},
                        dataType: 'json',
                        success: function (data) {
                            console.log(data);
                            console.log("ajax success");
                        },
                        error: function (data) {
                            console.log(data);
                            console.log("ajax fail");
                        }
                    })
                    swal("刪除！", "圖片已刪除。", "success");
                    $("button.confirm.btn.btn-lg.btn-primary").addClass('swalSuccess')
                    box.slideUp()
                };
            });
    })

    $(".img_box input[type=radio]").on('change', function () {
        //   alert($(this).attr('data-id'));
        // alert($("input[data-id=" + $(this).attr('data-id') + "]:checked").val())
        let publish = $(`input[imgid='${$(this).attr('imgid')}']:checked`).val()
        let url = $(this).attr('url');
        swal({
            title: "Are you sure?",
            text: "你確定要更改此設定嗎?",
            type: "warning",
            showCancelButton: true,
            confirmButtonColor: "#DD6B55",
            confirmButtonText: "確認更改",
            cancelButtonText: "取消此動作",
            closeOnConfirm: false,
        },
            function (isConfirm) {
                if (isConfirm) {
                    $.ajax({
                        type: "post",
                        url: url,
                        data: {
                            publish: publish
                        },
                        dataType: 'json',
                        success: function (data) {
                            console.log(data);
                            console.log("ajax success");
                        },
                        error: function (data) {
                            console.log(data);
                            console.log("ajax fail");
                        }
                    })
                    swal("完成！", "設定已更改。", "success");
                    $("button.confirm.btn.btn-lg.btn-primary").addClass('swalSuccess')
                }
                else {
                    location.reload();
                };
            });
    });
})