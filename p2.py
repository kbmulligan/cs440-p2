"""
CS440 Assignment 2
Submitted by K. Brett Mulligan (CSUID: 830189830)
My code utilizes the search.py code from the text.
To run my code...
To find a solution to the puzzle...
My code runs in ... time ...
"""

#################################################
# p2.py - find a solution to the Huarong Pass Puzzle
# by K. Brett Mulligan
# 9 Sep 2014
# CSU CS440
# Dr. Asa Ben-Hur
#################################################

from __future__ import absolute_import

import search.py
import sys

DO_TESTING = False
DO_VERBOSE_PARSING = False


print sys.version
print sys.version_info

# Given "search_type" of 'BFS', 'DFS', 'IDS', or 'BID'
# returns a list of actions which lead initial state to goal state
def huarong_pass_search(search_type):
    return