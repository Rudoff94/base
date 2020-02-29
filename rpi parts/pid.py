class PID:
	def __init__(self, kp, kd, ki, min, max):
		self.kp = kp
		self.kd = kd
		self.ki = ki

		self.min = min
		self.max = max

		self.last_err = None 
		self.sum = 0
'''
P = Kp * error
D = Kd * (cur_err - last_err)
I = Ki * sum

Sum for Ki = sum + err

max >= result <= min
'''	

	def reset(self):
		self.sum = 0
		self.last_err = None

	def calculate(self, error):

		P = self.kp * error	
		if self.last_err is not None:
			D = self.kd * (error = self.last_err)
		else: 
			D = 0
		I = self.sum
		self.sum += self.ki * error
		result = D + P + I
		self.last_err = error

		if result > self.max:
			result = self.max
		elif result < self.min:
			result = self.min
			
		return result 	