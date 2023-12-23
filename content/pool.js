// function input_hover(hover){
//     $
// }
$(document).ready(function () {
    $("input[type=text]").focus(function () {
        $(this).css({ "background-color": "#f0d99c", "color": "red" });
    })
    $("input[type=text]").blur(function () {
        $(this).css({ "background-color": '', "color": '' });
    })
    $("input[type=email]").focus(function () {
        $(this).css({ "background-color": "#f0d99c", "color": "red" });
    })
    $("input[type=email]").blur(function () {
        $(this).css({ "background-color": '', "color": '' });
    })
    $("textarea").focus(function () {
        $(this).css({ "background-color": "#f0d99c", "color": "red" });
    })
    $("textarea").blur(function () {
        $(this).css({ "background-color": '', "color": '' });
    })
    $("input[type=submit]").hover(function () {
        $(this).css({ "background-color": "#3cf", "color": "white" });
    })
    $("input[type=submit]").mouseleave(function () {
        $(this).css({ "background-color": "", "color": "" });
    })
    $("input.phone").mask("+7 (999) 999 99-99")
})