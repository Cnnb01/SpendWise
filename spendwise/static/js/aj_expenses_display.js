$(document).ready(function(){
    function loadExpenses(){
        $.ajax({
            url: "/api/v1/expenses/get",
            type: "GET",
            success: function(expenses){
                
                expenses.forEach(function(expense){
                    expense.entries.forEach(function(entry) {
                        $('#budget_table tbody').append(
                            '<tr>' +
                            '<td>' + entry.item + '</td>' +
                            '<td>' + entry.category + '</td>' +
                            '<td>' + entry.amount + '</td>' +
                            '<td>' + expense.dateAdded + '</td>' +
                            '</tr>'
                        );
                    });
                });
            },
            error: function(error){
                console.log("Error:", error);
            }
        });
    }
    loadExpenses();

    $("#back_button").click(function() {
        window.location.href = '/expenses/create';
    });
});
