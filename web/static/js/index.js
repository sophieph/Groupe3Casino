$('#start-game').on('click', function() {
    if ($('#form-name').hasClass('inactive')) {
        $('#form-name').removeClass('inactive');
        console.log('bruh')
    } else {
        console.log('kkk');
        $('#form-name').addClass('inactive');
    }
});
