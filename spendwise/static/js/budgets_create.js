window.onload = function() {
let budgetItems = JSON.parse(localStorage.getItem('budgetItems')) || [];

document.getElementById('submit_button').addEventListener('click', function(){
    let budgetTitle = document.getElementById('budget_title').value;
    let itemName = document.getElementById('item_name').value;
    let amountBudgeted = document.getElementById('amount_budgeted').value;
    // save the budget item to local storage
    budgetItems.push({
        budgetTitle: budgetTitle,
        itemName: itemName,
        amountBudgeted: amountBudgeted
    });
    localStorage.setItem('budgetItems', JSON.stringify(budgetItems));
    // clear form fields
    document.getElementById('budget_title').value = '';
    document.getElementById('item_name').value = '';
    document.getElementById('amount_budgeted').value = '';
});

document.getElementById('done_button').addEventListener('click', function() {
    // redirect to display on the display page
    window.location.href = 'budgets_display.html';
});

document.getElementById('back_button').addEventListener('click', function() {
    // redirect to display on the display page
    window.location.href = 'budgets.html';
});
}

// // Store
// localStorage.setItem("lastname", "Smith");
// for reading the localStorage .getItem()
// // Retrieve
// document.getElementById("result").innerHTML = localStorage.getItem("lastname");
// JSON.parse() JavaScript method that converts a JSON string into a JavaScript object