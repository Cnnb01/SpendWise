$(document).ready(function(){
    function loadBudgets(){
        $.ajax({
            url: "/api/v1/budgets/get",
            type: "GET",
            success: function(budgets){
        //         let currentTitle = "";
        //         let currentRow = null;

        //         budgets.forEach(function(budget){
        //             if (budget.budgetTitle !== currentTitle) {
        //                 currentTitle = budget.budgetTitle;
        //                 currentRow = $('<tr>').append('<td>' + currentTitle + '</td>');
        //             }
        //   // Append remaining cells for the current budget
        //             currentRow.append(
        //                 '<td>' + budget.categoryId + '</td>' +
        //                 '<td>' + budget.amountPredicted + '</td>' +
        //                 '<td contenteditable="true" class="amount_spent">' + budget.amountSpent + '</td>' +
        //                 '<td class="balance">' + budget.balance + '</td>'
        //             );
        //         });
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