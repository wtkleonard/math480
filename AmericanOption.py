""" Provides classes and methods to compute the prices
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

Note: The code is designed for Python 3.x."""

class BinomialTree:
    """ Specifies data structure indexed by a binomial
    tree. """
    def __init__(self,  N):
        """ Construct a binomial tree given the number of
        time steps. """
        tree = []
        for n in range(1, N+2):
            tree.append([None]*n)
        self.tree = tree

    def GetNode(self, n, i):
        """ Get the value at node (n, i). """
        return self.tree[n][i]

    def SetNode(self, n, i, value):
        """ Set the value at node (n, i). """
        self.tree[n][i] = value

    def Display(self, precision = 1):
        """ Display the tree given the precision """
        N = len(self.tree) - 1
        for n in range(N + 1):
            for i in range(n + 1):
                print(round(self.GetNode(n, i), precision), end = " ")
            print()

class BinomialModel:
    """ Specifies a binomial tree model. S0 is the initial
    stock price. At each time step, the stock price will either
    go up by U or go down by D. The number of time steps is N.
    R is the risk-free interest rate per period. It also contains
    a price tree for the stock. And a method to compute the
    risk-neutral probability. """
    
    def __init__(self, U, D, R, S0, N):
        """ Create a binomial tree model with up factor U, down
        factor D, risk-free interest rate R, initial stock price S0,
        and number of time steps N """
        self.U = U
        self.D = D
        self.R = R
        self.S0 = S0
        self.N = N

        # Construct the price tree of the stock
        Tree = BinomialTree(self.N)
        for n in range(0, self.N+1):
            for i in range(n+1):
                Tree.SetNode(n, i, self.ComputeS(n, i))
        self.StockTree = Tree

    def GetR(self):
        return self.R

    def GetN(self):
        return self.N

    def RiskNeutP(self):
        """ Returns the risk-neutral probability of the model. """
        return (1 + self.R - self.D) / (self.U - self.D)

    def ComputeS(self, n, i):
        """ Computes the stock price at node (n, i) """
        return self.S0*(self.U**i)*(self.D**(n-i))

class AmericanOption:
    """ Models an American option whose payoff depends only on
    the current stock price """
    def __init__(self, payoff):
        self.payoff = payoff
        
    def Price(self, Model):
        """ Computes the price tree of the American option using
        Snell's envelope. It returns the current price as well as
        the complete price tree. """
        
        N = Model.GetN()
        StockTree = Model.StockTree
        PriceTree = BinomialTree(N)
        p = Model.RiskNeutP()
        q = 1 - p

        for i in range(N+1):
            PriceTree.SetNode(N, i, self.payoff(StockTree.GetNode(N, i)))

        for n in range(N-1, -1, -1):
            for i in range(n+1):
                value1 = self.payoff(StockTree.GetNode(n, i))
                value2 = (p*PriceTree.GetNode(n+1, i+1) +
                          q*PriceTree.GetNode(n+1, i)) / (1 + Model.GetR())
                PriceTree.SetNode(n, i, max(value1, value2))

        return(PriceTree.GetNode(0, 0), PriceTree)

def const_call_payoff(K):
    """ Constructs the payoff function of the vanilla American
    call option with strike price K. """
    def call_payoff(S):
        return max(S - K, 0)
    return call_payoff

def const_put_payoff(K):
    """ Constructs the payoff function of the vanilla American
    put option with strike price K. """
    def put_payoff(S):
        return max(K - S, 0)
    return put_payoff

def const_call():
    """ Constructs an Americal call option and returns an object of class
    AmericanOption. The user inputs the strike price. """
    call_K = eval(input("Enter strike price of American call option: "))
    print()
    call_payoff = const_call_payoff(call_K)
    return AmericanOption(call_payoff)

def const_put():
    """ Constructs an Americal put option and returns an object of class
    AmericanOption. The user inputs the strike price. """    
    put_K = eval(input("Enter strike price of American put option: "))
    print()
    put_payoff = const_call_payoff(put_K)
    return AmericanOption(put_payoff)

def display_results(option, Model, precision = 1):
    """ Displays the current price of the option priced under Model. """
    results = option.Price(Model)
    print("The price of the option is", round(results[0], precision))
    print("\nThe price tree of the option is:")
    results[1].Display(precision)
    print("\nThe price tree of the stock is:")
    Model.StockTree.Display(precision)
    print()

def const_model():
    """ Creates a BinomialModel object using data inputed by the
    user. """
    U_, D_, R_, S0_, N_ = eval(input("Enter U, D, R, S0 and N: "))
    print()
    return BinomialModel(U_, D_, R_, S0_, N_)


def main():   
   Model = const_model()
   
   call = const_call()
   display_results(call, Model)

   put = const_put()
   display_results(put, Model)

main()
