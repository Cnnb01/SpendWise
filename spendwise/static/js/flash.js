// For message alerts

$(document).ready(function(){
  // when the close button is clicked
  $('.alert .close').click(function(event) {
    $(this).parent().remove();
  });

  // if the button is not clicked, vanish the alert after a set time
  const TIMEOUT = 2500;
  $('.alert').delay(TIMEOUT).fadeOut(function() {
    $(this).remove();
  });
});
