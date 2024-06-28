$(document).ready(function(){
    $("#submit_button").click(function(){
        var categoryId = $("#category_id").val();
        var budgetTitle = $("#budget_title").val();
        var amountPredicted = $("#amount_budgeted").val();

        if(categoryId && budgetTitle && amountPredicted){
            $.ajax({
                url:"/api/v1/budgets/add",
                type: "POST",
                contentType: 'application/json',
                data: JSON.stringify({categoryId, budgetTitle, amountPredicted}),
                success: function(response){
                    alert("Budget created successfully.");
                    $("#budget_form")[0].reset();//clears the form
                },
                error: function(error){
                    console.log("Error:", error);
                }
            });
        }
        else{
            alert("Please fill in all required fields")
        }
    });
    $("#done_button").click(function() {
        window.location.href = 'budgets_display.html';
    });

    $("#back_button").click(function() {
        window.location.href = 'budgets.html';
    });
});