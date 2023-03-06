# Verify if the parentheses match
# You will only see '(' or ')'
# Once you see a ')' in the string you will NOT get a '('
def is_match_parentheses_simple(s: str):
    count = 0
    for letter in s:
        if letter == ')':
            if count <= 0:
                return False
            else:
                count -= 1
        elif letter == '(':
            count += 1
        else:
            return False
    if count == 0:
        return True
    else:
        return False



