## SBML Benchmark Suite
The first benchmark suite is adapted from the systems biology markup language (SBML) [1,2] stochastic test suite [3] accessible at https://github.com/sbmlteam/sbml-test-suite/tree/release/cases/stochastic. SBML is an XML-based data format encoding models of biological systems. The test suite is designed for testing software for analyzing SBML models and has been converted into the PRISM language to also allow the testing of software for stochastic model checking. From the 100 cases provided by the SBML test suite, three were not included since the SBML-to-PRISM converter currently does not support rules or events.


## PRISM Benchmark Suite
In addition to the SBML benchmark models, we have included the PRISM benchmark suite [4]. This suite has several models including game models and ``toy'' simulations. The PRISM benchmark suite is licensed under the GPLv2 license, a prominent open-source license that allows for redistribution and modification as long as the license under which any copies (modified or not) remain unchanged. As a result of this freedom, PRISM benchmarks are also accessible in our repository. These models are used to test STAMINA [5,6], an infinite model-checking tool which supports the PRISM format.

## References
[1] Keating, Sarah M., Dagmar Waltemath, Matthias König, Fengkai Zhang, Andreas Dräger, Claudine Chaouiya, Frank T. Bergmann et al. "SBML Level 3: an extensible format for the exchange and reuse of biological models." Molecular systems biology 16, no. 8 (2020): e9110.

[2] Hucka, Michael, Andrew Finney, Herbert M. Sauro, Hamid Bolouri, John C. Doyle, Hiroaki Kitano, Adam P. Arkin et al. "The systems biology markup language (SBML): a medium for representation and exchange of biochemical network models." Bioinformatics 19, no. 4 (2003): 524-531.

[3] Evans, Thomas W., Colin S. Gillespie, and Darren J. Wilkinson. "The SBML discrete stochastic models test suite." Bioinformatics 24, no. 2 (2008): 285-286.

[4] Kwiatkowska, Marta, Gethin Norman, and David Parker. "PRISM 4.0: Verification of probabilistic real-time systems." In Computer Aided Verification: 23rd International Conference, CAV 2011, Snowbird, UT, USA, July 14-20, 2011. Proceedings 23, pp. 585-591. Springer Berlin Heidelberg, 2011.

[5] Neupane, Thakur, Chris J. Myers, Curtis Madsen, Hao Zheng, and Zhen Zhang. "Stamina: Stochastic approximate model-checker for infinite-state analysis." In Computer Aided Verification: 31st International Conference, CAV 2019, New York City, NY, USA, July 15-18, 2019, Proceedings, Part I 31, pp. 540-549. Springer International Publishing, 2019.

[6] Roberts, Riley, Thakur Neupane, Lukas Buecherl, Chris J. Myers, and Zhen Zhang. "STAMINA 2.0: Improving scalability of infinite-state stochastic model checking." In Verification, Model Checking, and Abstract Interpretation: 23rd International Conference, VMCAI 2022, Philadelphia, PA, USA, January 16–18, 2022, Proceedings, pp. 319-331. Cham: Springer International Publishing, 2022.
