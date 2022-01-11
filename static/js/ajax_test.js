$(document).ready(function() {
    $.ajax({
        url: "http://127.0.0.1:8000/ajax/get",
        type: "GET",
        dataType: "json",
    }).done(function(data) {

        console.log(data)
        console.log(data["main"])
        data.forEach((element) => {
            var tr = $('<tr />');
            var td;
            element.forEach((item, index) => {
                console.log(item)
                td = $('<td />').text(item);
                tr.append(td);
            });
            $('#datalist').append(tr)
        });
        // $('#datalist').append(tr)

    }).fail(function(data) {

    });

});