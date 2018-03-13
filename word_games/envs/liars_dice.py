"""OpenAI Gym Environment for Liar's Dice


"""

import gym
from random import randint
from collections import Counter
from gym import error, spaces, utils
from gym.utils import seeding

class Player:
	"""A player in the game of Liar's Dice
	
	Has the following properties:
	
	- hand: tuple of current roll
	- starting_dice: original number of dice
	- dice: number of dice remaining
		
	"""
	
	def __init__(self, agent, dice = 5):
		self.agent = agent
		self.starting_dice = dice
		self.dice = self.starting_dice
		self.hand = self.roll()
	def roll(self):
		_ = Counter()
		for die in range(self.dice):
			_.update(str(randint(1,6)))
		return _
	def reset(self):
		self.dice = self.starting_dice
		self.hand = self.roll()
	def act(self):
		self.agent.act()

class LiarsDiceEnv(gym.Env):
	"""Liar's Dice environment
	
	Liar's dice is a game where players roll a hand of 5 dice and place
	wagers about the quantity and value of dice. Players can call another 
	player's wager, forcing everyone to reveal their dice and determine whether
	the wager was valid or not. If the wager was valid, the player who called
	loses a die, otherwise the player who wagered loses a die. The players then
	roll a new hand of dice. The game ends when only one player can still roll.
	
	This implementation increases the reward the longer a player remains in the game
	"""
	
  def __init__(self):
	raise NotImplementedError  
  def step(self, action):
	for player in self.players:
		player.act()
    return obs, reward, done, info
  def reset(self):
    for player in self.players:
		player.reset()
  def render(self, mode='human', close=False):
    raise NotImplementedError