---
id: hit_rate
title: Hit Rate
sidebar_position: 5
---

# Hit Rate

## Summary
The ratio of user hits divided by the total number of users.

## Description
The ratio of user hits divided by the total number of users (user hit: a user that has accessed at least one service that is also a personal recommendation). The metric is expressed by the formula: $$Hit Rate=\frac{hits}{users}$$

## Output

| Type | Float |
| --- | ----------- |
| Min | 0 |
| Max | +$$\infty$$ |

:::info
A value of 0 indicates that no user hits occurred.
:::

## Prerequisites:
* all available recommendations by registered users
* all available users

## Process Flow:
* ### Retrieve user-service association
For each user get the recommended services and the services the user accessed "services" files accordingly
* ### Calculate hits
Check if the user has at least one accessed service in recommendations. If yes increase number of hits by one
* ### Calculate ratio
Divide user hits by the total number of users



