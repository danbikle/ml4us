class03rsquared/readme.txt

This folder contains scripts which help me understand the idea of "R-Squared" AKA "R2".

In the book, "Introduction to Statistical Learning", the authors introduce R2 in Chapter 3 "Linear Regression":

http://www-bcf.usc.edu/~gareth/ISL/ISLR%20Seventh%20Printing.pdf

R2 is a number between 0 and 1 which describes how well a model fits some test data.

I like the R2 idea because the data can come from many types of observations.

For example I could have a model-1 which attempts to describe the price of IBM.

And I could have model-2 which wants to describe the temperature of San Jose.

If R2 from model-2-predictions is larger than R2 from model-1-predictions,
then model-2 is more accurate and perhaps "better".

The formula for R-Squared is this:

R2 = 1 - RSS/TSS

where RSS is sum((yi - yhati)**2)
where yhati are predicted values of yi from the model I want to evaluate.
and   TSS is sum((yi - mean(yi))**2)

I demonstrate R2 using some Python scripts.

