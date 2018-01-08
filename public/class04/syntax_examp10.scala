/*
~/ml4/public/class04/syntax_examp10.scala

This script should show some example syntax for Scala.
*/

"hello class!"
    
// val should make immutable variable:
val int_i = 1

// var should make mutable variable:
var ur_i = 2
ur_i = 22

// I should define func which takes 1 arg of type Int and returns an Int:
def myfnc(m_i: Int): Int = m_i + 1

// I should call it:
myfnc(7)

// I should define func which does not declare return type:
def urfnc() = myfnc(3)

// I should call it:
urfnc()

// I should call it with no parens:
urfnc

// I should declare an anonymous func:
() => "I am anonymous"
// I dont know how to call it yet, but will later.

// I should declare an anonymous func:
(param: Int) => "I take a param which should be an Int."
// I dont know how to call it yet, but will later.

// I should assign anonymous func to a val:
val theirfnc = (aparam: Int) => "I am non-anonymous!"
theirfnc(99)

// I can use brakets:
def somefnc(myparam: Int): Int = {
  myparam * 2
}
somefnc(4)

// I should declare anon func with brackets:
{
  i_param: Int =>
    println("I am anonymous, in brackets")
    i_param + 9
}

// Another way I should declare anon func with brackets:
{
  (j_param: Int) =>
    println("I am anonymous, in brackets")
    j_param + 5
}


// I should create partially applied function using underscore:
def addem(p1: Int, p2: Int): Int = p1 + p2

val nothrfunc = addem(3, _: Int)
nothrfunc(4) // should return 7

/* I should demo curried functions.
This is an idea which allows me to transform single function
with multiple args
into multiple funcs
with one arg.
*/

def mult2(m1: Int)(m2: Int): Int = m1 * m2
mult2(7)(3) // 2 args
val two_infront = mult2(2)(_: Int)
two_infront(6) // 1 arg
val three_inback = mult2(_: Int)(3)
three_inback(5) // 1 arg

// I should demo how to use anon func via a call to map:
List(0,1,2,3,4).map {param => param*2}

/* I should demo how to use anon func via a call to map.
Sometimes I add parens to help me see param: */
List(0,1,2,3,5).map {(param) => param*3}

// I should demo variable-length args:
def varfnc(params: Int*) = params.map {(param) => param*2}
varfnc(0,3,2,5)

// I should demo variable-types. I should use T by convention:
def vart_fnc[T](somenum: T) = println(s"hello ${somenum}")
vart_fnc(3)
vart_fnc(-3.9)
vart_fnc("Dan")
vart_fnc(9F)
vart_fnc(9D)
vart_fnc(0xF)
vart_fnc(Integer.parseInt("0101", 2))
