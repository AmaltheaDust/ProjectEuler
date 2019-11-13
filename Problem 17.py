"""
If the numbers 1 to 5 are written out in words: one, two, three, four, five, then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.

If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be used?

"""

firstnine_single_d = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
exception_11_19 = ['eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen']

firstnine_double_d = ['ten', 'twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety']
firstnine_triple_d = ['hundred']
and_holder = ['and']


for belowten in range(9):
    print(firstnine_single_d[belowten])
