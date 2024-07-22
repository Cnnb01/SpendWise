const doc = document;

doc.addEventListener('DOMContentLoaded', () => {
  let expenseTable = null;
  let baseApiRoute = '/api/v1/budgets';

  // Delete a row when the delete button is clicked
  doc.addEventListener('click', (event) => {
    // insert the table after the start button
    const addItemBtn = doc.getElementById('add-item-btn');
    const createBudgetBtn = doc.getElementById('create-budget-btn');

    if (event.target.id === 'start-btn') {
      event.preventDefault();
      if (!expenseTable) {
        expenseTable = doc.createElement('table');
        expenseTable.id = 'budget-creation-table';
        expenseTable.innerHTML = `
        <thead>
          <tr>
            <th>Item name</th>
            <th>Category</th>
            <th>Amount budgeted</th>
          </tr>
        </thead>
        <tbody>
          <tr class="info-entry">
            <td><input type="text" name='item_name', autofocus></td>
            <td><input type="text" name='category_name'></td>
            <td><input type="number" name='amount_budgeted'></td>
            <td><button class="delete-btn">delete</button></td>
          </tr>
        </tbody>
        `;

        // show hidden buttons, hide start button
        addItemBtn.classList.remove('hidden');
        createBudgetBtn.classList.remove('hidden');
        addItemBtn.insertAdjacentElement('beforebegin', expenseTable);
        event.target.classList.add('hidden');
      }
    }

    // Add table rows on button click
    if (event.target.id === 'add-item-btn') {
      event.preventDefault();
      const tableRow = doc.createElement('tr');
      tableRow.classList.add('info-entry');
      tableRow.innerHTML = `
        <td><input type="text" name='item_name', autofocus></td>
        <td><input type="text" name='category_name'></td>
        <td><input type="number" name='amount_budgeted'></td>
        <td><button class="delete-btn">delete</button></td>
      `;
      expenseTable = doc.getElementById('budget-creation-table');
      const tbody = expenseTable.querySelector('tbody');
      tbody.appendChild(tableRow);
    }

    // delete rows at delete button click
    if (event.target.classList.contains('delete-btn')) {
      event.preventDefault();
      const row = event.target.closest('tr');
      row.remove();

      // remove the table if all data rows are deleted
      const rows = expenseTable.querySelectorAll('tbody tr');
      console.log(rows.length);
      if (rows.length === 0) {
        expenseTable.remove();
        expenseTable = null;
        doc.getElementById('start-btn').classList.remove('hidden');
        addItemBtn.classList.add('hidden');
        createBudgetBtn.classList.add('hidden');
      }
    }

    if (event.target.id === 'start-btn') {
      // Show items that were previously hidden
      doc.getElementById('budget-creation-table').classList.remove('hidden');
      doc.getElementById('add-item-btn').classList.remove('hidden');
      doc.getElementById('create-budget-btn').classList.remove('hidden');
      // hide the start button
      this.classList.add('hidden');
    }

    // make a request to the API
    if (event.target.id === 'create-budget-btn') {
      event.preventDefault();
      const budgetForm =  doc.getElementById('budget_form');
      const budgetTitle = doc.getElementById('budget-title').value;
      const dataRows = doc.querySelectorAll('tbody tr');
      const items = [];

      dataRows.forEach( (dataRow) => {
        const itemName = dataRow.querySelector(`input[name='item_name']`).value;
        const categoryName = dataRow.querySelector(`input[name='category_name']`).value;
        const amountBudgeted = dataRow.querySelector(`input[name='amount_budgeted']`).value;
        items.push({itemName, categoryName, amountBudgeted});
      });

      // make the api call
      fetch(`${baseApiRoute}/add`,{
        method: 'POST',
        headers: {'content-Type': 'application/json'},
        body: JSON.stringify({budgetTitle, items})
      })
      .then(response => response.json())
      .then(data => {
        alert('Budget created successfully');
        window.location.href = '/budgets/display'
      })
      .catch((error) => {
        console.log('Error: ', error);
      })
    }
  });
});
