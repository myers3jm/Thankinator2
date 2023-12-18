import pandas as pd
import Event
from Event import Event
import Letter
from Letter import Letter

def main():
    df = pd.read_excel("main/book.xlsx")

    event = Event('birthday party', ['bouncy house', 'clown', 'petting zoo'], 'last week')
    
    for entry in df.values:
        letter = Letter(event, entry[0], entry[1], entry[2], entry[3], 'sincerely', 'J. Matthew Myers')
        print(letter)
        print('################################')

main()