# “All vanity plates must start with at least two letters.”
# “… vanity plates may contain a maximum of 6 characters (letters or numbers) and a minimum of 2 characters.”
# “Numbers cannot be used in the middle of a plate; they must come at the end. For example, AAA222 would be an acceptable … 
# vanity plate; AAA22A would not be acceptable. The first number used cannot be a ‘0’.”
# “No periods, spaces, or punctuation marks are allowed.”

def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    first_two_letters(s)
    length_two_to_six(s)
    ends_with_number(s)
    def is_alnum(s):
   
    
# main()

#     #check if first two are letters
def first_two_letters(s):
    if s[:2].isalpha():
        return True

#     # check len() 2 < string < 6
    def length_two_to_six(s):
        if 2 < len(s) < 6:
            return True

#     # number at the end
def ends_with_number(s):
    if s[:-1].isdecimal():
        return True

#no space, punctuation etc 
def is_alnum(s):
    s.isalnum()


plate = input("Plate: ")


# # first number not a 0

# #number not in middle
# for i in range(0, (len(plate)- 1)):
#     if plate[i].isdecimal() and plate[i+1].isalpha():
#         return True

