$(document).ready(function() {
    $.ajax({
        url: "http://127.0.0.1:8000/ajax/get",
        type: "GET",
        dataType: "json",
    }).done(function(data) {

        console.log(data["main"][0])
        console.log(data["main"].length)

        var i;
        // for (i = 0; i > data["main"].length; i++) {
        //     console(data["main"][i])
        // }
        var tr = $('<tr />');
        var td;

        $.each(data["main"], function(index, value) {
            if (index == 1) {
                console.log(value)
                td = $('<td class="status" />').text(value);

            } else {
                td = $('<td />').text(value);

            }
            tr.append(td);
        })
        $('#datalist').append(tr)
        SetStatus()

        var tr = $('<tr />');
        var modaldiv = $('<div class="modal">')
        $.each(data["detail"], function(index, value) {

        })

    }).fail(function(data) {

    });


});

function SetStatus() {
    let select = [];
    let status = document.getElementsByClassName("status");
    console.log(status)
    for (let i = 0; i < status.length; i++) {
        let selectHtml = "<select id=select" + i + ">";
        selectHtml = selectHtml + "<option value='1'>" + "稼働中" + "</option>";
        selectHtml = selectHtml + "<option value='2'>" + "終了" + "</option>";
        status[i].innerHTML = selectHtml + "</select>";
    }
}