$(document).ready(function() {
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
        newRow.append("<td><button class='delete-btn'>delete</button></td>");
        $("#expense-creation-table tbody").append(newRow);
    });

    $("#expense-creation-table").on('click', '.delete-btn', function(event) {
        event.preventDefault();
        $(this).closest('tr').remove();
    });

    // Capture form submission
    $("#expense-form").submit(function(event) {
        event.preventDefault();
        const formData = $(this).serializeArray();
        const expenseTitle = $("#expense-title").val();
        const expenseEntries = [];

        formData.forEach(item => {
            if (item.name === "category-name[]") {
                expenseEntries.push({ category: item.value });
            } else if (item.name === "amount-spent[]") {
                expenseEntries[expenseEntries.length - 1].amount = item.value;
            }
        });

        const expense = {
            title: expenseTitle,
            entries: expenseEntries
        };

        // Save expense to localStorage
        // let expenses = JSON.parse(localStorage.getItem('expenses')) || [];
        // expenses.push(expense);
        // localStorage.setItem('expenses', JSON.stringify(expenses));

        // Navigate to display.html
        window.location.href = 'display_expenses.html';
    });
});
