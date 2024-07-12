$(document).ready(function(){
    function loadBudgets(){
        $.ajax({
            url: "/api/v1/budgets/get",
            type: "GET",
            success: function(budgets){
              const budgetTable = $('#budget_table');
                budgets.forEach(function(budget){
                  const budgetRow = $(`<tr></tr>`);
                  budgetRow.append(`<td><a href="/budgets/${budget.Id}/categories">${budget.budgetTitle}</a></td>`);
                  budgetRow.append(`<td>${budget.amountPredicted}</td>`);
                  budgetRow.append(`<td contenteditable="true" class="amount_spent">${budget.amountSpent}</td>`);
                  budgetRow.append(`<td class="balance">${budget.balance}</td>`);
                  budgetTable.append(budgetRow);
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