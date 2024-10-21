"""The Game of Hog."""

from dice import six_sided, make_test_dice
from ucb import main, trace, interact

GOAL = 100  # The goal of Hog is to score 100 points.

######################
# Phase 1: Simulator #
######################


"""
>>> from hog import *
>>> roll_dice(2, make_test_dice(4, 6, 1))
这个的意思是投骰子两次, 第一次投出4点, 第二次投出6点;(4, 6, 1)是一个骰子, 代表了骰子的点数,骰子会不断循环4, 6, 1, 4, 6, 1, 4, 6, 1, ...
? 10
-- OK! --

---------------------------------------------------------------------
>>> from hog import *
>>> roll_dice(3, make_test_dice(4, 6, 1))
这里是投骰子三次, 第一次投出4点, 第二次投出6点, 第三次投出1点,只要有1点,就返回1
? 1
-- OK! --

---------------------------------------------------------------------
>>> from hog import *
>>> roll_dice(4, make_test_dice(2, 2, 3))
? 9
-- OK! --

---------------------------------------------------------------------
>>> from hog import *
>>> a = roll_dice(4, make_test_dice(1, 2, 3))
>>> a # check that the value is being returned, not printed
这里返回的是a的值,而不是打印出来
? 1
-- OK! --

---------------------------------------------------------------------
>>> from hog import *
>>> counted_dice = make_test_dice(4, 1, 2, 6)
>>> roll_dice(3, counted_dice)
这里是投骰子三次, 第一次投出4点, 第二次投出1点, 第三次投出2点,只要有1点,就返回1
? 1
-- OK! --

>>> # Make sure you call dice exactly num_rolls times!
>>> # If you call it fewer or more than that, it won't be at the right spot in the cycle for the next roll
>>> # Note that a return statement within a loop ends the loop
>>> roll_dice(1, counted_dice)
? 4
-- Not quite. Try again! --
这里会接着counted_dice的顺序往下走,所以第一次投出6点,而不是4点,因为之前已经投过了三次,所以这里是第四次投骰子
? 6
-- OK! --
"""


def roll_dice(num_rolls, dice=six_sided):
    """Simulate rolling the DICE exactly NUM_ROLLS > 0 times. Return the sum of
    the outcomes unless any of the outcomes is 1. In that case, return 1.

    num_rolls:  The number of dice rolls that will be made.
    dice:       A function that simulates a single dice roll outcome.
    """
    # These assert statements ensure that num_rolls is a positive integer.
    assert type(num_rolls) == int, "num_rolls must be an integer."
    assert num_rolls > 0, "Must roll at least once."
    # BEGIN PROBLEM 1
    "*** YOUR CODE HERE ***"
    i = 0
    sum = 0
    one = False
    while i < num_rolls:
        temp = dice()  # dice的return值是一次返回一个
        if temp == 1:
            one = True
        sum += temp
        i += 1
    if one == True:
        return 1
    else:
        return sum

    # END PROBLEM 1


def boar_brawl(player_score, opponent_score):
    """Return the points scored by rolling 0 dice according to Boar Brawl.

    player_score:     The total score of the current player.
    opponent_score:   The total score of the other player.

    """
    # BEGIN PROBLEM 2
    "*** YOUR CODE HERE ***"
    x = player_score % 10
    y = opponent_score // 10 % 10
    ans = 3 * abs(x - y)
    if ans == 0:
        return 1
    else:
        return ans

    # END PROBLEM 2


def take_turn(num_rolls, player_score, opponent_score, dice=six_sided):
    """Return the points scored on a turn rolling NUM_ROLLS dice when the
    player has PLAYER_SCORE points and the opponent has OPPONENT_SCORE points.

    num_rolls:       The number of dice rolls that will be made.
    player_score:    The total score of the current player.
    opponent_score:  The total score of the other player.
    dice:            A function that simulates a single dice roll outcome.

    >>> from hog import *
    >>> take_turn(2, 7, 27, make_test_dice(4, 5, 1))
    单纯的投骰子,投两次,第一次投出4点,第二次投出5点,所以返回9
    ? 9
    -- OK! --

    ---------------------------------------------------------------------
    Question 3 > Suite 1 > Case 2
    (cases remaining: 11)

    >>> from hog import *
    >>> take_turn(3, 15, 9, make_test_dice(4, 6, 1))
    ? 1
    -- OK! --

    ---------------------------------------------------------------------
    Question 3 > Suite 1 > Case 3
    (cases remaining: 10)

    >>> from hog import *
    >>> take_turn(0, 12, 41) # what happens when you roll 0 dice?
    因为是0,所以会进行boar_brawl,返回3 * abs(2 - 4) = 6
    ? 6
    -- OK! --
    """
    # Leave these assert statements here; they help check for errors.
    assert type(num_rolls) == int, "num_rolls must be an integer."
    assert num_rolls >= 0, "Cannot roll a negative number of dice in take_turn."
    assert num_rolls <= 10, "Cannot roll more than 10 dice."
    # BEGIN PROBLEM 3
    "*** YOUR CODE HERE ***"
    if num_rolls == 0:
        return boar_brawl(player_score, opponent_score)
    else:
        return roll_dice(num_rolls, dice)
    # END PROBLEM 3


def simple_update(num_rolls, player_score, opponent_score, dice=six_sided):
    """Return the total score of a player who starts their turn with
    PLAYER_SCORE and then rolls NUM_ROLLS DICE, ignoring Sus Fuss.
    """
    score = player_score + take_turn(num_rolls, player_score, opponent_score, dice)
    return score


def is_prime(n):
    """Return whether N is prime."""
    if n == 1:
        return False
    k = 2
    while k < n:
        if n % k == 0:
            return False
        k += 1
    return True


def num_factors(n):
    """Return the number of factors of N, including 1 and N itself."""
    # BEGIN PROBLEM 4
    "*** YOUR CODE HERE ***"
    i = 1
    count = 0
    while i <= n:
        if n % i == 0:
            count += 1
        i += 1
    return count
    # END PROBLEM 4


def sus_points(score):
    """Return the new score of a player taking into account the Sus Fuss rule."""
    # BEGIN PROBLEM 4
    "*** YOUR CODE HERE ***"
    if num_factors(score) == 3 or num_factors(score) == 4:
        while not is_prime(score):
            score += 1
    return score
    # END PROBLEM 4


def sus_update(num_rolls, player_score, opponent_score, dice=six_sided):
    """Return the total score of a player who starts their turn with
    PLAYER_SCORE and then rolls NUM_ROLLS DICE, *including* Sus Fuss.
    """
    # BEGIN PROBLEM 4
    "*** YOUR CODE HERE ***"
    score = player_score + take_turn(num_rolls, player_score, opponent_score, dice)
    score = sus_points(score)
    return score
    # END PROBLEM 4


def always_roll_5(score, opponent_score):
    """A strategy of always rolling 5 dice, regardless of the player's score or
    the opponent's score.
    """
    return 5


def play(strategy0, strategy1, update, score0=0, score1=0, dice=six_sided, goal=GOAL):
    """Simulate a game and return the final scores of both players, with
    Player 0's score first and Player 1's score second.
    模拟一场游戏并返回两位玩家的最终得分,Player 0 的得分在前,Player 1 的得分在后。

    E.g., play(always_roll_5, always_roll_5, sus_update) simulates a game in
    which both players always choose to roll 5 dice on every turn and the Sus
    Fuss rule is in effect.
    例如,play(always_roll_5, always_roll_5, sus_update) 模拟了一场游戏，
    其中两位玩家每回合都选择掷 5 次骰子，并且 Sus Fuss 规则生效。

    A strategy function, such as always_roll_5, takes the current player's
    score and their opponent's score and returns the number of dice the current
    player chooses to roll.
    策略函数，例如 always_roll_5,接受当前玩家的得分和对手的得分,并返回当前玩家选择掷骰子的次数。

    An update function, such as sus_update or simple_update, takes the number
    of dice to roll, the current player's score, the opponent's score, and the
    dice function used to simulate rolling dice. It returns the updated score
    of the current player after they take their turn.
    更新函数，例如 sus_update 或 simple_update,接受掷骰子的次数、当前玩家的得分、对手的得分以及用于模拟掷骰子的函数。
    它返回当前玩家在回合结束后的更新得分。

    strategy0: The strategy for player0.                                        Player 0 的策略。
    strategy1: The strategy for player1.                                        Player 1 的策略。
    update:    The update function (used for both players).                     更新函数(用于两位玩家)。
    score0:    Starting score for Player 0                                      Player 0 的初始得分。
    score1:    Starting score for Player 1                                      Player 1 的初始得分。
    dice:      A function of zero arguments that simulates a dice roll.         模拟掷骰子的零参数函数。
    goal:      The game ends and someone wins when this score is reached.       当达到此得分时，游戏结束并有人获胜。
    """
    who = 0  # Who is about to take a turn, 0 (first) or 1 (second)
    # BEGIN PROBLEM 5
    "*** YOUR CODE HERE ***"
    while score0 < goal and score1 < goal:
        if who == 0:
            score0 = update(strategy0(score0, score1), score0, score1, dice)
            who = 1
        else:
            score1 = update(strategy1(score1, score0), score1, score0, dice)
            who = 0
    # END PROBLEM 5
    return score0, score1


#######################
# Phase 2: Strategies #
#######################


def always_roll(n):
    """Return a player strategy that always rolls N dice.

    A player strategy is a function that takes two total scores as arguments
    (the current player's score, and the opponent's score), and returns a
    number of dice that the current player will roll this turn.

    >>> strategy = always_roll(3)
    >>> strategy(0, 0)
    3
    >>> strategy(99, 99)
    3
    """
    assert n >= 0 and n <= 10
    # BEGIN PROBLEM 6
    "*** YOUR CODE HERE ***"

    def strategy(score, opponent_score):
        return n

    return strategy
    # END PROBLEM 6


def catch_up(score, opponent_score):
    """A player strategy that always rolls 5 dice unless the opponent
    has a higher score, in which case 6 dice are rolled.

    >>> catch_up(9, 4)
    5
    >>> strategy(17, 18)
    6
    """
    if score < opponent_score:
        return 6  # Roll one more to catch up
    else:
        return 5


def is_always_roll(strategy, goal=GOAL):
    """Return whether STRATEGY always chooses the same number of dice to roll
    given a game that goes to GOAL points.
    返回 STRATEGY 是否在达到 GOAL 分数的游戏中总是选择相同数量的骰子。

    >>> is_always_roll(always_roll_5)
    True
    >>> is_always_roll(always_roll(3))
    True
    >>> is_always_roll(catch_up)
    False
    """
    # BEGIN PROBLEM 7
    "*** YOUR CODE HERE ***"
    score = 0
    check = strategy(0, 0)
    while score < goal:
        opponent_score = 0
        while opponent_score < goal:
            if strategy(score, opponent_score) != check:
                return False
            opponent_score += 1
        score += 1
    return True
    # END PROBLEM 7


def make_averaged(original_function, samples_count=1000):
    """Return a function that returns the average value of ORIGINAL_FUNCTION
    called SAMPLES_COUNT times.

    To implement this function, you will have to use *args syntax.

    >>> dice = make_test_dice(4, 2, 5, 1)
    >>> averaged_dice = make_averaged(roll_dice, 40)
    >>> averaged_dice(1, dice)  # The avg of 10 4's, 10 2's, 10 5's, and 10 1's
    3.0

    >>> from hog import *
    >>> dice = make_test_dice(3, 1, 5, 6)
    >>> averaged_roll_dice = make_averaged(roll_dice, 1000)
    >>> # Average of calling roll_dice 1000 times
    >>> # Enter a float (e.g. 1.0) instead of an integer
    >>> averaged_roll_dice(2, dice)
    注意,这里2组为1循环,即(3, 1), (5, 6),一个进行500次,这里有一个小坑,就是返回的是float,所以要返回6.0
    除此之外,还要注意1的问题,只要有1,就返回1,因此,前面的(3, 1)返回1,后面的(5, 6)返回11,所以最后的结果是6.0,即(1 + 11) * 500 / 1000
    ? 6.0
    """
    # BEGIN PROBLEM 8
    "*** YOUR CODE HERE ***"

    def average(*args):
        i = 0
        sum = 0
        while i < samples_count:
            sum += original_function(*args)
            i += 1
        return sum / samples_count

    return average
    # END PROBLEM 8


def max_scoring_num_rolls(dice=six_sided, samples_count=1000):
    """Return the number of dice (1 to 10) that gives the highest average turn score
    by calling roll_dice with the provided DICE a total of SAMPLES_COUNT times.
    Assume that the dice always return positive outcomes.
    返回掷骰子次数(1 到 10)，通过使用提供的 DICE 调用 roll_dice 总共 SAMPLES_COUNT 次，
    以获得最高的平均回合得分。
    假设骰子总是返回正数结果。

    >>> dice = make_test_dice(1, 6)
    >>> max_scoring_num_rolls(dice)
    1
    """
    # BEGIN PROBLEM 9
    "*** YOUR CODE HERE ***"
    i = 1
    max = 0
    max_num = 0
    while i <= 10:
        temp = make_averaged(roll_dice, samples_count)(i, dice)
        if temp > max:
            max = temp
            max_num = i
        i += 1
    return max_num
    # END PROBLEM 9


def winner(strategy0, strategy1):
    """Return 0 if strategy0 wins against strategy1, and 1 otherwise."""
    score0, score1 = play(strategy0, strategy1, sus_update)
    if score0 > score1:
        return 0
    else:
        return 1


def average_win_rate(strategy, baseline=always_roll(6)):
    """Return the average win rate of STRATEGY against BASELINE. Averages the
    winrate when starting the game as player 0 and as player 1.
    """
    win_rate_as_player_0 = 1 - make_averaged(winner)(strategy, baseline)
    win_rate_as_player_1 = make_averaged(winner)(baseline, strategy)

    return (win_rate_as_player_0 + win_rate_as_player_1) / 2


def run_experiments():
    """Run a series of strategy experiments and report results."""
    six_sided_max = max_scoring_num_rolls(six_sided)
    print("Max scoring num rolls for six-sided dice:", six_sided_max)

    print("always_roll(6) win rate:", average_win_rate(always_roll(6)))  # near 0.5
    print("catch_up win rate:", average_win_rate(catch_up))
    print("always_roll(3) win rate:", average_win_rate(always_roll(3)))
    print("always_roll(8) win rate:", average_win_rate(always_roll(8)))

    print("boar_strategy win rate:", average_win_rate(boar_strategy))
    print("sus_strategy win rate:", average_win_rate(sus_strategy))
    print("final_strategy win rate:", average_win_rate(final_strategy))
    "*** You may add additional experiments as you wish ***"


def boar_strategy(score, opponent_score, threshold=11, num_rolls=6):
    """This strategy returns 0 dice if Boar Brawl gives at least THRESHOLD
    points, and returns NUM_ROLLS otherwise. Ignore score and Sus Fuss.
    """
    # BEGIN PROBLEM 10
    if boar_brawl(score, opponent_score) >= threshold:
        return 0
    else:
        return num_rolls

    # END PROBLEM 10


def sus_strategy(score, opponent_score, threshold=11, num_rolls=6):
    """This strategy returns 0 dice when your score would increase by at least threshold."""
    # BEGIN PROBLEM 11
    ans = sus_update(0, score, opponent_score)
    if ans - score >= threshold:
        return 0
    else:
        return num_rolls

    # END PROBLEM 11


def final_strategy(score, opponent_score):
    """Write a brief description of your final strategy.

    *** YOUR DESCRIPTION HERE ***
    """
    # BEGIN PROBLEM 12
    return 6  # Remove this line once implemented.
    # END PROBLEM 12


##########################
# Command Line Interface #
##########################

# NOTE: The function in this section does not need to be changed. It uses
# features of Python not yet covered in the course.


@main
def run(*args):
    """Read in the command-line argument and calls corresponding functions."""
    import argparse

    parser = argparse.ArgumentParser(description="Play Hog")
    parser.add_argument(
        "--run_experiments", "-r", action="store_true", help="Runs strategy experiments"
    )

    args = parser.parse_args()

    if args.run_experiments:
        run_experiments()
