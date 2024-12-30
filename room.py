class Room:

    def __init__(self, theme_tag: str, function_tag: str, difficulty_tag: str, environment_tag: str):
        self.theme_tag = theme_tag
        self.function_tag = function_tag
        self.difficulty_tag = difficulty_tag
        self.environment_tag = environment_tag

    def validate_tags(self) -> bool:
        from globals import VALID_TAG_COMBINATIONS

        return (self.theme_tag, self.function_tag, self.difficulty_tag, self.environment_tag) in VALID_TAG_COMBINATIONS
