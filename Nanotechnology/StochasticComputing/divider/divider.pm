// Unipolar stochastic divider circuit
  
dtmc

const double epsilon0;
const double epsilon1;

//------------------
// Signal Sources
//------------------
module Source0
  inA : [0..1] init 0;

  [event] (inA=0 | inA=1) -> epsilon0:(inA'=1) + (1-epsilon0):(inA'=0);
endmodule

// Second signal source:
module Source1 = Source0 [ inA=inB, epsilon0=epsilon1 ] endmodule



// AND gate
module AND0

  AB : [0..1] init 0;

  [event] (inB=1)&(Q=1)  ->  (AB' = 1);
  [event] !(inB=1 & Q=1) ->  (AB' = 0);

endmodule


// Up-Down Counter
module UDC0

   c0: [-63..63] init 0;

   [event] (c0 > -63) & (c0 < 63) -> 1:(c0' = c0 + inA - AB);
   [event] (c0 = -63) -> 1:(c0' = c0 + inA);
   [event] (c0 = 63)  -> 1:(c0' = c0 - AB);
  
endmodule

// Feedback
module FB0
   Q: [0..1] init 0;

   [event]  (c0 >= -63) & (c0 <= 63) ->  ((c0+64)/128):(Q' = 1) + (1-(c0+64)/128):(Q'=0); 
endmodule

