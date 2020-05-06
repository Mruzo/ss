$('.likebutton').click(function(){
var catid;
catid = $(this).attr("data-catid");
$.ajax({
    type: "GET",
    url: "spaceblog/likepost",
    data: {
        post_id: catid
    },
    success: function( data ) {
        $('#like' + catid ).remove();
        $('#message').text(data);
    }
})
})