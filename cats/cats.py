"""Typing test implementation"""

from utils import lower, split, remove_punctuation, lines_from_file
from ucb import main, interact, trace
from datetime import datetime


###########
# Phase 1 #
###########


def choose(paragraphs, select, k):
    """Return the Kth paragraph from PARAGRAPHS for which SELECT called on the
    paragraph returns true. If there are fewer than K such paragraphs, return
    the empty string.
    """
    # BEGIN PROBLEM 1
    "*** YOUR CODE HERE ***"
    lst = []
    lst = [s for s in paragraphs if select(s)]
    if k < len(lst):
        return lst[k]
    else:
        return ""
    # END PROBLEM 1


def about(topic):
    """Return a select function that returns whether a paragraph contains one
    of the words in TOPIC.

    >>> about_dogs = about(['dog', 'dogs', 'pup', 'puppy'])
    >>> choose(['Cute Dog!', 'That is a cat.', 'Nice pup!'], about_dogs, 0)
    'Cute Dog!'
    >>> choose(['Cute Dog!', 'That is a cat.', 'Nice pup.'], about_dogs, 1)
    'Nice pup.'
    """
    assert all([lower(x) == x for x in topic]), "topics should be lowercase."
    # BEGIN PROBLEM 2
    "*** YOUR CODE HERE ***"

    def sel(par):
        par = remove_punctuation(par)
        par = lower(par)
        lst = split(par)
        for top in topic:
            if top in lst:
                return True
        return False

    return sel

    # END PROBLEM 2


def accuracy(typed, reference):
    """Return the accuracy (percentage of words typed correctly) of TYPED
    when compared to the prefix of REFERENCE that was typed.

    >>> accuracy('Cute Dog!', 'Cute Dog.')
    50.0
    >>> accuracy('A Cute Dog!', 'Cute Dog.')
    0.0
    >>> accuracy('cute Dog.', 'Cute Dog.')
    50.0
    >>> accuracy('Cute Dog. I say!', 'Cute Dog.')
    50.0
    >>> accuracy('Cute', 'Cute Dog.')
    100.0
    >>> accuracy('', 'Cute Dog.')
    0.0
    """
    typed_words = split(typed)
    reference_words = split(reference)
    # BEGIN PROBLEM 3
    "*** YOUR CODE HERE ***"
    lent = len(typed_words)
    lenr = len(reference_words)
    wlen = min(lent, lenr)
    if lent == 0 and lenr == 0:
        return 100.0
    if lent == 0 or lenr == 0:
        return 0.0
    ri, wr = 0, 0
    cou = 0
    while cou < wlen:
        if typed_words[cou] == reference_words[cou]:
            ri = ri + 1
        else:
            wr = wr + 1
        cou = cou + 1
    if lent > lenr:
        wr += lent - lenr
    return ri / (ri + wr) * 100

    # END PROBLEM 3


def wpm(typed, elapsed):
    """Return the words-per-minute (WPM) of the TYPED string."""
    assert elapsed > 0, "Elapsed time must be positive"
    # BEGIN PROBLEM 4
    "*** YOUR CODE HERE ***"
    lenth = len(typed)
    nword = lenth / 5
    return nword * 60 / elapsed
    # END PROBLEM 4


def autocorrect(user_word, valid_words, diff_function, limit):
    """Returns the element of VALID_WORDS that has the smallest difference
    from USER_WORD. Instead returns USER_WORD if that difference is greater
    than LIMIT.
    """
    # BEGIN PROBLEM 5
    "*** YOUR CODE HERE ***"
    if user_word in valid_words:
        return user_word
    curlim = limit
    ret = user_word
    id = 0
    while id < len(valid_words):
        temlim = diff_function(user_word, valid_words[id], limit)
        if temlim <= limit:
            curlim = temlim
            ret = valid_words[id]
            break
        id += 1
    while id < len(valid_words):
        temlim = diff_function(user_word, valid_words[id], limit)
        if temlim < curlim:
            curlim = temlim
            ret = valid_words[id]
        id += 1
    return ret

    # END PROBLEM 5


def shifty_shifts(start, goal, limit):
    """A diff function for autocorrect that determines how many letters
    in START need to be substituted to create GOAL, then adds the difference in
    their lengths.
    """
    # BEGIN PROBLEM 6
    ret = abs(len(start) - len(goal))
    if ret > limit:
        return ret
    if start == "" and goal == "":
        return 0
    if start == "" or goal == "":
        return ret
    if start[0] == goal[0]:
        return shifty_shifts(start[1:], goal[1:], limit)
    else:
        return 1 + shifty_shifts(start[1:], goal[1:], limit - 1)
    # END PROBLEM 6


def pawssible_patches(start, goal, limit):
    """A diff function that computes the edit distance from START to GOAL."""
    if start == goal:
        return 0
    if limit == 0:
        return 1
    if start == "":
        return len(goal)
    elif goal == "":
        return len(start)
    else:
        if start[0] == goal[0]:
            return pawssible_patches(start[1:], goal[1:], limit)
        else:
            add_diff = pawssible_patches(start, goal[1:], limit - 1) + 1
            rem_diff = pawssible_patches(start[1:], goal, limit - 1) + 1
            swa_diff = pawssible_patches(start[1:], goal[1:], limit - 1) + 1
            return min(add_diff, rem_diff, swa_diff)


def final_diff(start, goal, limit):
    """A diff function. If you implement this function, it will be used."""
    assert False, "Remove this line to use your final_diff function"


###########
# Phase 3 #
###########


def report_progress(typed, prompt, user_id, send):
    """Send a report of your id and progress so far to the multiplayer server."""
    # BEGIN PROBLEM 8
    "*** YOUR CODE HERE ***"
    tot = len(prompt)
    ri = 0
    ind = 0
    while ind < len(typed):
        if typed[ind] != prompt[ind]:
            break
        ind += 1
    ratio = ind / tot
    send({"id": user_id, "progress": ratio})
    return ratio
    # END PROBLEM 8


def fastest_words_report(times_per_player, words):
    """Return a text description of the fastest words typed by each player."""
    game = time_per_word(times_per_player, words)
    fastest = fastest_words(game)
    report = ""
    for i in range(len(fastest)):
        words = ",".join(fastest[i])
        report += "Player {} typed these fastest: {}\n".format(i + 1, words)
    return report


def time_per_word(times_per_player, words):
    """Given timing data, return a game data abstraction, which contains a list
    of words and the amount of time each player took to type each word.

    Arguments:
        times_per_player: A list of lists of timestamps including the time
                          the player started typing, followed by the time
                          the player finished typing each word.
        words: a list of words, in the order they are typed.
    """
    # BEGIN PROBLEM 9
    "*** YOUR CODE HERE ***"

    lent = len(times_per_player)
    k = 0
    times = []
    while k < lent:
        tem = []
        timep = times_per_player[k]
        for i in range(len(timep) - 1):
            tem += [timep[i + 1] - timep[i]]
        times += [tem]
        k += 1
    return game(words, times)
    # END PROBLEM 9


"""p = [[1, 4, 6, 7], [0, 4, 6, 9]]
words = ["This", "is", "fun"]
game = time_per_word(p, words)
game[0]"""


def fastest_words(game):
    """Return a list of lists of which words each player typed fastest.

    Arguments:
        game: a game data abstraction as returned by time_per_word.
    Returns:
        a list of lists containing which words each player typed fastest
    """
    player_indices = range(len(all_times(game)))  # contains an *index* for each player
    word_indices = range(len(all_words(game)))  # contains an *index* for each word
    # BEGIN PROBLEM 10
    "*** YOUR CODE HERE ***"
    ret = []
    for i in player_indices:
        tem = []
        ret += [tem]
    for i in word_indices:
        word = word_at(game, i)
        id = 0
        t = time(game, 0, i)
        for j in player_indices:
            tem = time(game, j, i)
            if t > tem:
                id = j
                t = tem
        ret[id] += [word]
    return ret

    # END PROBLEM 10


def game(words, times):
    """A data abstraction containing all words typed and their times."""
    assert all([type(w) == str for w in words]), "words should be a list of strings"
    assert all([type(t) == list for t in times]), "times should be a list of lists"
    assert all(
        [isinstance(i, (int, float)) for t in times for i in t]
    ), "times lists should contain numbers"
    assert all(
        [len(t) == len(words) for t in times]
    ), "There should be one word per time."
    return [words, times]


def word_at(game, word_index):
    """A selector function that gets the word with index word_index"""
    assert 0 <= word_index < len(game[0]), "word_index out of range of words"
    return game[0][word_index]


def all_words(game):
    """A selector function for all the words in the game"""
    return game[0]


def all_times(game):
    """A selector function for all typing times for all players"""
    return game[1]


def time(game, player_num, word_index):
    """A selector function for the time it took player_num to type the word at word_index"""
    assert word_index < len(game[0]), "word_index out of range of words"
    assert player_num < len(game[1]), "player_num out of range of players"
    return game[1][player_num][word_index]


def game_string(game):
    """A helper function that takes in a game object and returns a string representation of it"""
    return "game(%s, %s)" % (game[0], game[1])


enable_multiplayer = False  # Change to True when you're ready to race.

##########################
# Command Line Interface #
##########################


def run_typing_test(topics):
    """Measure typing speed and accuracy on the command line."""
    paragraphs = lines_from_file("data/sample_paragraphs.txt")
    select = lambda p: True
    if topics:
        select = about(topics)
    i = 0
    while True:
        reference = choose(paragraphs, select, i)
        if not reference:
            print("No more paragraphs about", topics, "are available.")
            return
        print("Type the following paragraph and then press enter/return.")
        print("If you only type part of it, you will be scored only on that part.\n")
        print(reference)
        print()

        start = datetime.now()
        typed = input()
        if not typed:
            print("Goodbye.")
            return
        print()

        elapsed = (datetime.now() - start).total_seconds()
        print("Nice work!")
        print("Words per minute:", wpm(typed, elapsed))
        print("Accuracy:        ", accuracy(typed, reference))

        print("\nPress enter/return for the next paragraph or type q to quit.")
        if input().strip() == "q":
            return
        i += 1


@main
def run(*args):
    """Read in the command-line argument and calls corresponding functions."""
    import argparse

    parser = argparse.ArgumentParser(description="Typing Test")
    parser.add_argument("topic", help="Topic word", nargs="*")
    parser.add_argument("-t", help="Run typing test", action="store_true")

    args = parser.parse_args()
    if args.t:
        run_typing_test(args.topic)
