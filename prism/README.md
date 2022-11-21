### Genetic Toggle Switch
This genetic circuit model for the toggle switch has two inputs aTc and IPTG. It can be set to the OFF state by supplying it with aTc and set to ON state by supplying IPTG. Two important properties for a toggle switch circuit are the response time and failure rate. The CSL property is given by "P=? [true U<=2100 (TetR>40 &  LacI<20)]". 

### Robot World
This case study considers a robot moving in an n×n grid world taken from and a janitor moving in a larger grid KnxKn, where $K$ is constant scaling factor which makes the system practically infinite state. The robot starts from the bottom left corner to reach the top right corner. The Janitor moves around the larger grid randomly. Only robot or janitor can occupy one position at any given time. The robot also randomly communicates with the base station. We calculate the probability that the robot reaches the top right corner within $100$ time units while periodically communicating with the base station. The CSL formula describing the property is "P_{=?} [(P>=0.5 [ true U<=7 (c=1)]) U<=100 ((x1=n)&(y1=n))]"$''". 

### Jackson Queuing Network
A Jackson Queuing Network (JQN) consists of $N$ interconnected nodes (queues) with infinite queue capacity. Initially, all queues are considered empty. Each station is connected to a single server which distributes the arrived jobs to different stations. Customers arrive as a Poisson stream with intensity $\lambda$ for $N$ queues. A customer, upon completing service at a node $i$, either leaves the network or enters another node $j$. We consider the case with $N=4,5$ with constant $\lambda=5$. We compute the probability that, within 10 time units, the first queue has more that $3$ jobs and the second queue has more than $5$ jobs, given by the CSL property "P_{=?} [true U[0.0,10.0]  (s\_1>=4) & (s_2>=6)]". 

### Cyclic Server Polling System
This case study taken from the PRISM's benchmark suite. It is based on a cyclic server attending N stations. For model checking, we consider the probability that station one is polled within 10 time units, described by the CSL formula "P=? [true U<=10 (s=1 &  a=0)]". 

### Tandem Queuing Network 
Tandem queuing network is the simplest interconnected queuing network with two queues with one server each. Customers join the first queue and enters the second queue immediately after completing the service. We consider both queues with capacity c. In this paper we consider the probability that, first queue becomes full in 0.25 time units given by CSL property "P_{=?} [true U<=T sc=c]". 
