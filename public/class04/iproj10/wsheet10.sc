1 + 2
1 > 4

// val makes one immutable
val one = 1

// var makes x is mutable
var x = 1 + one
x = 3

// define func which takes 1 arg of type Int and returns an Int
def addOne(m: Int): Int = m + 1

// define a function which does not declare return type:
def addtwo() = addOne(2)
addtwo()
// paren is optional:
addtwo



// anon functions:
(m: Int) => m + 1
(m: Int, n: Int) => m + n

// assign to a val
val myf2 = (uu: Double) => uu + 9.9
myf2(8.2)


// I can use brakets

def myf(mm: Int): Int = {
  println("hey!")
  // notice lack of return keyword:
  mm * 2
}
myf(6)

// anon func with brackets:
{
  i: Int =>
    println("i am anonymous")
    i + 9
}

// underscore helps me create partially applied functions:

def adder(m: Int, n: Int): Int = m + n

val nothrfunc = adder(2, _: Int)
nothrfunc(33)

// curried functions
/*idea which allows me to transform single function
with multiple args
into multiple funcs
with one arg.
*/

def mult2(m1: Int)(m2: Int): Int = m1 * m2
mult2(7)(3)


