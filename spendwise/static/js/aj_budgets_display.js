$(document).ready(function(){
    function loadBudgets(){
        $.ajax({
            url: "http://localhost:5000/api/v1/budgets",
            type: "GET",
            success: function(budgets){
                budgets.forEach(function(budget){
                    $('#budget_table').append(
                        '<tr><td>' + budget.bugetTitle + '</td>' +
                        '<td>' + budget.itemName + '</td>' +
                        '<td>' + budget.amountPredicted + '</td>' +
                        '<td>' + budget.amountSpent + '</td>' +
                        '<td>' + budget.balance + '</td></tr>'
                    );
                });
            },
            error: function(error){
                console.log("Error:", error);
            }
        });
    }
    loadBudgets();
    $("#back_button").click(function() {
        window.location.href = 'budgets_create.html';
    });
});