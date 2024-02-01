let selectedCountry = $('#id_default_country').val();
if (!selectedCountry) {
    $('#id_default_country').css('color', '#cccccc');
};
$('#id_default_country').change(function () {
    selectedCountry = $(this).val();
    if (!selectedCountry) {
        $(this).css('color', '#cccccc');
    } else {
        $(this).css('color', '#000');
    }
})