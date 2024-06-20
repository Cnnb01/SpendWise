window.onload = function() {
let budgetItems = JSON.parse(localStorage.getItem('budgetItems')) || [];
budgetItems.forEach(budgetItem => {
    let newRow = document.createElement('tr');
    newRow.innerHTML = '<td>' + budgetItem.budgetTitle + '</td><td>'+ budgetItem.itemName + '</td><td>' + budgetItem.amountBudgeted + '</td><td contenteditable="true" class="amount_spent"></td><td class="remainder"></td>';
    document.getElementById('budget_table').appendChild(newRow);
});

// calc the remainder
document.querySelectorAll('.amount_spent').forEach(function(element) {
    element.addEventListener('input', function() {
        let amountSpent = parseFloat(this.innerHTML);
        let amountBudgeted = parseFloat(this.previousElementSibling.innerText);
        let remainder = amountBudgeted - amountSpent;
        this.nextElementSibling.innerText = remainder.toFixed(2);
    })
})

document.getElementById('back_button').addEventListener('click', function() {
    // Redirect to the Create Budget page
    window.location.href = 'budgets_create.html';
});
}