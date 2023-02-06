// rfb.pm
// Restorative Feedback model
// A type of Triple Modular Redundancy (TMR)
ctmc

const double Rc      =100;     // signal transition rate of logic gates
const double epsilon =1;       // transient upset rate
const double alpha   =0.01;    // state upset rate
const double T;
const int    initialErrors;

// Signal Source
module source1 
  x1 : [0..1];

  []  (true) -> epsilon:(x1'=1) + Rc:(x1'=0);
endmodule

module source2 = source1 [x1=x2] endmodule
module source3 = source1 [x1=x3] endmodule


// Modified Muller C-element
module Cem1
  y1 : [0..1];

  [] (x1 = y3)  -> (Rc):(y1' = y3);
  [] (x1 != y3) -> (alpha):(y1'=1-y1);
endmodule

module Cem2 = Cem1 [y1=y2, x1=x2, y3=y1] endmodule
module Cem3 = Cem1 [y1=y3, x1=x3, y3=y2] endmodule

 
init ((x1+x2+x3=initialErrors) & ((y1=x3)&(y2=x1)&(y3=x2))) endinit
