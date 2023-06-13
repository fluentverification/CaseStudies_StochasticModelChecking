// rfb.pm
// Restorative Feedback model
// A type of Triple Modular Redundancy (TMR)
ctmc

const double Rc      = 10;       // signal transition rate of logic gates
const double Rn      = 2;        // noise process rate
const double epsilon = 1;        // transient upset rate
const double alpha   = .1;       // state upset rate
const double T;
const int    i1;
const int    i2;
const int    i3;


// Noise sources
module noise1
  n1: int init 0;

  [] (true) -> Rn:(n1'=1)+(Rn/2):(n1'=2)+(Rn/4):(n1'=3)+(Rn/8):(n1'=4);
endmodule
module noise2 = noise1 [ n1=n2 ] endmodule
module noise3 = noise1 [ n1=n3 ] endmodule


// Signal Source
module source1 
  x1 : int init i1;

  []  (x1 > 0) -> (epsilon/2):(x1'=x1+n1) + (epsilon/2):(x1'=x1-n1) + Rc:(x1'=x1-1);
  []  (x1 = 0) -> (epsilon/2):(x1'=x1+n1) + (epsilon/2):(x1'=x1-n1);
  []  (x1 < 0) -> (epsilon/2):(x1'=x1+n1) + (epsilon/2):(x1'=x1-n1) + Rc:(x1'=x1+1);
endmodule

module source2 = source1 [ x1=x2, i1=i2, n1=n2 ] endmodule
module source3 = source1 [ x1=x3, i1=i3, n1=n3 ] endmodule


// Modified Muller C-element
module Cem1
  y1 : int init i3;

  [] (x1 = y3)  -> (Rc):(y1' = y3);
  [] (x1 != y3) -> (alpha/2):(y1'=y1+1)+(alpha/2):(y1'=y1-1);
endmodule

module Cem2 = Cem1 [ x1=x2, y1=y2, y3=y1, i3 = i1 ] endmodule
module Cem3 = Cem1 [ x1=x3, y1=y3, y3=y2, i3 = i2 ] endmodule

