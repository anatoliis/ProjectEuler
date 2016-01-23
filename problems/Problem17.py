#!/usr/bin/env pypy

numbers = { 1:'one',2:'two',3:'three',4:'four',5:'five',6:'six',7:'seven',8:'eight',9:'nine',10:'ten',
			11:'eleven',12:'twelve',13:'thirteen',14:'fourteen',15:'fifteen',16:'sixteen',17:'seventeen',
			18:'eighteen',19:'nineteen',20:'twenty',30:'thirty',40:'forty',50:'fifty',60:'sixty',
			70:'seventy',80:'eighty',90:'ninety',100:'hundred',1000:'thousand'}

def number_to_spell(n):
	if n < 21: return numbers[n]
	thousands, hundreds, tens, left = [0] * (4 - len(str(n))) + map(int, str(n))
	if tens == 1:
		left += 10
		tens = 0
	result = ''
	if thousands: result += '%s %s' % (numbers[thousands], numbers[1000])
	if hundreds: result += '%s %s' % (numbers[hundreds], numbers[100]) + ' and ' * bool(tens or left)
	if tens: result += numbers[tens*10]
	if left: result += '-' * bool(tens) + numbers[left]
	return result

total_length = 0
for number in xrange(1,1001):
	spell = number_to_spell(number)
	length = len(spell.replace('-', '').replace(' ', ''))
	total_length += length

print 'result: %s' % total_length