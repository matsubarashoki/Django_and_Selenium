$(document).ready(function() {

    $.ajax({
        url: "http://127.0.0.1:8000/ajax/get",
        type: "GET",
        dataType: "json",
    }).done(function(data) {
        console.log(data)
        console.log(data[1].id)
            // matterData.forEach((row, index) => {
            //     console.log(row[index])
            // })

    }).fail(function(data) {

    });


    // // server-side利用時は拡張機能の選択(Select)が使えないので、DataTables公式の
    // // サンプルコードを元に選択処理を自作する。
    // // https://datatables.net/examples/server_side/select_rows.html
    // $('#datatable tbody').on('click', 'tr', function() {

    //     let id = $(this).attr('data-id');
    //     //配列(selected)の中のidが存在したら配列のindexを返す
    //     let index = $.inArray(id, selected);

    //     if (index === -1) {

    //         selected.push(id);
    //         //これなんだ？
    //         selected.sort(function(a, b) {
    //             return a - b
    //         });
    //         //選択行にselectedクラスを足している？
    //         $(this).addClass('selected');
    //     } else {
    //         selected.splice(index, 1);
    //         $(this).removeClass('selected');
    //     }
    //     $('#selected').html(selected.join(','));
    // });

    // // サンプル：クリックしたレコードのデータを取得
    // // data()でセル、行、表示中のテーブル全体のデータを取得可能
    // // https://datatables.net/reference/api/row().data()

    // $('#datatable tbody').on('click', 'tr', function() {
    //     console.log(table.row(this).data());
    // });

    // // 全選択を解除
    // $('#clear').on('click', function() {
    //     selected = [];
    //     $('#datatable tr').removeClass('selected');
    //     $('#selected').html(selected.join(','))
    // })

    // // 印刷・Excel・CSVボタン クリック
    // $('.report').on('click', function() {

    //     if (selected.length == 0) {
    //         alert('先にデータを選択してください。');
    //         return false;
    //     }

    //     // 隠しフォームに選択したidを格納し、各機能のWebAPIに送信する
    //     let form = $("#form")[0];
    //     $("*[name=id_list]").val(selected.join('_'))
    //     form.method = 'GET';

    //     // GETクエリの長さ制限に注意。このコードは大量件数の選択に配慮していません。
    //     // https://support.microsoft.com/ja-jp/help/208427/maximum-url-length-is-2-083-characters-in-internet-explorer

    //     // ボタンのidで処理判定
    //     switch (this.id) {
    //         case 'print':
    //             // 印刷のみ別ウィンドウを開く
    //             window.open('', 'new_window');
    //             form.action = 'print';
    //             form.target = 'new_window';
    //             form.submit();
    //             break;
    //         case 'excel':
    //             form.action = 'excel';
    //             form.submit();
    //             break;
    //         case 'csv':
    //             form.action = 'csv';
    //             form.submit();
    //             break;
    //     }
    // })
});