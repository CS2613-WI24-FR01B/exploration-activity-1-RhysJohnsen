[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-24ddc0f5d75046c5622901739e7c5dd533143b0c8e959d652212380cedb1ea36.svg)](https://classroom.github.com/a/FJiO-WNb)
# EA1 Rhys Johnsen
## What library?
This exploration activity looks at some of the uses of the NumPy library
## How to run the program
This program simulates a dairy farm week by week. inputs are below:
>next

Progress to the next week
>cure

Will prompt you to enter a cow's number to cure
>age

Prints the ages of all cows
>prod

Prints the production of all cows
>weight

Prints the weights of all cows
>end

Ends the program
>sick

Shows which cows are sick (Only for debugging use to see that sick cows do have reduced weight & production)
## What purpose?
This program is used to keep track of a dairy farm. This program will only alert the user when there are things that may or may not require attention, like low production or weight. when a cow has both of these, the program will suggest that the cow is sick, and may need treatment. (not always the case, weights and production will fluctuate)
## Sample input/output
>next

All is normal
>next

The following cow(s) have produced too little:
[94]
>next

The following cow(s) have produced too little:
[44][94]
>next

The following cow(s) have produced too little:
[44][55]
>next

The following cow(s) have produced too little:
[44][46][55][57][94]
The following cow(s) weigh too little:
[94]
The following cow(s) are likely sick:
[94]
>cure

Which cow would you like to cure?
>94

This cow was sick
>cure

Which cow would you like to cure?
>6

This cow was not sick
>end