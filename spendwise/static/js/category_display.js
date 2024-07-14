$(document).ready(function(){
    function loadCategories(budgetId){
        $.ajax({
            url: `/api/v1/budgets/${budgetId}/categories`,
            type: "GET",
            success: function(data){
                console.log("Received data:", data);//debbugging
                $("#category_table").find("tr:gt(0)").remove();//clearing existing rows except the header
                $("h1").text(data.budgetTitle + " Categories");
                data.categories.forEach(function(category){
                  const category_table = $('#category_table');
                  const table_row = $(`<tr></tr>`)
                  table_row.append(`<td>${category.category_name}</td>`)
                  table_row.append(`<td>${category.amount_budgeted}</td>`)
                  category_table.append(table_row);
                });
            },
            error: function(error){
                console.log("Error:", error);
            }
        });
    }

    // extract budgetId from URL path
    const pathArray = window.location.pathname.split('/');
    const budgetId = pathArray[pathArray.length - 2];

    if (budgetId) {
        loadCategories(budgetId);
    }

    $("#back_button").click(function() {
        window.location.href = '/budgets/display';
    });
});

