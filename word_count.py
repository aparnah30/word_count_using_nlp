def word_count(text, min_freq=1, blacklist=[]):
    word_count = {}
    total_words = 0
    lines = text.split('\n')
    for line in lines:
        words = line.split()
        for word in words:
            word = word.strip('.,!?;:"()[]{}')
            word = word.lower()
            if word not in blacklist:  
                word_count[word] = word_count.get(word, 0) + 1  
                total_words += 1
    word_count = {word: count for word, count in word_count.items() if count >= min_freq}
    print("Total words: ", total_words)
    return word_count

def print_word_count(word_count):
    print( "word","\t\t", "count")
    for word, count in word_count.items():
        print( word,"\t\t", count)

def main():
    text = """ Deutsche Boerse boosts dividend

            Deutsche Boerse, the German stock exchange that is trying to buy its London rival, has said it will boost its
            2004 dividend payment by 27%.

            Analysts said that the move is aimed at winning over investors opposed to its bid for the London Stock Exchange.
            Critics of the takeover have complained that the money could be better used by returning cash to shareholders.
            Deutsche Boerse also said profit in the three months to 31 December was 120.7m euros.
            Sales climbed to 364.4m euros, lifting revenue for the year to a record 1.45bn euros.

            Frankfurt-based Deutsche Boerse has offered £1.3bn ($2.48bn; 1.88bn euros) for the London Stock Exchange.
            Rival pan-European bourse Euronext is working also on a bid. Late on Monday, Deutsche Boerse said it would lift
            its 2004 dividend payment to 70 euro cents (£0.48; $0.98) from 55 euro cents a year earlier.
            "There is a whiff of a sweetener in there," Anais Faraj, an analyst at Nomura told the BBC's World
            Business Report. "Most of the disgruntled shareholders of Deutsche Boerse are complaining that the money that is
            being used for the bid could be better placed in their hands, paid out in dividends," Mr Faraj continued.
            Deutsche Boerse is "trying to buy them off in a sense", he said.

            """
    blacklist = ['the', 'and', 'be', 'in', 'a','of','to','is']

    while True:
        print("\nMenu:")
        print("1. Get all words and their frequencies")
        print("2. Get words with frequency greater than a particular frequency")
        print("3. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            print_word_count(word_count(text, blacklist=blacklist))
        elif choice == '2':
            min_freq = int(input("Enter the minimum frequency: "))
            print_word_count(word_count(text, min_freq=min_freq, blacklist=blacklist))
        elif choice == '3':
            print("Exit")
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()
