### Genetic Circuit0x8E

This genetic circuit model implements a more complex circuit first proposed in the Cello paper. The circuit has three input arguments IPTG, aTc, and Ara and one output argument YFP. 

This circuit shows glitching behavior, which is analyzed in these case studies. There are two types of glitches. In one type, the output should remain in a low state during an input transition (found in Glitch-Zero). In the other type, the output should remain at a high state (found in Glitch-One) during an input transition. The folders include a bounded and unbounded model for each input transition that causes glitching behavior. The folders also include the corresponding properties file (csl-file). In addition, each model shows in line 4 of the code the probability that is expected to be calculated by STAMINA. 

