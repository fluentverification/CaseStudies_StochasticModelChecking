// Unipolar stochastic divider circuit  
dtmc

const double a;
const double b;
const int    T;

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
   c0: int init 0;

   [event] (true) -> 1:(c0' = c0 + inA - QB);
endmodule

// Clock Timer
module clockTimer
   N: int init 1;
   M: int init 1;

   [event] (true) -> 1:(N'=N+1)&(M'=1+round(log(N,2)));
endmodule


// Output and Feedback
formula q=(c0+M+1)/(2*(M+1));
module FB0
   Q: [0..1] init 0;

   [event]  (c0 >= -M) & (c0 <= M) ->  q:(Q' = 1) + (1-q):(Q'=0); 

endmodule

