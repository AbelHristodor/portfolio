$("document").ready(function () {
    getAll();
});

$('form').on('submit', function (e) {
    e.preventDefault();
    $.ajax({
        type: "POST",
        url: "/api/todo/add/",
        data: {
            text: $("#task").val(),
            csrfmiddlewaretoken: Cookies.get("csrftoken")
        },
        success: function (data) {
            getAll();
        }
    });
})


function getAll() {
    clearFields();
    $.ajax({
        type: "GET",
        url: "/api/todo/getAll/",
        cache: false,
        datatype: "json",
        success: function (data) {
            $("ul#taks-list.list-group.my-3").empty()
            $.each(data, function (index, item) {
                d = document.createElement("a");
                $(d)
                    .html(
                        "<button type='submit' onClick='deleteTodo(this)' class='list-group-item list-group-item-action' id='taskBtn' data-id='" +
                        item['pk'] + "'>" +
                        item['fields']['text'] + "</button>" + "<hr class='my-1'>"
                    )
                    .appendTo("ul#taks-list.list-group.my-3");
            });
        },
    });
};

function deleteTodo(obj) {
    let id = $(obj).data('id');
    $.ajax({
        type: "POST",
        url: "/api/todo/delete/",
        cache: false,
        data: {
            id: id,
            csrfmiddlewaretoken: Cookies.get("csrftoken"),
        },
        success: function () {
            getAll()
        }
    });
};

function clearFields() {
    $('#task').val('');
};