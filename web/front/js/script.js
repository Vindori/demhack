$(window).ready(function () {

    $('#app').click(function(){
        data = {
            'text': $('#text1').val()
        }
        $.post("http://185.119.59.119:8080/api/get_score/", data, function(data, status) {
            $('#text2').text(data.score + '%');
            console.log(data.score);
        }, "json");
    });
});
