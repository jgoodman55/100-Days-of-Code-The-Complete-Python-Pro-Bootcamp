# Coffee Machine Simulator

A command-line coffee machine simulation built with Python. Users can order drinks, insert coins, and receive change, while the machine tracks its ingredient resources and total profit across the session.

---

## Features

- Interactive CLI prompt with input validation
- Three drink options with unique ingredient and cost requirements
- Coin-based payment system with automatic change calculation
- Resource tracking that prevents orders when ingredients run low
- Live reporting of current resources and profit
- Clean shutdown via a turn-off command

---

## Project Structure

```
.
├── main.py           # Entry point and main event loop
├── menu.py           # MenuItem and Menu classes
├── coffee_maker.py   # Resource management and drink preparation
└── money_machine.py  # Coin processing and payment logic
```

---

## Requirements

- Python 3.8 or higher
- No third-party dependencies

---

## Usage

```bash
python main.py
```

At the prompt, type one of the following commands:

| Command | Description |
|---|---|
| `espresso` | Order an espresso ($1.50) |
| `latte` | Order a latte ($2.50) |
| `cappuccino` | Order a cappuccino ($3.00) |
| `report` | Print current resource levels and profit |
| `off` | Turn off the machine and exit |

---

## Drink Menu

| Drink | Water | Milk | Coffee | Cost |
|---|---|---|---|---|
| Espresso | 50ml | 0ml | 18g | $1.50 |
| Latte | 200ml | 150ml | 24g | $2.50 |
| Cappuccino | 250ml | 50ml | 24g | $3.00 |

---

## Starting Resources

| Resource | Amount |
|---|---|
| Water | 300ml |
| Milk | 200ml |
| Coffee | 100g |

---

## Example Session

```
What would you like? latte/espresso/cappuccino/: latte
Please insert coins.
How many quarters?: 10
How many dimes?: 0
How many nickles?: 0
How many pennies?: 0
Here is $0.0 in change.
Here is your latte. Enjoy!

What would you like? latte/espresso/cappuccino/: report
Water: 100ml
Milk: 50ml
Coffee: 76g
Money: $2.5

What would you like? latte/espresso/cappuccino/: off
```

---

## Module Overview

**`main.py`** runs the main loop, handles user input, and coordinates the three supporting modules.

**`menu.py`** defines `MenuItem` (name, cost, ingredient quantities) and `Menu` (item lookup and listing).

**`coffee_maker.py`** manages ingredient levels, checks whether a drink can be made, and deducts resources after a successful order.

**`money_machine.py`** handles coin input, calculates the total inserted, issues change, and accumulates profit.
