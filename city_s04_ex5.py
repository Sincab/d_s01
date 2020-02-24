def main():
    entered_word_1 = input('enter first word:')
    entered_word_2 = input('enter second word:')

    print('They are ', isAnagram(entered_word_1, entered_word_2))



def isAnagram(entered_word_1, entered_word_2):
    if sorting_thins(entered_word_1) == sorting_thins(entered_word_2):
        return 'Anagram'
    return 'NOT Angram'

def sorting_thins(string):
    return sorted([s for s in string])

main()
