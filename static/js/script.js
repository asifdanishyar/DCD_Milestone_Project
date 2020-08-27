$(document).ready(function() {
    // code initializer for collapsible
    $(".collapsible").collapsible();
    // code initializer for select
    $("select").material_select();
    // code initializer for side navbar
    $(".button-collapse").sideNav();
    // code initializer for carousel(image slider)
    $(".carousel").carousel();
    setInterval(function() {
        $(".carousel").carousel("previous");
    }, 2000);
    // code initializer for modal
    $(".modal").modal();
    $("select").formselect();
    // code initializer for flash message
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
