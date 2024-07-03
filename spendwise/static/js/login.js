$(document).ready(function () {
  $('#login-form').on('submit', function (event) {
    event.preventDefault(); // prevent default form submission behavior

    const email = $('#email').val();
    const password = $('#password').val();

    const showLoginSuccess = function (response) {
      // redirect the user to the appropriate page
      window.location.href = response.redirect;
    };

    const showLoginFailure = function (jqXHR, textStatus, errorThrown) {
      const message = jqXHR.responseJSON.message;
      alert(message);
    };

    // AJAX request to send the form
    $.ajax({
      url: '/api/v1/login',
      type: 'POST',
      contentType: 'application/json',
      data: JSON.stringify({email, password}),
      success: showLoginSuccess,
      error: showLoginFailure
    });
  });
});
