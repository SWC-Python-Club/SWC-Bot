from discord import Embed

class error:
    def embed(self, name, description):
        return Embed(
                title="Error",
                description = f"**{name}**\n{description}"
                )

class ArgumentError(error):
    def __init__(self, argc):
        self.argc = argc
    def as_embed(self):
        if self.argc <= 1:
            return super().embed("ArgumentError", f"Please enter at least {self.argc} argument")
        else: 
            return super().embed("ArgumentError", f"Please enter at least {self.argc} arguments")
