$(document).ready(function () {
  $('#login-form').on('submit', function (event) {
    event.preventDefault(); // prevent default form submission behavior

    const email = $('#email').val();
    const passwd = $('#password').val();


    // AJAX request to send the form
    $.ajax({
      url: '/api/v1/login',
      type: 'POST',
      contentType: 'application/json',
      data: JSON.stringify({ email: email, password: password }),
      success: showLoginSuccess,
      error: showLoginFailure
    });
  });
});


function showLoginSuccess(response) {
	$('#message').text(response.message);
	if (response.redirect) {
		window.location.href = response.redirect;
	}
}

function showLoginFailure(response) {
	$('#message').text(response.responseJSON.message);
}
