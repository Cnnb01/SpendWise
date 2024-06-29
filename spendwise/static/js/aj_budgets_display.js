$(document).ready(function(){
    function loadBudgets(){
        $.ajax({
            url: "/api/v1/budgets/get",
            type: "GET",
            success: function(budgets){
                budgets.forEach(function(budget){
                    $('#budget_table').append(
                        '<tr><td>' + budget.budgetTitle + '</td>' +
                        '<td>' + budget.categoryId + '</td>' +
                        '<td>' + budget.amountPredicted + '</td>' +
                        '<td contenteditable="true" class="amount_spent">' + budget.amountSpent + '</td>' +
                        '<td class="balance">' + budget.balance + '</td></tr>'
                    );
                });
                // calculating the balance and making amount_spent editable
                $('.amount_spent').on('input', function(){
                    let amountSpent = parseFloat($(this).text());
                    let amountPredicted = parseFloat($(this).prev().text());
                    let balance = amountPredicted - amountSpent;
                    $(this).next().text(balance.toFixed(2));
                });
            },
            error: function(error){
                console.log("Error:", error);
            }
        });
    }
    loadBudgets();
    $("#back_button").click(function() {
        window.location.href = '/budgets/create';
    });
});