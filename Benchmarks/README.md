## SBML Benchmark Suite
The first benchmark suite is adapted from the systems biology markup language (SBML) [1,2] stochastic test suite [3] accessible at https://github.com/sbmlteam/sbml-test-suite/tree/release/cases/stochastic. SBML is an XML-based data format encoding models of biological systems. The test suite is designed for testing software for analyzing SBML models and has been converted into the PRISM language to also allow the testing of software for stochastic model checking. From the 100 cases provided by the SBML test suite, three were not included since the SBML-to-PRISM converter currently does not support rules or events.


## References
[1] Keating, Sarah M., Dagmar Waltemath, Matthias König, Fengkai Zhang, Andreas Dräger, Claudine Chaouiya, Frank T. Bergmann et al. "SBML Level 3: an extensible format for the exchange and reuse of biological models." Molecular systems biology 16, no. 8 (2020): e9110.

[2] Hucka, Michael, Andrew Finney, Herbert M. Sauro, Hamid Bolouri, John C. Doyle, Hiroaki Kitano, Adam P. Arkin et al. "The systems biology markup language (SBML): a medium for representation and exchange of biochemical network models." Bioinformatics 19, no. 4 (2003): 524-531.

[3] Evans, Thomas W., Colin S. Gillespie, and Darren J. Wilkinson. "The SBML discrete stochastic models test suite." Bioinformatics 24, no. 2 (2008): 285-286.
