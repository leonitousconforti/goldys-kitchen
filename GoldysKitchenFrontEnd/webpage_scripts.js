// Stores the current ingredients the user has inputed
const ingredientsList = [];
const ingredients = [];

function addIngredient() {
    // 1. Get the user input from the saerch box
    var inputValue = document.getElementById('ingredient-input').value;

    // 2. Add it to the ingredients list
    ingredientsList.push(inputValue);

    // 3. update the list html
    updateIngredientListHTML();
}

function updateIngredientListHTML() {
    // 1. Grab a reference to the html unordered list for the ingredients
    const unorderedList = document.getElementById("ingredient-list");

    // 2. Clear all the current elements
    unorderedList.innerHTML = '';

    // 3. Add all the ingredients as list items
    for (const ingredient of ingredientsList) {
        unorderedList.innerHTML += `<li>${ingredient}</li>`;
    }
}

function keyPressed(event) {
    var k = event.key;
    if (k == "Tab") {
        event.preventDefault();
        if (document.getElementById("ingredient-input").value != "")
        {
            addIngredient();
            document.getElementById("ingredient-input").value = "";   
        }
    } else if (k == "Enter") {
        event.preventDefault();
        if (document.getElementById("ingredient-input").value != "")
        {
            addIngredient();
            document.getElementById("ingredient-input").value = "";   
        }
    }
}