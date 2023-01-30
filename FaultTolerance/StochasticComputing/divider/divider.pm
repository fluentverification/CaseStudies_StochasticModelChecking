// Unipolar stochastic divider circuit  
dtmc

const double a;
const double b;
const int T;

// Saturation level for up-down counter
const int MAXCOUNT=63;

//------------------
// Signal Sources
//------------------
module Source0
  inA : [0..1] init 0;

  [event] (inA=0 | inA=1) -> a:(inA'=1) + (1-a):(inA'=0);
endmodule

// Second signal source:
module Source1 = Source0 [ inA=inB, a=b ] endmodule


// AND gate
module AND0
  QB : [0..1] init 0;

  [event] (inB=1)&(Q=1)  ->  (QB' = 1);
  [event] !(inB=1 & Q=1) ->  (QB' = 0);
endmodule


// Up-Down Counter
module UDC0
   c0: [-MAXCOUNT..MAXCOUNT] init 0;

   [event] (c0 > -MAXCOUNT) & (c0 < MAXCOUNT) -> 1:(c0' = c0 + inA - QB);
   [event] (c0 = -MAXCOUNT) -> 1:(c0' = c0 + inA);
   [event] (c0 = MAXCOUNT)  -> 1:(c0' = c0 - QB);  
endmodule

// Output and Feedback
formula q=(c0+MAXCOUNT+1)/(2*(MAXCOUNT+1));
module FB0
   Q: [0..1] init 0;

   [event]  (c0 >= -MAXCOUNT) & (c0 <= MAXCOUNT) ->  q:(Q' = 1) + (1-q):(Q'=0); 
endmodule

