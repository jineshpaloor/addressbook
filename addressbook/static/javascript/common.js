$(document).ready(function() {

    $("#add-contact").click(function (){
        var content = $("#content");
        $.ajax({
            url:'/address/add/',
            type: 'GET',
            success: function (resp){
                $(content).html(resp.html);
            }
        });
    });

    $("#add-contact-submit").live('click', function (e){
            e.preventDefault();
            var form = $("#add-contact-form");
            var content = $("#content");
            $.ajax({
                url:'/address/add/',
                type: 'POST',
                data: $(form).serialize(),
                dataType: 'json',
                success: function (resp){
                    $(content).html(resp.html);
                }
            });
    });


});

