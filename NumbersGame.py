{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Welcome to our git page! Enter your name:  madeleine\n",
      "Guess the secret number!  3\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "OOPS! madeleine you did not guess correctly! The secret number was 7\n"
     ]
    }
   ],
   "source": [
    "## This python program has a user guess a number\n",
    "    ## if invalid value is entered, the program is terminated\n",
    "\n",
    "name = input(\"Welcome to our git page! Enter your name: \")\n",
    "\n",
    "guess = input(\"Guess the secret number! \")\n",
    "\n",
    "try:\n",
    "    guess = int(guess)\n",
    "    secret_number = 7\n",
    "    if guess == secret_number:\n",
    "        valid = True\n",
    "        print(\"Congrats! \" + name + \" you guessed correctly!\")\n",
    "    else:\n",
    "        valid = False\n",
    "        print(\"OOPS! \" + name + \" you did not guess correctly! The secret number was \" + str(secret_number))\n",
    "except:\n",
    "    print(\"You entered an invalid value. Please re-run and enter an integer.\")\n",
    "    "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.8.3"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
