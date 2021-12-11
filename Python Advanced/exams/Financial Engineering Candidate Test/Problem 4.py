#bubble sort algorithm

def sort(list_numbers): #the only argument of the function is the list of numbers
    for num_1 in range(len(list_numbers)):
        for num_2 in range(len(list_numbers) - 1):
            if list_numbers[num_2] > list_numbers[num_2 + 1]:
                list_numbers[num_2], list_numbers[num_2 + 1] = \
                    list_numbers[num_2 + 1], list_numbers[num_2] #swap values

    return list_numbers


list_numbers = [3, 2, 5, 6, 1, 50, 35]  #test integer numbers
sorted_list = sort(list_numbers)  #the functions is invoked and the sorted list is returned
print(" ".join(map(str, sorted_list))) #the print function prints the sorted numbers on the console

from math import sqrt, log, exp
from scipy.stats import norm  # we need this for the normal distribution function


def option_value(S, K, T, r, sigma):
    # I have intentionally changed the name of the function to follow Python conventions

    d_1 = (log(S / K) + (r + 0.5 * sigma ** 2) * T) / (sigma * sqrt(T))
    d_2 = (log(S / K) + (r - 0.5 * sigma ** 2) * T) / (sigma * sqrt(T))

    call_option_price = (S * norm.cdf(d_1, 0.0, 1.0) - K * exp(-r * T) * norm.cdf(d_2, 0.0, 1.0))

    return call_option_price, d_1  # the function returns a tuple of the option price, d1


def implied_volatility():
    initial_option_price = 1.9  # arbitrarily chosen price of call option from option chain
    epsilon = 1  # Define variable to check stopping conditions
    abstol = 0.0001  # Stop calculation when abs(epsilon) < this number

    iteration = 0  # Variable to count number of iterations
    max_iter = 1000  # Max number of iterations before aborting

    sigma = 0.25

    while epsilon > abstol:
        if iteration > max_iter:
            break

        iteration = iteration + 1

        call_option_price, d_1 = option_value(50, 100, 1, 0.05, 0.25)  # here we call the optionValue function
        # I have slightly changed the return values of the option_value function for this task, as we also need
        # d1
        expression = call_option_price - initial_option_price

        vega = 50 * norm.pdf(d_1) * sqrt(0.05)
        implied_volatility_value = -expression / vega + sigma
        epsilon = abs(expression)

    return implied_volatility_value


result = option_value(50, 100, 1, 0.05, 0.25)
print(result)
print(implied_volatility())
