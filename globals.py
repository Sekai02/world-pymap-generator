VALID_TAG_COMBINATIONS = [
    ("forest", "exploration", "easy", "outdoor"),
    ("cave", "combat", "hard", "underground"),
    ("castle", "puzzle", "medium", "indoor"),
    ("desert", "survival", "hard", "outdoor"),
    ("dungeon", "treasure", "medium", "underground"),
    ("mountain", "climbing", "hard", "outdoor"),
    ("village", "social", "easy", "indoor"),
    #can add more
]

#similarity matrix for theme
theme_sim = {
    "forest": {"forest": 10, "cave": 3, "castle": 2, "desert": 4, "dungeon": 3, "mountain": 7, "village": 5},
    "cave": {"forest": 3, "cave": 10, "castle": 4, "desert": 2, "dungeon": 8, "mountain": 6, "village": 1},
    "castle": {"forest": 2, "cave": 4, "castle": 10, "desert": 5, "dungeon": 6, "mountain": 3, "village": 8},
    "desert": {"forest": 4, "cave": 2, "castle": 5, "desert": 10, "dungeon": 4, "mountain": 7, "village": 3},
    "dungeon": {"forest": 3, "cave": 8, "castle": 6, "desert": 4, "dungeon": 10, "mountain": 5, "village": 2},
    "mountain": {"forest": 7, "cave": 6, "castle": 3, "desert": 7, "dungeon": 5, "mountain": 10, "village": 4},
    "village": {"forest": 5, "cave": 1, "castle": 8, "desert": 3, "dungeon": 2, "mountain": 4, "village": 10}
}

#similarity matrix for function
function_sim = {
    "exploration": {"exploration": 10, "combat": 3, "puzzle": 4, "survival": 5, "treasure": 6, "climbing": 8, "social": 2},
    "combat": {"exploration": 3, "combat": 10, "puzzle": 5, "survival": 7, "treasure": 8, "climbing": 6, "social": 1},
    "puzzle": {"exploration": 4, "combat": 5, "puzzle": 10, "survival": 3, "treasure": 4, "climbing": 6, "social": 7},
    "survival": {"exploration": 5, "combat": 7, "puzzle": 3, "survival": 10, "treasure": 5, "climbing": 8, "social": 2},
    "treasure": {"exploration": 6, "combat": 8, "puzzle": 4, "survival": 5, "treasure": 10, "climbing": 7, "social": 3},
    "climbing": {"exploration": 8, "combat": 6, "puzzle": 6, "survival": 8, "treasure": 7, "climbing": 10, "social": 4},
    "social": {"exploration": 2, "combat": 1, "puzzle": 7, "survival": 2, "treasure": 3, "climbing": 4, "social": 10}
}

#similarity matrix for environment
environment_sim = {
    "outdoor": {"outdoor": 10, "underground": 2, "indoor": 4},
    "underground": {"outdoor": 2, "underground": 10, "indoor": 3},
    "indoor": {"outdoor": 4, "underground": 3, "indoor": 10}
}

#similarity matrix for difficulty
difficulty_sim = {
    "easy": {"easy": 10, "medium": 6, "hard": 3},
    "medium": {"easy": 6, "medium": 10, "hard": 7},
    "hard": {"easy": 3, "medium": 7, "hard": 10}
}

#weights for each tag
w_t = 1.0
w_f = 1.0
w_e = 1.0
w_d = 1.0