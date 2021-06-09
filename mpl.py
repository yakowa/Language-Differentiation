# Importing dependencies
import matplotlib.pyplot as plt
import numpy as np

def showBarChart(alpha, beta, colour="#bb0f83", width=0.1):
    # Setting x
    if alpha == "alpha":
        # If alphabet mode is wanted - set x as the alphabet
        x = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]    
    else:
        # If not alphabet mode - custom mode
        x = alpha
    
    # Setting y
    # print(beta[x[0]])
    y = []
    for i in x:
        y.append(beta[i])

    # Plotting the graph
    plt.title('Letter Frequency')
    plt.gcf().canvas.set_window_title('Language Differentiation')
    plt.bar(x, y, color=colour, width=width)
    plt.show()


def showCompBarChart(alpha, beta, alphaTwo, betaTwo, colour="#bb0f83", width=0.2):
    # Setting x
    if alpha == "alpha":
        # If alphabet mode is wanted - set x as the alphabet
        x = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]    
    else:
        # If not alphabet mode - custom mode
        x = alpha
    if alphaTwo == "alpha":
        # If alphabet mode is wanted - set x2 as the alphabet
        x2 = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]    
    else:
        # If not alphabet mode - custom mode
        x2 = alphaTwo
    
    # Setting y
    y = []
    for i in x:
        y.append(beta[i])    

    # Setting y2
    y2 = []
    for i in x2:
        y2.append(betaTwo[i])

    # Plotting the graph
    plt.title('Compare Languages | Blue - One, Orange - Two')
    plt.gcf().canvas.set_window_title('Language Differentiation')
    plt.bar(x2, y2, color="orange", width=width+0.4)
    plt.bar(x, y, color="blue", width=width)
    plt.show()