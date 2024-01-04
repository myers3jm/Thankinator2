class Event:
    def __init__(self, title: str, location: str, timeframe: str):
        self.title = title
        self.location = location
        self.timeframe = timeframe
    
    def getTitle(self) -> str:
        return self.title
    
    def getLocation(self) -> str:
        return self.location
    
    def getTimeframe(self) -> str:
        return self.timeframe