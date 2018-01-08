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
