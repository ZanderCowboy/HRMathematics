# input
n_value = int(input("Enter Z_(n): "))
# n_value = 5
print(n_value)

out_str = ""
for i in range(n_value):
	old_i = i
	out_str += str(old_i) + " "
	calc = old_i + i

	if i == 0:
		isZero = True
	while isZero != True:
		if calc < n_value:
			out_str += str(calc) + " "
			old_i = calc

		elif calc >= n_value:
			calc = calc - n_value
			out_str += str(calc) + " "
			old_i = calc
			if calc == 0:
				isZero = True

		calc = old_i + i

	print("<{}> \t = {}".format(i, out_str))
	out_str = ""
	isZero = False
