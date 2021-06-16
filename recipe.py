class Recipe:

    def __init__(
        self,
        _id,
        cuisine_type,
        recipe_name,
        meal_time,
        description,
        servings,
        is_vegetarian,
        prep_time,
        cooking_time,
        ingredients,
        method,
        allergens,
        image,
        video,
        recipe_by
    ):
        self._id = _id
        self.cuisine_type = cuisine_type
        self.recipe_name = recipe_name
        self.meal_time = meal_time
        self.description = description
        self.servings = servings
        self.is_vegetarian = is_vegetarian
        self.prep_time = prep_time
        self.cooking_time = cooking_time
        self.ingredients = ingredients
        self.method = method
        self.allergens = allergens
        self.image = image
        self.video = video
        self.recipe_by = recipe_by