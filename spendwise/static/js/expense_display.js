$(document).ready(function() {
    // Retrieve budgets from localStorage
    let budgets = JSON.parse(localStorage.getItem('budgets')) || [];

    // Function to render the table rows
    function renderTable() {
        $("#budget_table tbody").empty(); // Clear the existing rows
        budgets.forEach((budget, budgetIndex) => {
            budget.entries.forEach((entry, entryIndex) => {
                const newRow = $("<tr></tr>");
                newRow.append(`<td>${budget.title}</td>`);
                newRow.append(`<td>${entry.category}</td>`);
                newRow.append(`<td>${entry.amount}</td>`);
                newRow.append(`<td><button class="delete-btn" data-budget-index="${budgetIndex}" data-entry-index="${entryIndex}">Delete</button></td>`);
                $("#budget_table tbody").append(newRow);
            });
        });
    }

    // Initial render of the table
    renderTable();

    // Handle the delete button click
    $("#budget_table").on('click', '.delete-btn', function() {
        const budgetIndex = $(this).data('budget-index');
        const entryIndex = $(this).data('entry-index');

        // Remove the entry from the budget
        budgets[budgetIndex].entries.splice(entryIndex, 1);

        // If the budget has no more entries, remove the budget itself
        if (budgets[budgetIndex].entries.length === 0) {
            budgets.splice(budgetIndex, 1);
        }

        // Update localStorage
        localStorage.setItem('budgets', JSON.stringify(budgets));

        // Re-render the table
        renderTable();
    });

    // Handle the back button click
    $("#back_button").click(function() {
        window.history.back();
    });
});

