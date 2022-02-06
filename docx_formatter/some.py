class EndIndex:
	def __init__(self, desired_num):
		self.desired_num = desired_num

	def bisection(self, num, old=0) -> int:
		mid_index = int(num / 2)

		if mid_index == self.desired_num - 1 or mid_index == self.desired_num + 1:
			return num / 2

		if mid_index > self.desired_num:
			return self.bisection((mid_index - (mid_index - old)/2) * 2, old)
		else:
			return self.bisection((mid_index + (mid_index - old)/2) * 2, mid_index)

i = EndIndex(85)
print(i.bisection(100))