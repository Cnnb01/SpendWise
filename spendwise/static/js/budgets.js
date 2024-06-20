window.onload = function() {
let navbarItems = document.getElementsByClassName('navbar_item');

// removes 'selected' class from all items hence non is selscted 
function removeSelectedClass() {
    for (let i = 0; i < navbarItems.length; i++) {
        navbarItems[i].classList.remove('selected');
    }
}


for (let i = 0; i < navbarItems.length; i++) {
    navbarItems[i].addEventListener('click', function(){
        removeSelectedClass();
        this.classList.add('selected');
    });
}
}