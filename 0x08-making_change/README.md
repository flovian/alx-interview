# Making Change

This code calculates the fewest number of coins needed to make each value from 0 to total, and then return the value in the last element of the list. 

## Tasks

+ [x] 0. **Change comes from within**<br/>[0-making_change.py](0-making_change.py) contains a module with a function that determines the fewest number of coins needed to meet a given amount `total` when given a pile of coins of different values, with the following requirements:
  + Prototype: `def makeChange(coins, total)`.
  + Return: fewest number of coins needed to meet `total`.
    + If `total` is `0` or less, return `0`.
    + If `total` cannot be met by any number of coins you have, return `-1`.
  + `coins` is a list of the values of the coins in your possession.
  + The value of a coin will always be an integer greater than `0`.
  + You can assume you have an infinite number of each denomination of coin in the list.
  + Your solution’s runtime will be evaluated in this task.
