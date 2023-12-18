class Event:
    def __init__(self, title: str, highlights: list, timeframe: str):
        self.title = title
        self.highlights = highlights
        self.timeframe = timeframe
    
    def getTitle(self) -> str:
        return self.title
    
    def getHighlights(self) -> str:
        return self.highlights
    
    def getTimeframe(self) -> str:
        return self.timeframe