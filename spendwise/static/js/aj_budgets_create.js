// $(document).ready(function(){
//     $("#submit_button").click(function(event){
//         event.preventDefault(); // prevent default form submission behavior
//         var categoryId = $("#category_id").val();
//         var budgetTitle = $("#budget_title").val();
//         var amountPredicted = $("#amount_budgeted").val();

//         if(categoryId && budgetTitle && amountPredicted){
//             $.ajax({
//                 url:"/api/v1/budgets/add",
//                 type: "POST",
//                 contentType: 'application/json',
//                 data: JSON.stringify({categoryId, budgetTitle, amountPredicted}),
//                 success: function(response){
//                     alert("Budget created successfully.");
//                     $("#budget_form")[0].reset();//clears the form
//                 },
//                 error: function(error){
//                     console.log("Error:", error);
//                 }
//             });
//         }
//         else{
//             alert("Please fill in all required fields")
//         }
//     });
//     $("#create-budget-btn").click(function() {
//         window.location.href = '/budgets/display';
//     });

    // $("#back_button").click(function() {
    //     window.location.href = '/home';
    // });
// });

$(document).ready(function() {
    // show table and other buttons when the user starts to create the budget
    $("#start-btn").click(function(event) {
        event.preventDefault();
        // Show table and button that were previously hidden
        $("#budget-creation-table, #create-budget-btn, #add-item-btn").show();
        $("#start-btn").hide();
    });

    // Add more item rows to the table when the add item button is clicked
    $("#add-item-btn").click(function(event) {
        event.preventDefault();
        
        // Create a new table row element
        const newRow = $("<tr></tr>").addClass("budget-entry");
        
        // Add cells (columns) to the new row
        newRow.append("<td><input type='text' name='category_name'></td>"); // Category name
        newRow.append("<td><input type='number' name='amount_budgeted'></td>"); // Amount budgeted
        newRow.append("<td><button type='button' class='delete-btn'>Delete</button></td>"); // Delete button
        
        // Append the new row to the table body
        $("#budget-creation-table tbody").append(newRow);
    });

    // Delete a row when the delete button is clicked
    $(document).on('click', '.delete-btn', function() {
        $(this).closest('tr').remove();
    });

    // Submit form via AJAX
    $("#create-budget-btn").click(function(event) {
        event.preventDefault();
        
        var budgetTitle = $("#budget-title").val();
        var categories = [];
        
        $("#budget-creation-table tbody tr").each(function() {
            var categoryName = $(this).find("input[name='category_name']").val();
            var amountBudgeted = $(this).find("input[name='amount_budgeted']").val();
            
            if (categoryName && amountBudgeted) {
                categories.push({
                    categoryName: categoryName,
                    amountBudgeted: amountBudgeted
                });
            }
        });

        // if (budgetTitle && categories.length > 0) {
            $.ajax({
                url: "/api/v1/budgets/add",
                type: "POST",
                contentType: "application/json",
                data: JSON.stringify({
                    budgetTitle: budgetTitle,
                    categories: categories
                }),
                success: function(response) {
                    alert("Budget created successfully.");
                    $("#budget_form")[0].reset(); // Clears the form
                    $("#budget-creation-table tbody").empty(); // Clears the table
                    $("#budget-creation-table, #create-budget-btn, #add-item-btn").hide(); // Hide the table and buttons
                    $("#start-btn").show(); // Show the start button
                },
                error: function(error) {
                    console.log("Error:", error);
                }
            });
        // } else {
        //     alert("Please fill in all required fields.");
        // }
    });

    // Navigate to budgets display page
    $("#create-budget-btn").click(function() {
        window.location.href = '/budgets/display';
    });
});
