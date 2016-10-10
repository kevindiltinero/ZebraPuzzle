from variables import *

class Constraint(object):

	constraint_set = []
	size = 0

	def __init__(self):
		Constraint.constraint_set.append(self)
		Constraint.size += 1

	def is_satisfied(self):
		pass

	def reduction(self):
		pass

	@staticmethod
	def printConstraints():
		for i in range(len(Constraint.constraint_set)):
			print Constraint.constraint_set[i].__str__()

class Constraint_equality_var_var(Constraint):

	def __init__(self, A, B):
		Constraint.__init__(self)
		self.A = A
		self.B = B

	def is_satisfied(self):
		for i in self.A.var_domain.domain:
			for j in self.B.var_domain.domain:
				if i == j:
					return True
		return False

	def reduction(self):
		if self.is_satisfied() == True:
			tempA = self.A.var_domain.domain
			tempB = self.B.var_domain.domain
			self.A.var_domain.destroyDomain()
			self.B.var_domain.destroyDomain()
			for i in tempA:
				for j in tempB:
					if i == j:
						self.A.setDomain(i)
						self.B.setDomain(j)
			if self.A.getDomain().is_empty() or self.B.getDomain().is_empty():
				return False
			else:
				return True

	def __str__(self):
		return "%s equals %s" % (self.A, self.B)


class Constraint_equality_var_cons(Constraints):

    def is_satisfied(self, variable1, cons):
        if cons in variable1.get_domain().possibilities:
            return True
        else:
            return False

    def reduction(self, variable1, cons):
        new_first = []
        new_first.append(cons)
        variable1.set_domain(new_first)


class Constraint_equality_var_plus_cons(Constraint):

	def __init__(self, A, B, C):
		Constraint.__init__(self)
		self.A = A
		self.B = B
		self.C = C

	def is_satisfied(self):

		for i in self.A.var_domain.domain:
			for j in self.B.var_domain.domain:
				if (i-1) in self.B.var_domain.domain or (i+1) in self.B.var_domain.domain:
					if (j-1) in self.A.var_domain.domain or (j+1) in self.A.var_domain.domain:
						return True
		return False

	def reduction(self):
		if self.is_satisfied() == True:
			if self.C == 2:
				tempA = self.A.var_domain.domain
				tempB = self.B.var_domain.domain
				self.A.var_domain.destroyDomain()
				self.B.var_domain.destroyDomain()
				for i in tempA:
					if (i-1) in tempB or (i+1) in tempB:
						self.A.setDomain(i)
				for j in tempB:
					if (j-1) in tempA or (i+1) in tempA:
						self.B.setDomain(j)
			elif self.C == 1:
				tempA = self.A.var_domain.domain
				tempB = self.B.var_domain.domain
				self.A.var_domain.destroyDomain()
				self.B.var_domain.destroyDomain()
				for i in tempA:
					if (i-1) in tempB:
						self.A.setDomain(i)
				for j in tempB:
					if (j+1) in tempA:
						self.B.setDomain(j)
			if self.A.getDomain().is_empty() or self.B.getDomain().is_empty():
				return False
			else:
				return True

	def __str__(self):
		return "%s next to %s" % (self.A, self.B)


class Constraint_difference_var_var(Constraint):

	def __init__(self, A, B):
		Constraint.__init__(self)
		self.A = A
		self.B = B

	def is_satisfied(self):
		if self.A.getDomain().is_reduced_to_1() or self.B.getDomain().is_reduced_to_1():
			for i in self.A.var_domain.domain:
				for j in self.B.var_domain.domain:
					if i == j:
						return True
			return False

	def reduction(self):
		if self.is_satisfied() == True:
			if self.A.getDomain().is_reduced_to_1():
				self.B.var_domain.domain.remove(self.A.getDomain().domain[0])
			elif self.B.getDomain().is_reduced_to_1():
				self.A.var_domain.domain.remove(self.B.getDomain().domain[0])
			if self.A.getDomain().is_empty() or self.B.getDomain().is_empty():
				return False
			else:
				return True

	def __str__(self):
		return "%s not equal %s" % (self.A, self.B)






from variables import *

class Constraint(object):

	constraint_set = []
	size = 0

	def __init__(self):
		Constraint.constraint_set.append(self)
		Constraint.size += 1

	def is_satisfied(self):
		pass

	def reduction(self):
		pass

	@staticmethod
	def printConstraints():
		for i in range(len(Constraint.constraint_set)):
			print Constraint.constraint_set[i].__str__()

class Constraint_equality_var_var(Constraint):

	def __init__(self, A, B):
		Constraint.__init__(self)
		self.A = A
		self.B = B

	def is_satisfied(self):
		for i in self.A.var_domain.domain:
			for j in self.B.var_domain.domain:
				if i == j:
					return True
		return False

	def reduction(self):
		if self.is_satisfied() == True:
			tempA = self.A.var_domain.domain
			tempB = self.B.var_domain.domain
			self.A.var_domain.destroyDomain()
			self.B.var_domain.destroyDomain()
			for i in tempA:
				for j in tempB:
					if i == j:
						self.A.setDomain(i)
						self.B.setDomain(j)
			if self.A.getDomain().is_empty() or self.B.getDomain().is_empty():
				return False
			else:
				return True

	def __str__(self):
		return "%s equals %s" % (self.A, self.B)

class Constraint_equality_var_cons(Constraint):

	def __init__(self, A, C):
		Constraint.__init__(self)
		self.A = A
		self.C = C

	def is_satisfied(self):
		if self.C in self.A.var_domain.domain:
			return True
		else:
			return False
		pass

	def reduction(self):
		if self.is_satisfied() == True:
			self.A.var_domain.destroyDomain()
			self.A.setDomain(self.C)
			if self.A.getDomain().is_empty():
				return False
			else:
				return True

	def __str__(self):
		return "%s equals house %s" % (self.A, self.C)

class Constraint_equality_var_plus_cons(Constraint):

	def __init__(self, A, B, C):
		Constraint.__init__(self)
		self.A = A
		self.B = B
		self.C = C

	def is_satisfied(self):
		for i in self.A.var_domain.domain:
			for j in self.B.var_domain.domain:
				if (i-1) in self.B.var_domain.domain or (i+1) in self.B.var_domain.domain:
					if (j-1) in self.A.var_domain.domain or (j+1) in self.A.var_domain.domain:
						return True
		return False

	def reduction(self):
		if self.is_satisfied() == True:
			if self.C == 2:
				tempA = self.A.var_domain.domain
				tempB = self.B.var_domain.domain
				self.A.var_domain.destroyDomain()
				self.B.var_domain.destroyDomain()
				for i in tempA:
					if (i-1) in tempB or (i+1) in tempB:
						self.A.setDomain(i)
				for j in tempB:
					if (j-1) in tempA or (i+1) in tempA:
						self.B.setDomain(j)
			elif self.C == 1:
				tempA = self.A.var_domain.domain
				tempB = self.B.var_domain.domain
				self.A.var_domain.destroyDomain()
				self.B.var_domain.destroyDomain()
				for i in tempA:
					if (i-1) in tempB:
						self.A.setDomain(i)
				for j in tempB:
					if (j+1) in tempA:
						self.B.setDomain(j)
			if self.A.getDomain().is_empty() or self.B.getDomain().is_empty():
				return False
			else:
				return True

	def __str__(self):
		return "%s next to %s" % (self.A, self.B)

class Constraint_difference_var_var(Constraint):

	def __init__(self, A, B):
		Constraint.__init__(self)
		self.A = A
		self.B = B

	def is_satisfied(self):
		if self.A.getDomain().is_reduced_to_1() or self.B.getDomain().is_reduced_to_1():
			for i in self.A.var_domain.domain:
				for j in self.B.var_domain.domain:
					if i == j:
						return True
			return False

	def reduction(self):
		if self.is_satisfied() == True:
			if self.A.getDomain().is_reduced_to_1():
				self.B.var_domain.domain.remove(self.A.getDomain().domain[0])
			elif self.B.getDomain().is_reduced_to_1():
				self.A.var_domain.domain.remove(self.B.getDomain().domain[0])
			if self.A.getDomain().is_empty() or self.B.getDomain().is_empty():
				return False
			else:
				return True

	def __str__(self):
		return "%s not equal %s" % (self.A, self.B)