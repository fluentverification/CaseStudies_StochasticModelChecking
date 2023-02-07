# Stochastic Model Case Studies

Stochastic models are well-suited to studying systems in emerging fields such as nanotechnology, computational chemistry, and synthetic biology. However, the kinds of stochastic models which arise in these emerging fields tend to have infinite state space which cannot be analyzed by most existing tools. It is therefore prudent that tools be developed to verify infinite state space stochastic models. Likewise, there does not exist a collection of case studies for analyzing the performance of infinite state space stochastic model checking tools. Here, such a collection is developed and presented. The collection includes case studies from nanotechnology, computational chemistry, and synthetic biology which vary in complexity from toy models to practical designs encoded in the PRISM language. The models can be used in [PRISM](https://www.prismmodelchecker.org), [STORM](https://www.stormchecker.org), or [STAMINA](https://github.com/fluentverification/stamina-cplusplus) or any other tool that uses the PRISM language. The case-study repository presented here is intended to be a living document, so community contributions and recommendations are welcome.

## Repository structure

### Benchmarks

Benchmarks play a critical role in accessing various systems in computer engineering and science. They ensure a reliable, systematic test to evaluate a computer system's accuracy and performance. The benchmarks of this work includes two different sets of benchmarks.

### Chemical Reaction Networks

Chemical reaction networks are systems including some number of chemical species reacting through some number of defined reaction channels. Because chemical reaction networks underlie all biomolecular processes, their modeling, and analysis are relevant to the design and analysis of biological systems with applications to medicine, biomanufacturing, and biofuels. Stochastic model checking is particularly relevant in these systems because biochemical systems may have low molecule counts, so traditional chemical kinetics are insufficient. This section describes five such examples.

### Genetic Circuits

Genetic circuits are part of synthetic biology, a research field combining engineering principles with biology. Researchers build circuits out of defined biological parts adding desired functionalities to biological systems. Automation in the design process allows scientists to model and analyze their genetic circuits \emph{in silico} to test the system before implementation. Stochastic model checking has been used to analyze genetic circuits before, which have an infinite state space and therefore suit the case studies presented here.

### Fault Computing

Fault tolerant computing encompasses a wide variety of fault mechanisms and strategies to mitigate them. The case studies presented here focus on circuits that experience transient upsets modeled by Markov processes. Case studies in this field are given in two subcategories.
