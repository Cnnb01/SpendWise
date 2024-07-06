$(document).ready(function(){
    function loadCategories(budgetId){
        $.ajax({
            url: "/api/v1/budgets/" + budgetId + "/categories",
            type: "GET",
            success: function(data){
                $("#budget-title").text(data.budgetTitle + " Categories");
                data.categories.forEach(function(category){
                    $('#category_table').append(
                        '<tr>' +
                        '<td>' + category.category_name + '</td>' +
                        '<td>' + category.amount_budgeted + '</td>' +
                        '</tr>'
                    );
                });
            },
            error: function(error){
                console.log("Error:", error);
            }
        });
    }

    // Extract budgetId from URL
    var urlParams = new URLSearchParams(window.location.search);
    var budgetId = urlParams.get('budgetId');

    if (budgetId) {
        loadCategories(budgetId);
    }

    $("#back_button").click(function() {
        window.location.href = '/budgets/display';
    });
});
