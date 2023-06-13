// tmr.pm
// Triple Modular Reduncancy model
// using majority logic
ctmc

const double Rc=100;          // signal transition rate of logic gates
const double epsilon=1;       // transient upset rate
const double T;
const int    initialErrors;

// Signal Source
module source1 
  x1 : [0..1];

  []  (true) -> epsilon:(x1'=1) + Rc:(x1'=0);
endmodule

module source2 = source1 [x1=x2] endmodule
module source3 = source1 [x1=x3] endmodule


// Majority Gates
module Maj1
  y1 : [0..1];

  [] (x1 + x2 + x3 > 1)  -> (Rc):(y1' = 1) + epsilon:(y1'=0);
  [] (x1 + x2 + x3 < 2)  -> (Rc):(y1' = 0) + epsilon:(y1'=1);

endmodule

module Maj2 = Maj1 [y1=y2] endmodule
module Maj3 = Maj1 [y1=y3] endmodule

 
init (x1+x2+x3=initialErrors) endinit
