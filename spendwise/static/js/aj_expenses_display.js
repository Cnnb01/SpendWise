$(document).ready(function() {
    function loadExpenses() {
        $.ajax({
            url: "/api/v1/expenses/get",
            type: "GET",
            success: function(expenses) {
                $('#budget_table tbody').empty();  // Clear existing table rows
                
                expenses.forEach(function(expense) {
                    let dateAdded = new Date(expense.dateAdded).toLocaleDateString(); // Format the date

                    $('#budget_table tbody').append(
                        '<tr>' +
                        '<td>' + expense.itemName + '</td>' +
                        '<td>' + expense.categoryId + '</td>' +
                        '<td>' + expense.expenseAmount + '</td>' +
                        '<td>' + dateAdded + '</td>' +
                        '</tr>'
                    );
                });
            },
            error: function(error) {
                console.log("Error:", error);
            }
        });
    }
    
    loadExpenses();

    $("#back_button").click(function() {
        window.location.href = '/expenses/create';
    });
});

