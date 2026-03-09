# DriveGo


## A smart ordering system for Restaurants and Cafes that allows customers to order using their Car Plate Number to avoid waiting in line.


### Project Idea 
- Instead of waiting for a waiter or standing in a queue, the customer is identified by their car plate. The system recognizes them, remembers their usual order, and applies loyalty discounts automatically.


### Objectives 
- Speed up the ordering process
- Use the car plate as a digital ID.
- Reward frequent customers with automatic points.

### Features 
- Find customer info instantly by plate number.
- Repeat Last Order: "The usual" order is ready inone click.
- 10 points per visit. 100 points = 10 SAR discount.
- Automatic total calculation and bill summary.


### Project Contents
- main.py: To run the application.
- restaurant.py: Handles the menu, prices, and bills.
- customer.py: Manages customer data and plate formats.
- utils.py: Colors the messages (Green for success, Red for errors).


### Usage Scenario:
- Arrival: Customer arrives; staff enters plate ABC 123.
- Recognition: System says: "Welcome back! Do you want your usual Latte?"
- Ordering: Customer confirms or adds a new item.
- Checkout: Points are added, discount is applied, and the order is done—No waiting!

## Installation
- Download the project files
- Run main.py using Python.