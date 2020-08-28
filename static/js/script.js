$(document).ready(function() {
    // code for collapsible
    $(".collapsible").collapsible();
    // code for select
    $("select").material_select();
    // code for side navbar
    $(".button-collapse").sideNav();
    // code for carousel(image slider)
        $(".carousel").carousel();
        setInterval(function() {
        $(".carousel").carousel("next");
    }, 3000);
    // code for modal
    $(".modal").modal();
    // for flash message
    $(".alert.success").hide().delay(1000).fadeIn(200).delay(4000).fadeOut(200);
    // code initializer for character counter in input fields
    $('input#recipe_name, textarea#recipe_description, textarea#recipe_ingredients, textarea#recipe_preparation').characterCounter();
});
// Added underline code to show feedback message of required in the select
//source stack overflow
$("select[required]").css({
    display: "block",
    height: 0,
    padding: 0,
    width: 0,
    position: "absolute",
});
