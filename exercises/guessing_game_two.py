#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import print_function 
import random
"""
ITERATION THREE: Now that you have written a simple guessing
game, add some logic in that determines if the game is over
when either:
* user has correctly guesses the number
* user has reached 5 guesses

Let's use two functions:

* is_guess_correct
* display_user_output

STRETCH: In the case user loses, show correct number.
In the case user wins tell them how many guesses it took for
them to win. Both situations show user all guesses they made.
"""

def display_user_output(num_to_guess, guessed_num):
	"""
	:param: guessed_num - number user guessed
	:param: num_to_guess - number the user has to guess

	:returns string saying if the guess is too high, too low, or match
	"""

def is_guess_correct(num_to_guess, guessed_num):
	"""
	:param: guessed_num - number user guessed
	:param: num_to_guess - number the user has to guess

	:returns boolean True if correct else False	
	"""

game_not_over = False
turns = 0

while game_not_over:
	# TODO: ask for user input 
	# determine what message to show user
	# determine if guess is correct