# Unipolar Stochastic Divider Model

This case example models a stochastic divider using 
the unipolar stochastic numerical format. In the 
unipolar format, a signal $x$ is a real number between 
0 and 1, encoded probabilistically in a binary signal 
$X(t)$. At any time $t$, the signal $X(t)=1$ with 
probability $x$, and $X(t)=0$ with probability $1-x$.

The divider circuit accepts two stochastic inputs, 
$A(t)$ and $B(t)$, and produces a single output 
$Q(t)$. Ideally $Q$ should arrive at a steady-state 
probability $Q(t)=q=a/b$. 

The PRISM model for this circuit is provided in 
`divider.pm`. The input probabilities are given 
via constants `a` and `b`. Internally, the stochastic 
input signals are `inA` and `inB`, and the output 
signal is `Q`.

Two example properties are given in `divider.props`:

* `P=? [ F[T,T] Q = 1 ]`  evaluates the probability 
that Q=1 (i.e. the numerical output $q$) at `T` clock cycles, 
which relates to the circuit's response time. The constant `T`
is an integer.
* `S=? [ Q = 1 ]` evaluates the steady-state probability
that Q=1. 

## Example results:

### `a=0.1`, `b=0.3`, and `T=100` 

The expected output is $q=1/3$. 

```
prism --const a=0.1 --const b=0.3 --const T=100 divider.pm divider.props
```

For the first property (at 100 clock cycles) PRISM returns:

```
Result: 0.4665562152140168 (exact floating point)
```

For the second property (steady state) PRISM returns:

```
Result: 0.33333443639168
```


### `a=0.7`, `b=0.3`, and `T=100` 

In this case the ratio $a/b$ is greather than one, so the expected output 
is saturated close to $q=1$. 

```
prism --const a=0.1 --const b=0.3 --const T=100 divider.pm divider.props
```

For the first property (at 100 clock cycles) PRISM returns:

```
Result: 0.8790749994268042 (exact floating point)
```

For the second property (steady state) PRISM returns:

```
Result: 0.9881554646304057
```

