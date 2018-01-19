class polynom:
    def __init__(self, coeff):
        # remove leading 0's
        while(coeff[0] == 0):
            coeff.remove(0)
        self.poly = coeff

    # overloaded add
    def __add__(self, other):
        result = []

        #reverse the lists
        self_reversed = list(reversed(self.poly))
        other_reversed = list(reversed(other.poly))

        # concatenate 0s to front of the shorter list
        while(len(self_reversed) < len(other_reversed)):
            self_reversed.append(0)
        while(len(self_reversed) > len(other_reversed)):
            other_reversed.append(0)

        # both lists are same length; iterate each both list in parallel and add each element together
        for (x, y) in zip(self_reversed, other_reversed):
            result.append(x + y)

        # return the result reversed so polynomial degrees are in decreasing order
        return polynom(list(reversed(result)))

    # overloaded subtract
    def __sub__(self, other):
        result = []

        #reverse the lists
        self_reversed = list(reversed(self.poly))
        other_reversed = list(reversed(other.poly))

        # concatenate 0s to front of the shorter list
        while(len(self_reversed) < len(other_reversed)):
            self_reversed.append(0)
        while(len(self_reversed) > len(other_reversed)):
            other_reversed.append(0)

        # both lists are same length; iterate each both list in parallel and subtract each element
        for (x, y) in zip(self_reversed, other_reversed):
            result.append(x - y)

        # return the result reversed so polynomial degrees are in decreasing order
        return polynom(list(reversed(result)))

    # overloaded multiplication
    def __mul__(self, other):
        # create reversed copies of the coefficient list
        self_reversed = list(reversed(self.poly))
        other_reversed = list(reversed(other.poly))

        # initialize a list of results with proper number of elements
        result = [0] * (len(self.poly) + len(other.poly) - 1)

        # iterate through both lists and calculate the results in proper index
        for i in range(len(self_reversed)):
            for j in range(len(other_reversed)):
                result[i + j] += (self_reversed[i] * other_reversed[j])

        return polynom(list(reversed(result)))

    # derivative 
    def drv(self):
        result = list(reversed(self.poly))
        for i in range(len(result)):
            result[i] *= i

        del result[0]   # remove the constant b/c polynomial degree decreases by 1 when taking derivative
        result = list(reversed(result))
        return polynom(result)

    # integral
    def intg(self, a, b):
        #check if bounds are correct
        if(a > b):
            print("Error: lower bound is greater upper bound.")
            exit()

        result = list(reversed(self.poly))
        lower = 0.0
        upper = 0.0

        for i in range(len(result)):
            lower += float(((a ** (i + 1)) * result[i])) / (i + 1)
            upper += float(((b ** (i + 1)) * result[i])) / (i + 1)

        return upper - lower


p1 = polynom([2,3,0,1])
p2 = polynom([1,1,2])
p3 = polynom([2,1])
p4 = polynom([1,1])
print p2.poly
print "Poly 1: " + str(p1.poly)
print "Poly 2: " + str(p2.poly)
p = p1 + p2
print "P1 + P2: " + str(p.poly)
p = p1 - p2
print "P1 - P2: " + str(p.poly)
p = p1 * p2
print "P1 * P2: " + str(p.poly)
p = p1 * p3
print "P1 * P3: " + str(p.poly)
p = p3 * p4
print "P3 * P4: " + str(p.poly)
p = p.drv()
print "Derivative of P: " + str(p.poly)
p = p.intg(1, 5)
print "Integral of P from 1 to 5: " + str(p)
print p2.poly
