$(document).ready(function() {
    console.log("Document is ready.");

    $("#start-btn").click(function(event) {
        event.preventDefault();
        $("#expense-creation-table, #create-expense-btn, #add-item-btn").show();
        $("#start-btn").hide();
    });

    $("#add-item-btn").click(function(event) {
        event.preventDefault();
        const newRow = $("<tr class='info-entry'></tr>");
        newRow.append("<td><input type='text' name='item-name' required></td>");
        newRow.append("<td><input type='text' name='category-name' required></td>");
        newRow.append("<td><input type='number' name='amount-spent' required></td>");
        newRow.append("<td><button class='delete-btn'>Delete</button></td>");
        $("#expense-creation-table tbody").append(newRow);
    });

    $("#expense-creation-table").on('click', '.delete-btn', function(event) {
        event.preventDefault();
        $(this).closest('tr').remove();
    });

    $("#create-expense-btn").click(function(event) {
        event.preventDefault();

        console.log("Create expense button clicked.");

        let expenseEntries = [];
        $("#expense-creation-table tbody tr").each(function() {
            let item = $(this).find("input[name='item-name']").val();
            let category = $(this).find("input[name='category-name']").val();
            let amount = $(this).find("input[name='amount-spent']").val();
            if(item && category && amount) {
                expenseEntries.push({
                    item: item,
                    category: category,
                    amount: parseFloat(amount)
                });
            }
        });

        console.log("Collected expense entries:", expenseEntries);

        let expense = {
            entries: expenseEntries
        };

        if(expenseEntries.length > 0){
            $.ajax({
                url: "/api/v1/expenses/add",
                type: "POST",
                contentType: 'application/json',
                data: JSON.stringify(expense),
                success: function(response){
                    alert("Expense added successfully.");

                    window.location.href = '/expenses/display';
                },
                error: function(error){
                    console.log("Error:", error);
                }
            });
        }
        else{
            alert("Please add at least one expense entry.");
        }
    });
});
