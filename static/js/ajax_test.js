$(document).ready(function() {
    $.ajax({
        url: "http://127.0.0.1:8000/ajax/get",
        type: "GET",
        dataType: "json",
    }).done(function(data) {

        var tr;
        var td;
        $.each(data, function(index, value) {
            if (index.indexOf('main') !== -1) {
                var tr = $('<tr />');
                var td;
                $.each(value, function(index, m_value) {
                    if (index == 0) {
                        //MatterIdは作らない
                    } else if (index == 2) {
                        td = $('<td class="status" />').text(m_value);
                    } else {
                        td = $('<td />').text(m_value);
                    }
                    tr.append(td);
                })
                $('#datalist').append(tr)

            } else {
                var tr_m = $('<tr class="modal_row"/>');
                var d;
                $.each(value, function(index, d_value) {
                    d = $('<div class="modal_item"  />').text(d_value)
                    tr_m.append(d);
                });
                $('#datalist').append(tr_m);
            }
        })

        SetStatus();
        //$('.modal_row').css("display", "none");
        $('#MatterId').css("display", "none");

    }).fail(function(data) {});

});

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

function ShowModal() {
    let status = document.getElementsByClassName("status");

}