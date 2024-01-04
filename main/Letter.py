import Event

class Letter:
    def __init__(self, event: Event, location: str, person: str, address: str, attended: str, gift: str, sentiment: str, signature: str):
        self.event = event
        self.person = person
        self.address = address
        self.attended = True if attended.upper() == 'YES' else False
        self.gift = gift
        self.sentiment = sentiment
        self.signature = signature

    def __repr__(self) -> str:
        ret = f'<h1>Dear {self.person},</h1>'
        ret += f'<p>I wanted to say thank you for {"coming to my" if self.attended else "celebrating my"} {self.event.title.lower()} {"at " if self.attended and self.event.location != "" else ""}{self.event.location if self.attended else ""} {self.event.timeframe}.'
        ret += f' It meant a lot to {"see" if self.attended else "hear from"} you.'
        ret += f' I also wanted to thank you for your generosity. I appreciate the {self.gift.lower()} very much, and I know I will get good use out of your gift!'
        ret += f' I can\'t wait to {"see" if self.attended else "hear from"} you again!</p>'
        ret += f'<h3>\n\n{self.sentiment.title()},\n {self.signature}</h3>'
        return ret