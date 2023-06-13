# Fault Tolerance Computing and Electronics 

This directory contains models in the fault tolerance domain. 

At present there are two subdirectories containing 
specialized models:

```
|-- Redundancy
|   |-- RFB
|   `-- TMR
`-- StochasticComputing
    |-- divide_by_two
    `-- divider
```

An overview of each subcategory and the specific models is 
provided in the text below. All of the provided cases are 
designed to model transient noise or "soft" upsets, as opposed 
to permanent hardware defects.


# Redundancy Models

Fault tolerant systems usually have redundant modules and/or signals 
so that the system's correct function can be recovered, even in the 
event of an error.

## TMR: Triple Modular Redundancy

This model represents a classic "majority vote" redundancy technique 
that has been deployed in critical systems since the 1960s. The TMR
model has a low state complexity and is provided mainly as a benchmark
for judging the RFB model.

## RFB: Restorative Feedback

This model is an updated form of TMR designed to suppress transient 
faults. RFB is also suitable for fault tolerance with non-binary 
discrete signals as might be encountered in a data communication bus
or high-density Flash memory. Due to its feedback dynamics and 
non-binary signals, RFB can have a large or infinite state complexity.

Two PRISM models are provided:

* `rfb.pm` -- a binary-valued model with low state complexity.
* `rfb_inf.pm` -- a multiple-valued model with infinite state complexity.


# Stochastic Computing Models

Fault tolerant systems sometimes employ "approximate" computing strategies 
for masking or detecting errors in arithmetic or signal processing 
circuits. Stochastic computing circuits operate by filtering pseudo-
random bit-streams (PRBS) wherein the computation depends on the overall 
average value rather than any particular bit. These circuits are therefore
insensitive to a small number of transient upsets.

## Divide-By-Two Circuit

The stochastic divide-by-two function is based on the toggle flip-flop, 
which provides a uniform output probability (i.e. average) independent 
of the input probability. By using a simple feedback arrangement, this 
property can be used to divide a PRBS value by 2.


## Divider

The divider circuit uses a counter to estimate a PRBS probability and 
"re-emit" an independent PRBS with the same average value. The re-
emitted stream is then used in feedback to obtain the ratio of two 
PRBS averages. Two models are provided:

* `divider.pm` -- a finite-state model with a fixed counter precision.
* `divider_inf.pm` -- an infinite-state model with a variable counter precision.

