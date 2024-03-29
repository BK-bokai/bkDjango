$(document).ready(function () {
    $(".msg-func").on('click', function () {
        $("form[msgId=" + $(this).attr('msgId') + "]").toggle(500);
    })
    //刪除文章
    $('.msgDel').on('click', function () {

        let msgid = $(this).attr('msgId');
        let url = $(this).attr('url');
        let target = $("div[msg=message" + msgid + "]")

        swal({
            title: "Are you sure?",
            text: "你確定要刪除嗎?",
            type: "warning",
            showCancelButton: true,
            confirmButtonColor: "#DD6B55",
            confirmButtonText: "Yes, 確認刪除!",
            cancelButtonText: "No, 取消動作!",
            closeOnConfirm: false,
            closeOnCancel: false
        },
            function (isConfirm) {
                if (isConfirm) {
                    $.ajax({
                        type: "POST",
                        // url: '{{url("admin/img")}}'+ '/' + $(this).attr('data-id'),
                        url: url,
                        data: {
                            id: msgid,
                        },
                        dataType: 'html',
                        success: function (data) {
                            swal("確認刪除", "已刪除此留言版", "success")
                            let remFun = function () {
                                target.remove();
                              }
                            target.slideUp(300,remFun);
                            console.log(data);
                            console.log("ajax success");
                        }
                    })
                }
                else {
                    swal("取消動作", "已取消剛剛請求！", "success")
                }
            });
    })

    //編輯文章
    $('.msgEdit').on('click', function () {
        //取得此留言的ID
        let msgid = $(this).attr('msgId');
        //取得此留言的URL
        let url = $(this).attr('url');
        //取得空白表單
        let form = $('#edit').children();
        //取得原本文章內文要用html(因為你要讀到<br>html標籤)
        let contain = $("div[msgcontain=" + msgid + "]").html().trim().replace(/<br>/g, "\r");
        //將文章內文改為表單
        let editarea = $("div[msgcontain=" + msgid + "]").html(form);


        // 再將原本的內文塞入編輯表單內要用val(因為你已經轉換行符號了)
        $("div[msgcontain=" + msgid + "] #textarea1").val(contain);


        $("#msgEdit").on('click', function () {
            //當編輯完時利用ajax傳送
            $.ajax({
                type: "POST",
                url: url,
                data: {
                    id: msgid,
                    body: $("div[msgcontain=" + msgid + "] #textarea1").val()
                },
                dataType: 'json',
                success: function (data) {
                    //成功時將修改的值塞進去原本表單的位置
                    $("div[msgcontain=" + msgid + "]").html($("div[msgcontain=" + msgid + "] #textarea1").val().replace(/\n/g, "<br>"))
                    // $("div[msgcontain=" + msgid + "]").html($("div[msgcontain=" + msgid + "] #textarea1").val())
                    //再將表單內的值清除
                    form.find('#textarea1').val('');
                    //再塞入編輯表單
                    $('#edit').html(form);
                    // $("div[msgcontain=" + msgid + "]").html($('#textarea1').val())
                    // $("div[msg=message" + msgid + "]").slideUp(3000)
                    console.log(data);
                    console.log("ajax success");
                }
            })
        })

    })


    //刪除回復
    $('.replyDel').on('click', function () {
        let replyid = $(this).attr('replyId');
        let url = $(this).attr('url');
        let target = $("div[reply=reply" + replyid + "]")
        let msgId  = $(this).attr('msgId')
        let reply_num = $('div.'+msgId+'_reply_num')
        let num = parseInt(reply_num.text().match(/\d+/))

        swal({
            title: "Are you sure?",
            text: "你確定要刪除嗎?",
            type: "warning",
            showCancelButton: true,
            confirmButtonColor: "#DD6B55",
            confirmButtonText: "Yes, 確認刪除!",
            cancelButtonText: "No, 取消動作!",
            closeOnConfirm: false,
            closeOnCancel: false
        },
            function (isConfirm) {
                if (isConfirm) {
                    $.ajax({
                        type: "POST",
                        url: url,
                        data: {
                            id: replyid,
                        },
                        dataType: 'html',
                        success: function (data) {
                            swal("確認刪除", "已刪除此留言", "success")

                            let remFun = function () {
                                target.remove();
                              }
                            target.slideUp(300,remFun);

                            reply_num.text(String(num - 1)+"則留言")
                            console.log(data);
                            console.log("ajax success");
                        }
                    })
                    // alert(url)
                }
                else {
                    swal("取消動作", "已取消剛剛請求！", "success")
                }
            });
    })

    //編輯回復
    $('.replyEdit').on('click', function () {

        let replyid = $(this).attr('replyId');
        let url = $(this).attr('url');
        //取得空白表單
        let form = $('#edit').children();
        //取得原本回復內文要用html(因為你要讀到<br>html標籤)
        let contain = $("span[replycontain=" + replyid + "]").html().trim().replace(/<br>/g, "\r");
        //將文章內文改為表單
        let editarea = $("span[replycontain=" + replyid + "]").html(form);

        // 再將原本的內文塞入編輯表單內要用val(因為已經轉換行符號了)
        $("span[replycontain=" + replyid + "] #textarea1").val(contain);

        $("#msgEdit").on('click', function () {
            //當編輯完時利用ajax傳送
            $.ajax({
                type: "POST",
                url: url,
                data: {
                    id: replyid,
                    body: $("span[replycontain=" + replyid + "] #textarea1").val()
                },
                dataType: 'html',
                success: function (data) {
                    //成功時將修改的值塞進去原本表單的位置
                    $("span[replycontain=" + replyid + "]").html($("span[replycontain=" + replyid + "] #textarea1").val().replace(/\n/g, "<br>"))
                    //再將表單內的值清除
                    form.find('#textarea1').val('');
                    //再塞入編輯表單
                    $('#edit').html(form);
                    console.log(data);
                    console.log("ajax success");
                }
            })


        })
    })

})