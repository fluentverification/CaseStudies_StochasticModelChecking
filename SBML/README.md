# SBML Case Studies

Case studies of genetic designs represented in the _Systems Biology Markup Language_ (SBML) are stored in this directory. SBML encodes mathmatical models of biological processes.

## Naming Convention

* 10_10: Production and degradation of molecules in steps of 10

* RBA: Reaction-based abstraction (remove irrelevant or rapid reactions)

* G0: Static zero glitch

* G1: Static one glitch

## Genetic Circuits

### Circuit0x8E

This circuit is part of the genetic circuits designed by the software tool Cello [1]. The circuit has three input arguments IPTG, aTc, and Ara and one output argument YFP.

![Figure1](https://github.com/fluentverification/CaseStudies_StochasticModelChecking/blob/refactor/Figures/Original.png "Figure 1")

In the laboratory, circuit 0x8E showed an unexpected, glitching behavior. Further analysis resulted in two more designs of the circuit as well as the analysis of its glitching behavior [2].

![Figure2](https://github.com/fluentverification/CaseStudies_StochasticModelChecking/blob/refactor/Figures/LogicHazardFree.png "Figure 2")

![Figure3](https://github.com/fluentverification/CaseStudies_StochasticModelChecking/blob/refactor/Figures/TwoInverter.png "Figure 3")

There are two types of glitches. In one type, the output should remain in a low state during an input transition (Zero Glitch). In the other type, the output should remain at a high state (One Glitch) during an input transition. More information can be found in [1-2].

### Muller C-element

This genetic circuit implements a state-holding gate called Muller C-element. If both inputs are high, its output goes high. If both inputs are low, the output is low. If the inputs are mixed, it retains its previous state. The three designs are the Majority, Speed_Independent, and Toggle Switch design [3].

![Figure4](https://github.com/fluentverification/CaseStudies_StochasticModelChecking/blob/refactor/Figures/Majority.png "Majority Design")

![Figure5](https://github.com/fluentverification/CaseStudies_StochasticModelChecking/blob/refactor/Figures/Speed_Independent.png "Speed-Speed_Independent")

![Figure6](https://github.com/fluentverification/CaseStudies_StochasticModelChecking/blob/refactor/Figures/Toggle.png "Toggle-Switch")

### Toggle Switch

The toggle switch is a state holding gate and consists of two promoters each followed by a coding sequence. Each promoter is repressed by the protein transcribed by the other promoter [4].

![Figure7](https://github.com/fluentverification/CaseStudies_StochasticModelChecking/blob/refactor/Figures/ToggleSwitch.png "Toggle-Switch")

### Repressilator

The repressilator consists of three promoters each with a repressor gene. It is a cyclic negative-feedback loop, periodically inducing the synthesis of green fluorescent proteins [5].

![Figure8](https://github.com/fluentverification/CaseStudies_StochasticModelChecking/blob/refactor/Figures/Repressilator.PNG "Repressilator")

### Dual Feedback Osciallator

### References

1. Nielsen, A. A. K.; Der, B. S.; Shin, J.; Vaidyanathan, P.; Paralanov, V.; Strychalski, E. A.; Ross, D.; Densmore, D.; Voigt, C. A. Genetic Circuit Design Automation. Science 2016, 352 (6281), aac7341–aac7341. https://doi.org/10.1126/science.aac7341.

2. Fontanarrosa, P.; Doosthosseini, H.; Borujeni, A. E.; Dorfan, Y.; Voigt, C. A.; Myers, C. Genetic Circuit Dynamics: Hazard and Glitch Analysis. ACS Synthetic Biology 2020, 15.

3. Madsen, C.; Zhang, Z.; Roehner, N.; Winstead, C.; Myers, C. Stochastic Model Checking of Genetic Circuits. J. Emerg. Technol. Comput. Syst. 2014, 11 (3), 1–21. https://doi.org/10.1145/2644817.

4. Gardner, T. S.; Cantor, C. R.; Collins, J. J. Construction of a Genetic Toggle Switch in Escherichia Coli. Nature 2000, 403 (6767), 339–342. https://doi.org/10.1038/35002131.

5. Elowitz, M. B.; Leibler, S. A Synthetic Oscillatory Network of Transcriptional Regulators. Nature 2000, 403 (6767), 335–338. https://doi.org/10.1038/35002125.
