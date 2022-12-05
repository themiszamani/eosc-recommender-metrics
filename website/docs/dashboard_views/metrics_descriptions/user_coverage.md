---
id: user_coverage
title: User Coverage
sidebar_position: 7
---

# User Coverage

## Summary
The percentage (%) of the division of the unique users found in recommendations to the total number of users.

## Description
The User Coverage is described by the formula $$\frac{unique\_rec\_users}{users}$$

## Output

| Type | Float |
| --- | ----------- |
| Min | 0 |
| Max | 100 |

:::info
User Coverage is 0 when recommendations are being suggested to none users, and 100 when recommendations are being suggested to all of the users.
:::

## Prerequisites:
* all available recommendations
* all available users

## Process Flow:
* ### Retrieve recommendations
Retrieve all available recommendations found in source
* ### Gather all unique users
Gather all unique users found in all available recommendations
* ### Retrieve users
Retrieve all available users found in source
* ### Calculate ratio
 Calculate the percentage (%) of the division of the unique users found in recommendations to the total number of users

