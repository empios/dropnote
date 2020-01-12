$(document).ready(function () {
    $(document).on('submit', '#note-activity', function (e) {
        e.preventDefault();
        var form = $(this).serialize();
        $.ajax({
            url: '/post-activity',
            type: 'POST',
            data: form,
            success: function (response) {
                console.log(response);
                location.reload();
            }
        });

    });


    $(document).on('submit', '#login-form', function (e) {
        e.preventDefault();
        var form = $(this).serialize();
        $.ajax({
            url: '/login-activity',
            type: 'POST',
            data: form,
            success: function (res) {
                if(res === "error"){
                    alert("Nie można się zalogować")
                }
                else{
                    console.log("Zalogowano jako", res);
                    window.location = '/'
                    // location.reload();
                }

            }
        });

    });

    $(document).on('submit', '#register-form', function (e) {
        e.preventDefault();
        var form = $('#register-form').serialize();
        $.ajax({
            url: '/register-activity',
            type: 'POST',
            data: form,
            success: function (response) {
                console.log(response);
                window.location = 'login'
            }
        });

    });

    $(document).on('click', '#logout', function (e) {
        e.preventDefault();
        $.ajax({
            url: '/logout',
            type: 'GET',
            success: function (response) {
                console.log(response);
                if(response === 'success') {
                    window.location = 'login';
                }
                else {
                    alert("Coś poszło nie tak");
                }
            }
        });

    });
});