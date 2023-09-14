import re


# Returns True If Given String Begins And Ends With 'start' And 'end' Substrings,
# Otherwise Returns False.
def begin_and_ends_with(txt, start, end) -> bool:
    if re.search(f"^{start}.*{end}.$", txt):
        return True
    else:
        return False


# Returns True If Given String Begins With 'start',
# Otherwise Return False
def begins_with(txt, start):
    if re.findall("\AThe", txt):
        return True
    else:
        return False


# Returns List Of All Lower Case Letters
def get_all_lower_case(txt):
    return re.findall("[a-z]", txt)


# Returns List Of Digits
def get_all_digits(txt):
    return re.findall("\d", txt)


# Returns Phone Number If Valid Format Available
def get_valid_phone_number(txt):
    phone_number_regex = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')
    phone_number = phone_number_regex.search(txt)

    if phone_number:
        print(f"\tPhone Number : {phone_number.group(0)}")
        print(f"\tArea Code    : {phone_number.group(1)}")
        print(f"\tLast 6 Nos.  : {phone_number.group(2)}")
        print(f"\tGrouped List : {phone_number.groups()}")
        return phone_number.group()
    else:
        return "000-000-0000"


if __name__ == '__main__':
    # Look For String That Begins With 'The' And Ends With 'India'
    txt1 = "The rain in India."
    if begin_and_ends_with(txt1, 'The', 'India'):
        print("Match Found!")
    else:
        print("No Match Found!")

    lower_case = get_all_lower_case(txt1)
    print(lower_case)

    txt2 = "The temperature today is 35 degree Celsius, which is equivalent to 95 Fahrenheit."
    digits = get_all_digits(txt2)
    print(digits)

    # Search For Sequence That Starts With "He" Followed By Exactly 2 (Any) Characters And An "o".
    txt3 = "Hello World!!"
    x = re.findall("He.{2}o", txt3)
    print(x)

    # Look For String That Begins With 'The'
    txt4 = "The Game Of Thrones."
    if begins_with(txt4, 'The'):
        print("Match Found At The Beginning!")
    else:
        print("No Match Found!")

    # Check If "ain" Is Present At The Beginning Of WORD
    x = re.findall(r"\bain", txt1)
    if x:
        print("Found A Word That Begins With 'ain.'!")
    else:
        print("No Word Beginning With 'ain' Found!")

    # Check If "ain" Is Present At The Ending Of WORD:
    x = re.findall(r"ain\b", txt1)
    if x:
        print("Found A Word That Ends With 'ain.'!")
    else:
        print("No Word Ending With 'ain' Found!")

    # Get If Valid Phone Number Available
    txt5 = "My cell number is 123-456-7890."
    txt6 = "My cell number is ABC-456-7890."
    print(f"Found {get_valid_phone_number(txt5)} In Input String.")
    print(f"Found {get_valid_phone_number(txt6)} In Input String.")

