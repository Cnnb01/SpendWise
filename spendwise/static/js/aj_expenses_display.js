$(document).ready(function(){
    function loadExpenses(){
        $.ajax({
            url: "/api/v1/expenses/get",
            type: "GET",
            success: function(budgets){
                budgets.forEach(function(budget){
                    $('#expense_table').append(
                        '<tr><td>' + expense.categoryId + '</td>' +
                        '<td>' + expense.expenseAmount + '</td>' +
                        '<td>' + expense.dateAdded + '</td></tr>'
                    );
                });
            },
            error: function(error){
                console.log("Error:", error);
            }
        });
    }
    loadExpenses();
    $("#back_button").click(function() {
        window.location.href = '/expenses/create';
    });
});