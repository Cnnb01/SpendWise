$(document).ready(function () {
  $('#signup-form').on('submit', function(event) {
    event.preventDefault(); // prevent default form submission behavior

    const firstName = $('#first-name').val();
    const lastName = $('#last-name').val();
    const email = $('#email').val();
    const passwd = $('#passwd').val();
    const confirmedPasswd = $('#confirm-passwd').val();

    if (passwd != confirmedPasswd) {
      alert('Passwords don\'t match. Try again');
      return;
    }

    // AJAX request to send the form
    $.ajax({
      url: '/api/v1/register',
      type: 'POST',
      contentType: 'application/json',
      data: JSON.stringify({firstName: firstName, lastName: lastName, email: email, passwd: passwd}),
    });
  });
});
