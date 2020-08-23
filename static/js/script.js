
$(document).ready(function() {
    $('.carousel').carousel({
    padding: 200    
    });
    setInterval(function(){
        $('.carousel').carousel('next');
    }, 2000);
    // code initializer for collapsible
    $(".collapsible").collapsible();
    // code initializer for select
    $("select").material_select();
    // code initializer for side navbar
    $(".button-collapse").sideNav();
    $('select').formSelect();
    // code initializer for carousel(image slider)
    
    
    // code initializer for modal
    $(".modal").modal();
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
$(".datepicker").pickadate({
    selectMonths: true, // Creates a dropdown to control month
    selectYears: 15, // Creates a dropdown of 15 years to control year,
    today: "Today",
    clear: "Clear",
    close: "Ok",
    closeOnSelect: false, // Close upon selecting a date,
});

// Added underline code to make date picker field required
// source stack overflow
$(".datepicker").prop("readonly", false);