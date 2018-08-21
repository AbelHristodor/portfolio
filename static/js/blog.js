$('document').ready(function () {
    getAllArticles();
});

function getAllArticles() {
    clearFieldsModal();
    $.ajax({
        type: "GET",
        url: "/api/blog/getAll/",
        cache: false,
        datatype: "json",
        success: function (data) {
            $('.articles').empty();
            $.each(data, function (index, item) {
                d = document.createElement("div")
                $(d)
                    .addClass("row padding")
                    .html('<div class="col-md-3"></div>' +
                        '<div class="col-md-6">' +
                        '<div class="card text-dark">' +
                        '<div class="card-header">' +
                        '<a id="articleHeader" href="/blog/content/'+ item['pk'] +'">' +
                        '<h3 class="card-title">' + item['fields']['title'] + '</h3>' +
                        '<h5 style="float:left">' +
                        '<b class="font-weight-light">Author: ' + item['fields']['author'] + '</b></h5>' +
                        '<h5 style="float:right">' +
                        '<i class="font-weight-light">Published: ' + item['fields']['published_date'].replace('T', ' ').replace('Z', ' ') + '</i></h5></a></div>' +
                        '<div class="card-body">' +
                        '<p class="card-text">' + item['fields']['text'] +
                        '<button style="float:right" class="btn btn-sm btn-dark my-md-3" onClick="deleteBlog(this)" data-id="' + item['pk'] + '">Delete article</button></p></div></div></div>' +
                        '<div class="col-md-3"></div>')
                    .appendTo('.articles')
            });
        }
    });

};

$('.modal').on('')
$('form').on('submit', function (e) {
    e.preventDefault();
    $.ajax({
        type: "POST",
        url: "/api/blog/add/",
        data: {
            title: $('#title').val(),
            author: $('#author').val(),
            text: $('#text').val(),
            csrfmiddlewaretoken: Cookies.get("csrftoken")
        },
        success: function () {
            $('.modal').modal('hide');
            getAllArticles();
        },
    });
});

function deleteBlog(obj) {
    let id = $(obj).data('id');
    $.ajax({
        type: "POST",
        url: "/api/blog/delete/",
        cache: false,
        data: {
            id: id,
            csrfmiddlewaretoken: Cookies.get("csrftoken"),
        },
        success: function () {
            getAllArticles()
        }
    });
};

function clearFieldsModal() {
    $('#title').val("");
    $('#author').val("");
    $('#text').val("");
};