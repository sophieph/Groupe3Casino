$( document ).ready(function() {
    $('#game').prop('disabled', false);
});

$('#start-game').on('click', function() {
    if ($('#form-name').hasClass('inactive')) {
        $('#form-name').removeClass('inactive');
    } else {
        $('#form-name').addClass('inactive');
    }
});

$('#start_game').on('click', function() {
    $('#game').removeClass('inactive');
    $('#game').prop('disabled', true);
});

$('#set-level').click(function(e){
    e.preventDefault();

    $.ajax({
        url: '/set-level',
        data: $('#level').serialize(),
        type: 'POST',
        success: function(res) {
            resu = jQuery.parseJSON(res);
            console.log(resu);

            if (resu.status == "OK") {
                $('#level').toggleClass('inactive');
                $('#level').prop('disabled', false);
                $('#game').removeClass('inactive');
                $('#game').prop('disabled', true);
                $('#error').html('');
                $('#error').removeClass('alert alert-danger')

            } else {
                $('#error').html('Mettez un niveau entre 1 et 3');
                $('#error').addClass('alert alert-danger')

            }
        },
        error: function(error){
            console.log(error);
        }
    });
});
