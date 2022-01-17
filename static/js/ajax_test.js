$(document).ready(function() {
    $.ajax({
        url: "http://127.0.0.1:8000/ajax/get",
        type: "GET",
        dataType: "json",
    }).done(function(data) {
        $.each(data, function(index, value) {
            if (index.indexOf('main') !== -1) {
                let tr = $('<tr class="main"/>');
                let checkbox = $('<td><input id="ch_box" type="checkbox" /></td>')
                tr.append(checkbox)
                let td;
                $.each(value, function(key, m_value) {
                    switch (key) {
                        case "案件ID":
                            td = $('<td class="matter_id" />').text(m_value);
                            break;
                        case "稼働ID":
                            td = $('<td class="aw_id" />').text(m_value);
                            break;
                        case "ステータス":
                            td = $('<td class="status" />').text(m_value);
                            break;
                        default:
                            td = $('<td />').text(m_value);
                            break;
                    }
                    tr.append(td);
                })
                $('#datalist').append(tr)

            } else {
                let tr_m = $('<tr class="modal_row" nowrap/>');
                let td = $('<td colspan="8" />');
                let d;
                $.each(value, function(key, d_value) {
                    $(tr_m).attr('id', value["案件ID"] + "_" + value["稼働ID"])
                    d = $('<div class="modal_item" />').text(key + " : " + d_value)
                    td.append(d);
                });
                let d_button = '<button class="btn btn-outline-dark mr-3 popup">編集</button>'
                td.append(d_button)

                tr_m.append(td)
                $('#datalist').append(tr_m);
            }
        });
        $('#MatterId').css("display", "none");
        $('.matter_id').css("display", "none");
        $('.modal_row').hide()

        SetStatus();

    }).fail(function(data) {

    });

    //セレクタボックスの処理
    function SetStatus() {
        let select = [];
        let status = document.getElementsByClassName("status");
        for (let i = 0; i < status.length; i++) {
            let selectHtml = "<select id=select" + i + ">";
            selectHtml = selectHtml + "<option value='1'>" + "稼働中" + "</option>";
            selectHtml = selectHtml + "<option value='2'>" + "終了" + "</option>";
            status[i].innerHTML = selectHtml + "</select>";
        }
    }

    //詳細行表示切り替えイベント
    $(document).on("click", ".main", function() {
        //val()はinputとかにしか使えないそうな。知らなかった。
        //対象行のID取得
        let target = $(this).children(".matter_id").html() + "_" + $(this).children(".aw_id").html();
        //表示切り替え 三項演算子
        let ans = ($('#' + target).css("display") == "none" ? $('#' + target).show() : $('#' + target).hide());
    });

    //チェックボックスが選択されたら、formにidを入れる
    $('#datatable input').on('click', function() {
        let aw_id = $(this).children('#aw_id').html()
        console.log(this)
    });

    //全選択解除
    $('#clear').on('click', function() {
        $('#datatable input').prop('checked', false);
        //$('#selected').html(selected.join(','))
    });

    // 印刷・Excel・CSVボタン クリック
    $('.report').on('click', function() {

        if (selected.length == 0) {
            alert('先にデータを選択してください。');
            return false;
        }

        // 隠しフォームに選択したidを格納し、各機能のWebAPIに送信する
        let form = $("#form")[0];
        $("*[name=id_list]").val(selected.join('_'))
        form.method = 'GET';

        // GETクエリの長さ制限に注意。このコードは大量件数の選択に配慮していません。
        // https://support.microsoft.com/ja-jp/help/208427/maximum-url-length-is-2-083-characters-in-internet-explorer

        // ボタンのidで処理判定
        switch (this.id) {
            case 'print':
                // 印刷のみ別ウィンドウを開く
                window.open('', 'new_window');
                form.action = 'print';
                form.target = 'new_window';
                form.submit();
                break;
            case 'excel':
                form.action = 'excel';
                form.submit();
                break;
            case 'csv':
                form.action = 'csv';
                form.submit();
                break;
        }
    })

    //編集ボタン
    $(document).on("click", "button.popup", function() {
        $.ajax({
            url: "http://127.0.0.1:8000/ajax/edit",
            type: "GET",
        }).done(function(data) {
            $('#modal').modal("show");
        })
    });


});