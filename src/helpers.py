from discord import Embed

colors = {
        "error": 0xff0000,
        "ok": 0x0761c2
}

class error:
    def __init__(self, name, description):
        self.title = name
        self.description = description
    def embed(self):
        print("making embed..")
        return Embed(
                title="Error",
                description = f"**{self.title}**\n{self.description}",
                color=colors["error"])

class ArgumentError(error):
    def __init__(self, argc, min_args):
        self.argc = argc
        self.min_args = min_args
    def as_embed(self):
        if self.argc <= min_args:
            return error.embed(self, "ArgumentError", f"Please enter at least {self.argc} argument")
        else: 
            return error.embed(self, "ArgumentError", f"Please enter at least {self.argc} arguments")

class UnknownCommandError(error):
    def __init__(self, command):
        super().__init__("Unknown Command", command)


