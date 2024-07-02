$(document).ready(function(){
    $("#submit_button").click(function(event){
        event.preventDefault(); // prevent default form submission behavior
        let categoryId = $("#category_id").val();
        // var budgetTitle = $("#budget_title").val();
        let expenseAmount = $("#expense_amount").val();

        if(categoryId && expenseAmount){
            $.ajax({
                url:"/api/v1/expenses/add",
                type: "POST",
                contentType: 'application/json',
                data: JSON.stringify({categoryId, expenseAmount}),
                success: function(response){
                    alert("Expense added successfully.");
                    $("#expense_form")[0].reset();//clears the form
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
        window.location.href = '/expenses/display';
    });

    $("#back_button").click(function() {
        window.location.href = '/home';
    });
});