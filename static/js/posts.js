////////////
// JavaScript for Posts page
//////////

$(function() {
    // Executed when js-menu-icon js clicked
    $('.js-menu-icon').click(function() {
        // $(this) : self element, namely div.js-menu-icon
        // next() : next to div.js-menu-icon, namely div.menu
        // toggle() : Switch between show and hiding display
        $(this).next().toggle();
    })
})