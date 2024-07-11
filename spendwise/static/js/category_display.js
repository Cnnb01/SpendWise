$(document).ready(function(){
    function loadCategories(budgetId){
        $.ajax({
            url: "/api/v1/budgets/" + budgetId + "/categories",
            type: "GET",
            success: function(data){
                console.log("Received data:", data);//debbugging
                $("#category_table").find("tr:gt(0)").remove();//clearing existing rows except the header
                $("h1").text(data.budgetTitle + " Categories");
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

    // extract budgetId from URL path
    var pathArray = window.location.pathname.split('/');
    var budgetId = pathArray[pathArray.length - 2];

    if (budgetId) {
        loadCategories(budgetId);
    }

    $("#back_button").click(function() {
        window.location.href = '/budgets/display';
    });
});

