#!/usr/bin/env python

class Fraction:
    def __init__(self,top,bottom):
        self.num = top
        self.den = bottom
    def __str__(self):
        return str(self.num)+"/"+str(self.den)
    def __add__(self, other):
        added_num = self.num*other.den + self.den*other.num
        added_den = self.den*other.den
        mygcd = gcd(added_num,added_den)
        return Fraction(added_num//mygcd,added_den//mygcd)
    def __mul__(self, other):
        firstnum = self.num*other.num
        secondnum = self.den*other.den
        mygcd = gcd(firstnum,secondnum)
        return Fraction(firstnum//mygcd,secondnum//mygcd)
    def __truediv__(self, other):
        firstnum = self.den*other.num
        secondnum = self.num*other.den
        mygcd = gcd(firstnum,secondnum)
        return Fraction(firstnum//mygcd,secondnum//mygcd)
    def __sub__(self, other):
        firstnum = self.num*other.den - self.den*other.num
        secondnum= self.den*other.den
        mygcd = gcd(firstnum,secondnum)
        return Fraction(firstnum//mygcd,secondnum//mygcd)
    def __gt__(self, other):
        firstnum = self.den*other.num
        secondnum = self.num*other.den
        return firstnum > secondnum
    def __lt__(self, other):
        firstnum = self.den*other.num
        secondnum = self.num*other.den
        return firstnum < secondnum
    def __eq__(self, other):
        firstnum = self.den*other.num
        secondnum = self.num*other.den
        return firstnum == secondnum

def gcd(m,n):
    while m%n != 0:
        oldm = m
        oldn = n

        m = oldn
        n = oldm%oldn
    return n

frac3 = 'poop'
frac = Fraction(10,5)
frac1 = Fraction(1,5)

print('The first fraction: %s' % (frac))
print('The second fraction:', frac1)
print('The subtraction ', frac-frac1)
print('The addition ', frac+frac1)
print('The division ', frac/frac1)
print('The equality ', frac==frac1)
print('The multiplication ', frac*frac1)
