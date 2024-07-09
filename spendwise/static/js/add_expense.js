$(document).ready(function() {
    $("#start-btn").click(function(event) {
        event.preventDefault();
        $("#budget-creation-table, #create-budget-btn, #add-item-btn").show();
        $("#start-btn").hide();
    });

    $("#add-item-btn").click(function(event) {
        event.preventDefault();
        const newRow = $("<tr class='budget-entry'></tr>");
        newRow.append("<td><input type='text' name='category-name[]' required></td>");
        newRow.append("<td><input type='number' name='amount-spent[]' required></td>");
        newRow.append("<td><button class='delete-btn'>Delete</button></td>");
        $("#budget-creation-table tbody").append(newRow);
    });

    $("#budget-creation-table").on('click', '.delete-btn', function(event) {
        event.preventDefault();
        $(this).closest('tr').remove();
    });

    // Capture form submission
    $("#budget-form").submit(function(event) {
        event.preventDefault();
        const formData = $(this).serializeArray();
        const budgetTitle = $("#budget-title").val();
        const budgetEntries = [];

        formData.forEach(item => {
            if (item.name === "category-name[]") {
                budgetEntries.push({ category: item.value });
            } else if (item.name === "amount-spent[]") {
                budgetEntries[budgetEntries.length - 1].amount = item.value;
            }
        });

        const budget = {
            title: budgetTitle,
            entries: budgetEntries
        };

        // Save budget to localStorage
        let budgets = JSON.parse(localStorage.getItem('budgets')) || [];
        budgets.push(budget);
        localStorage.setItem('budgets', JSON.stringify(budgets));

        // Navigate to display.html
        window.location.href = 'display_expenses.html';
    });
});
