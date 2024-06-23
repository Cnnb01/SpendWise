$(document).ready(function () {
  $('#signup-form').on('submit', function (event) {
    event.preventDefault(); // prevent default form submission behavior

    const firstName = $('#first-name').val();
    const lastName = $('#last-name').val();
    const email = $('#email').val();
    const passwd = $('#passwd').val();
    const confirmedPasswd = $('#confirm-passwd').val();

    if (passwd !== confirmedPasswd) {
      alert('Passwords don\'t match. Try again');
      return;
    }

    const showSignupSuccess = function (response) {
      alert(response.message);
    };

    const showSignupFailure = function (jqXHR, textStatus, errorThrown) {
      const message = jqXHR.responseJSON.message;
      alert(message);
    };

    // AJAX request to send the form
    $.ajax({
      url: '/api/v1/register',
      type: 'POST',
      contentType: 'application/json',
      data: JSON.stringify({ firstName, lastName, email, passwd }),
      success: showSignupSuccess,
      error: showSignupFailure
    });
  });
});
