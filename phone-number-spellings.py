# Write a function that can take a phone number and return all
# of the combinations of ways that phone number could be
# spelled. That could include replacing *any* of the digits in
# the number, or replacing a variable number of digits from
# the *end* of the number (but not a mixture, e.g. '1800CARPETS'
# is valid but '1800CAR7ETS' is not).

letters = {
    '2': 'ABC',
    '3': 'DEF',
    '4': 'GHI',
    '5': 'JKL',
    '6': 'MNO',
    '7': 'PQRS',
    '8': 'TUV',
    '9': 'WXYZ'
}

def addPerms(phone, perms, position):
    if position < 0:
        return

    digit = phone[position]
    if digit in letters:
        for letter in letters[digit]:
            new_phone = phone[:position] + letter + phone[position+1:]
            perms.append(new_phone)
            addPerms(new_phone, perms, position-1)


def spell_number(phone):
    perms = [phone]

    addPerms(phone, perms, len(phone)-1)

    return perms

def test_spell_number(input, expected_length):
    result = spell_number(input)
    num_results = len(result)
    if (num_results > 20):
        result = '%s ... (truncated)' % result[:20]
    print('input: %s\noutput length: %s\noutput: %s' % (input, result, num_results))
    if num_results != expected_length:
        print('FAILED. Expected output lenght of %s' % expected_length)
    else:
        print('PASSED')



test_spell_number('2222', 121)          # 1 + 3^1 + 3^2 + 3^3 + 3^4 = 121
test_spell_number('0000000000', 1)
test_spell_number('99999999991', 1)
test_spell_number('18002277387', 7685)     # 1 + 4^1 + 4*3 + 4*3^2 + 4^2*3^2 + 4^3*3^2 + 4^3*3^3 + 4^3*3^4 = 7685
