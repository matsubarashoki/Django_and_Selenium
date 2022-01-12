$(document).ready(function() {
    $.ajax({
        url: "http://127.0.0.1:8000/ajax/get",
        type: "GET",
        dataType: "json",
    }).done(function(data) {

        console.log(data)
        var tr;
        var td;
        $.each(data, function(index, value) {
            if (index.indexOf('main') !== -1) {
                var tr = $('<tr />');
                var td;
                $.each(value, function(index, m_value) {

                    if (index == 0) {
                        //

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
                var d = $('<div class="modal_item"  />').text(value)
                tr_m.append(d)
                $('#datalist').append(tr_m)
            }
        })

        SetStatus();
        $('.modal_row').css("display", "none");

        $('#MatterId').css("display", "none");


        // $.each(data["main"], function(index, value) {
        //     if (index == 1) {
        //         td = $('<td class="status" />').text(value);
        //     } else {
        //         td = $('<td />').text(value);
        //     }
        //     tr.append(td);
        // })
        // $('#datalist').append(tr)

        // SetStatus()

        // var tr_m = $('<tr id="modal_row"/>');
        // $.each(data["detail"], function(index, value) {
        //     var d = $('<div class="modal_item" tabtabindex="-1" />').text(value)
        //     tr_m.append(d)
        // })
        // $('#datalist').append(tr_m)
        // $('#modal_row').css("display", "none");


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

function displey_none() {

}