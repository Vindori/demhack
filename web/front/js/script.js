$(window).ready(function () {
    $('#app').css({
        borderRadius: "35px",
        margin: "20px 0px 20px 0px",
        backgroundColor: "black",
        display: "flex",
        justifyContent: "center",
        paddingLeft: "0",
        paddingRight: "0",
        width: "220px",
        height: "60px"
    }).css('background-color', 'red').text('salam alekum').css('background-image', 'url(../)');

    $('#app').click(function(){
        data = {
            'text': $('#text1').val()
        }
        $.post("http://185.119.59.119:8080/api/get_score/", data, function(data, status) {
            $('#text2').val(data.score + '%');
            console.log(data.score);
        }, "json");
    });
});
