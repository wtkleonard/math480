Provides classes and methods to compute the prices
of American options under the CRR binomial tree model.
We only consider American options which are Markovian
in the sense that the payoff depends only on the current
stock price. The user can define an American option by
specifying a payoff function. The algorithm will output
the price of the option at time 0 as well as its complete
price tree.

Some of the designs are taken from the book Numerical
Methods for Finance with C++ by Maciej J. Capinski
and Tomasz Zatawniak.

Note: The code is designed for Python 3.x.

Example:

>>> main()
Enter U, D, R, S0 and N: 1.1, 0.9, 0.05, 100, 3
Enter strike price of American call option: 100

The price of the option is 15.31

The price tree of the option is:
15.3 
4.5 19.9 
0 6.4 25.8 
0 0 8.9 33.1 

The price tree of the stock is:
100.0 
90.0 110.0 
81.0 99.0 121.0 
72.9 89.1 108.9 133.1 

Enter strike price of American put option: 100

The price of the option is 15.31

The price tree of the option is:
15.3 
4.5 19.9 
0 6.4 25.8 
0 0 8.9 33.1 

The price tree of the stock is:
100.0 
90.0 110.0 
81.0 99.0 121.0 
72.9 89.1 108.9 133.1
>>>

The user can also define other payoff functions and
modify the main() function accordingly.
