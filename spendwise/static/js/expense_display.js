$(document).ready(function() {
  $.ajax({
      url: "/api/v1/expenses/get",
      type: "GET",
      success: function(response) {
        // item name, category, amount spent, date added
        response.forEach(expense => {
          const expenseRow = $(`<tr></tr>`)

          // add columns to the row
          expenseRow.append(`<td>${expense.itemName}</td>`);
          expenseRow.append(`<td>${expense.categoryId}</td>`);
          expenseRow.append(`<td>${expense.expenseAmount}</td>`);
          expenseRow.append(`<td>${expense.dateAdded}</td>`);

          $('#expense_table').append(expenseRow);
        });
        console.log(response);
      },
      error: function(error) {
          console.log("Error:", error);
      }
  });

  $("#back_button").click(function() {
    window.location.href = '/expenses/create';
  });
});
