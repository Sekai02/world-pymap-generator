class MetaRoom:

    def __init__(self, theme_tag, function_tag, difficulty_tag, environment_tag):
        self.theme_tag = theme_tag
        self.function_tag = function_tag
        self.difficulty_tag = difficulty_tag
        self.environment_tag = environment_tag

    def validate_tags(self):
        from globals import VALID_TAG_COMBINATIONS

        return (self.theme_tag, self.function_tag, self.difficulty_tag, self.environment_tag) in VALID_TAG_COMBINATIONS
