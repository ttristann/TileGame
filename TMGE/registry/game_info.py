class GameInfo:
    def __init__(self, name: str, description: str, thumbnail=None):
        self.name = name
        self.description = description
        self.thumbnail = thumbnail
    
    def get_name(self) -> str:
        return self.name
    
    def get_description(self) -> str:
        return self.description
    
    def get_thumbnail(self):
        return self.thumbnail