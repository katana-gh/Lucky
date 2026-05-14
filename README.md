# Lucky

## Overview
An Uno-like game made in the CLI

Lucky is an UNO-like card game built around a simple but punishing gameplay loop. The dealer draws the starting card, the player receives 7 cards, and each turn you must match the current card by either color or number. Once played, that card becomes the new active card that must be matched next.
The deck contains 80 cards across four colors — Red, Blue, Green, and Yellow — with cards numbered 0–9.
Unlike traditional UNO, Lucky introduces a maximum hand size and a deck-shredding mechanic. After a certain turn threshold, drawing cards permanently destroys cards from the deck, making resource management and luck equally important to survival.

## How to Play

- There are three difficulty modes: Easy, Medium, and Hard.
- Each difficulty increases how many cards are shredded from the deck and how quickly punishments occur.
- The dealer draws the starting card.
- The player starts with 7 cards.
- Match the current card by color or number.
- The played card becomes the new active card.
- If no playable card exists, draw a card.
- The player has a maximum hand size of 10.
- If the player exceeds the maximum hand size, a random card is removed from their hand.
- Empty your hand to win.

## Installation

### Prerequisites

- Python 3.12.3+
- uv

Install uv:

```bash
pip install uv
```

### Clone the repository

```bash
git clone https://github.com/katana-gh/Lucky.git
cd Lucky
```

### Install dependencies

```bash
uv sync
```

## Usage

Run the program:

```bash
uv run main.py
```

## License

This project is licensed under the MIT License.
