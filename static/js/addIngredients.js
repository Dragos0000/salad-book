
function addIngredient() {

    let maxOfIngredients = 10; 
    let addIngredientButton = $('.add_button'); 
    let addIngredientDiv = $('.ingredient_div');
    let addIngredientFieldHtml = '<div class="row"><div class="input-field ingredient_div col s10"><i class="material-icons prefix">edit</i><input type="text" name="ingredients" value="" required/><label for="icon_prefix">Add Ingredient</label></div><a href="javascript:void(0);" class="remove_button validate"><i class="material-icons prefix">clear</i></a></div>'; 
    let ingredientNumber = 1;

    //add ingredient
    $(addIngredientButton).click(function() {
        if (ingredientNumber < maxOfIngredients) {
            ingredientNumber++; 
            $(addIngredientDiv).append(addIngredientFieldHtml);
        }
    });

    //remove ingredient 
    $(addIngredientDiv).on('click', '.remove_button', function(e) {
        e.preventDefault();
        $(this).parent('div').remove();
        ingredientNumber--; 
    });
};