$(document).ready(function() {
  $.ajax({
      url: "/api/v1/expenses/get",
      type: "GET",
      success: function(response) {
        // item name, category, amount spent, date added
        response.forEach(expense => {
          const expenseRow = $(`<tr></tr>`);

          // format the date to be human-readable
          const rawDate = new Date(expense.dateAdded);
          const dateOptions = {
            weekday: 'short', // e.g., Thu
            day: 'numeric',   // e.g., 4
            month: 'short',   // e.g., Jun
            year: 'numeric'   // e.g., 2024
          };
          const formattedDate = rawDate.toLocaleDateString(undefined, dateOptions);
          // add columns to the row
          expenseRow.append(`<td>${expense.itemName}</td>`);
          expenseRow.append(`<td>${expense.categoryName}</td>`);
          expenseRow.append(`<td>${expense.expenseAmount}</td>`);
          expenseRow.append(`<td>${formattedDate}</td>`);

          $('#expense_table').append(expenseRow);
        });
        
      },
      error: function(error) {
          console.log("Error:", error);
      }
  });

  $("#back_button").click(function() {
    window.location.href = '/expenses/create';
  });
});
