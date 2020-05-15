//var delayTimer;
//$('#post-text').keyup(function(){
//    clearTimeout(delayTimer);
//    $('#search_results').text('Loading...');
//    delayTimer = setTimeout(function() {
//        var text = $('#post-text').val();
//        $.ajax({
//            url: '/sharespace/create_post',
//            type: 'POST',
//            data: {
//                'search_term': text
//            },
//            dataType: 'json',
//            success: function(data) {
//                $('#search_results').text(data['form']);
//            }
//        });
//    }, 1000);
//});


//$('#post-form').on('submit', function(event){
//    event.preventDefault();
//    console.log("form submitted!")
//    create_post();
//});



$(function () {

//    $(".js-create-room").click(function () {
//        var btn = $(this);
//        $.ajax({
//            url: btn.attr("data-url"),
//            type: 'get',
//            dataType: 'json',
//            beforeSend: function () {
//                $("#modal-room").modal("show");
//            },
//            success: function (data) {
//                $("#modal-room .modal-content").html(data.html_form);
//            }
//        });
//        console.log('clicked')
//    });

    var loadForm = function () {
        var btn = $(this);
        console.log("before button clicked")
        $.ajax({
            url: btn.attr("data-url"),
            type: 'get',
            dataType: 'json',
            beforeSend: function () {
                $("#modal-room").modal("show");
            },
            success: function (data) {
                $("#modal-room .modal-content").html(data.html_form)
                console.log("clicked");
            }
        });

    };

    var saveForm = function () {
        var form = $(this);
        $.ajax({
            url: form.attr("action"),
            data: form.serialize(),
            type: form.attr("method"),
            dataType: 'json',
            success: function (data) {
                if (data.form_is_valid) {
                    $("#myTable tbody").html(data.html_room_list);
                    $("#modal-room").modal("hide");
                }
                else {
                    $("modal-room .modal-content").html(data.html_form);
                }
            }
        });
        return false;
    };

    //Binding

    //Create room
    $(".js-create-room").on("click", loadForm);
    $("#modal-room").on("submit", ".js-room-create-form", saveForm);

    //Update book
    $("#myTable").on("click", ".js-update-book", loadForm);
    $("#modal-room").on("submit", ".js-room-update-form", saveForm);

    //Delete book
    $("#myTable").on("click", ".js-delete-room", loadForm);
    $("#modal-room").on("submit", ".js-room-delete-form", saveForm);

});



//$(function () {
//    console.log("Hello!")
//    $.ajax({
//        url: '/sharespace/list',
//        type: 'get',
//        dataType: 'json',
//        success: function(data) {
//            let rows = ''
//            data.rooms.forEach((room) =>{
//                rows += `<tr> <td>${room.id}</td>
//                <td>${room.name}</td>
//                <td>${room.nobeds}</td>
//                <td>${room.room_type}</td>
//                <td>
//                    <button class="btn btn-danger" data-id=${room.id}>Delete</button>
//                    <button class="btn btn-danger" data-id=${room.id}>Update</button>
//                </td> </tr>`
//            })
////            console.log(rows)
//            $('#tabl').append(rows).animate({height: "+=10px"}, 300);
//
////                $('.deleteBtn').each((i, elm) => {
////                    $(elm).on("click", (e) => {
////                        deleteRoom($(elm))
////                    })
////                })
////            data.rooms.forEach((room) => {console.log(room)})
//
//        }
//
//    });
//
//});
//stop();
//
//function deleteRoom(el){
//    roomId = $(el).data('id')
//    $.ajax({
//        url: `/delete/{room.Id}`,
//        type: 'post',
//        dataType: 'json',
//        success: function (data) {
//            $(el).parents()[1].remove()
//        }
//    });
//}