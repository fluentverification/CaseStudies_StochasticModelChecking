// divide_by_two.pm
// Unipolar Stochastic Divide-By-2
// Based on Toggle Flip-Flop

dtmc

const double a;  // input value between 0 and 1
const int T;     // clock cycle count

//------------------
// Signal Sources
//------------------
module Source0
  inA : [0..1] init 0;

  [event] (true) -> a:(inA'=1) + (1-a):(inA'=0);
endmodule

//------------------------
// Toggle Flip-Flop (TFF)
//------------------------
module TFF
   B : [0..1] init 0;
  
   [event] (inA=0) -> (B' = B);
   [event] (inA=1) -> (B' = 1-B);
endmodule


//------------------
// AND gate
//------------------
module AND0

  Q : [0..1] init 0;
  
  [event] (inA=1 & B=1)  -> (Q'=1);
  [event] (inA=0 | B=0)  -> (Q'=0);  
endmodule
