$(document).ready(function() {
    $.ajax({
        url: "http://127.0.0.1:8000/ajax/get",
        type: "GET",
        dataType: "json",
    }).done(function(data) {
        let tr;
        let td;
        $.each(data, function(index, value) {
            if (index.indexOf('main') !== -1) {
                let tr = $('<tr class="main"/>');
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
                let td = $('<td colspan="7" />');
                let d;
                $.each(value, function(key, d_value) {
                    $(tr_m).attr('id', value["案件ID"] + "_" + value["稼働ID"])
                    d = $('<div class="modal_item" />').text(key + " : " + d_value)
                    td.append(d);
                });
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