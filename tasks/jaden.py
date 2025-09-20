def to_jaden_case(text):
    
    return " ".join (words.capitalize() for words in text.split())

string = "All the rules in this world were made by someone no smarter than you. So make your own."

print (to_jaden_case(string))
