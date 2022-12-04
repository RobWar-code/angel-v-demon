"""
    angel-v-demon
    Author: Robin Warner November 2022

    A command-line game for one player, presenting a story to be memorised by
    the player, and re-presented line by line with modifications for the
    player to correct.
"""
import math
import random
import platform
import os
import time
from re import fullmatch
from textwrap import wrap
from template_data import template_paragraphs

# Globals
LINE_WIDTH = 40  # To allow for display on mobiles
story = None
hi_score = 0


def main():
    """
        User interaction loops
        New game loop
    """

    global story

    # Introduce the game
    display_introduction()
    games_ended = False
    while not games_ended:
        display_instructions()
        # Get number of paragraphs
        num_paragraphs = enter_num_paras()
        # Get player level
        player_level = enter_player_level()
        # Determine play parameters
        start_num_fairies = (4 - player_level) * num_paragraphs
        expected_time_per_sentence = 20 / player_level
        max_differences_per_sentence = player_level
        # Set-up story object
        story = StoryHandler(
            template_paragraphs,
            num_paragraphs,
            max_differences_per_sentence,
            story_sentences, LINE_WIDTH)

        story.create_story()
        # Repeat game loop
        new_game = repeat_game_loop(num_paragraphs, player_level,
                                    expected_time_per_sentence,
                                    start_num_fairies)
        if not new_game:
            games_ended = True


def repeat_game_loop(num_paragraphs, player_level, expected_time_per_sentence,
                     start_num_fairies):
    """
        First and subsequent loops for the player to
        try the same game again
    """

    game_repeat_finished = False
    while not game_repeat_finished:
        # Print the angel's story
        print()
        print("ANGEL'S STORY")
        print()
        story.print_angel_story()
        # Display Count Down Loop
        # Determine total display time
        time_limit = math.floor(
            expected_time_per_sentence * num_paragraphs * 3 / 2)
        display_timer(time_limit)
        # Clear the display
        if platform.system() == "Windows":
            os.system("cls")
        else:
            os.system("clear")

        # Do the demon's sentence display
        game_opts = sentence_loop(num_paragraphs, player_level,
                                  start_num_fairies,
                                  expected_time_per_sentence)
        if not game_opts["replay"]:
            game_repeat_finished = True
        else:
            story.reset()

    return game_opts["new_game"]


def sentence_loop(num_paragraphs, player_level, start_num_fairies,
                  expected_time_per_sentence):
    """
        Presentation of each demon's sentence and user's responses
    """
    global hi_score

    fairy_count = start_num_fairies
    paragraph_count = 0
    got_sentence = True
    failed = False
    new_game = False
    replay = False
    # Set the time counter for scoring
    time_start = math.ceil(time.time())
    while not failed and got_sentence:
        # Print the next demon's sentence
        print("The Demon says:-")
        paragraph_end = story.print_demon_current_sentence()
        if paragraph_end:
            paragraph_count += 1
        # Get and check user corrections
        word_loop_ret = word_loop(fairy_count)
        failed = word_loop_ret["failed"]
        fairy_count = word_loop_ret["fairy_count"]

        if (paragraph_end and not failed):
            # Print the consequence
            print("The angel cheers:- ")
            story.print_good_consequence()
            if paragraph_count >= num_paragraphs:
                got_sentence = False
        elif not paragraph_end and not failed:
            print("Correct")

    if failed:
        user_input = input("Enter Y to replay game else ENTER: \n")
        if user_input == "Q" or user_input == "q":
            raise SystemExit()
        if user_input == "Y" or user_input == "y":
            replay = True
        else:
            user_input = input("Enter Y to play a new game else ENTER: \n")
            if user_input == "Q" or user_input == "q":
                raise SystemExit()
            if user_input == "Y" or user_input == "y":
                new_game = True

    else:
        print("The crowd cheers - YOU WIN")
        # Calculate Score
        time_end = math.ceil(time.time())
        diff_time = time_end - time_start
        target = num_paragraphs * 3 * expected_time_per_sentence
        score = player_level * (200 + target - diff_time)
        score_string = "Your Score is: " + str(score)
        if hi_score > 0:
            score_string += " High Score was: " + str(hi_score)
        if score > hi_score:
            hi_score = score
        print()
        print(score_string)

        # Offer of new game
        print()
        user_input = input("Play another game Y or Q to quit: \n")
        if user_input == "Y" or user_input == "y":
            new_game = True
        else:
            raise SystemExit()

    return {"new_game": new_game, "replay": replay}


def word_loop(fairy_count):
    """
        User response to demon's sentences and options arising
    """
    try_again = True
    while try_again:
        # Get user replacement words
        failed = get_user_corrections()
        if failed:
            print("WRONG - The demon chuckles..")
            if fairy_count > 0:
                fairy_count = fairy_count - 1
                # The fairy intervenes
                if random.random() < 0.5:
                    print()
                    print("A fairy gives you another chance:")
                    story.print_demon_previous_sentence()
                else:
                    print()
                    print("A fairy saves the knight's life")
                    print()
                    try_again = False
                    failed = False
            else:
                story.print_ill_consequence()
                try_again = False
        else:
            try_again = False

    return {"failed": failed, "fairy_count": fairy_count}


def get_user_corrections():
    """
        User input of corrections to demon's sentence. Validation of input.
    """
    invalid = True
    failed = False
    while invalid:
        print()
        user_input = input("Enter corrections: \n")
        if user_input == "Q" or user_input == "q":
            raise SystemExit()
        # Check the input against the angel's sentence
        result = story.test_angel_substitutes(user_input)
        if result == "match":
            invalid = False
        elif result == "no match":
            invalid = False
            failed = True
        else:
            print("Invalid corrections, use red=blue bear=angel etc")

    return failed


def display_timer(time_limit):
    """
        Display a numeric count-down timer for time_limit seconds
    """
    print()
    print("Count Down: ", end="")
    display_time = str(time_limit).zfill(3)
    print(display_time, end="")
    while time_limit > 0:
        time.sleep(1)
        time_limit -= 1
        display_time = str(time_limit).zfill(3)
        print("\b\b\b" + display_time, end="", flush=True)
        time_limit -= 1
    print()


def display_introduction():
    """
        Display the general introduction to the game
    """
    print("Welcome to Angel v Demon!")
    print()
    print("""In this game, you are presented with a
story written for a bold knight by an
angel. However, before the knight can
receive his fate, a demon seizes the
copy and modifies some words on each
line. Your mission is to restore it to
its original form line by line and
save the knight ...""")
    print()
    user_input = input("Click ENTER key to continue - Q to quit: \n")
    if user_input == "Q" or user_input == "q":
        raise SystemExit()


def display_instructions():
    """
        Display the general instructions for the game
    """
    print()
    print("INSTRUCTIONS")
    print()
    print("""At the start of the game you will be
presented with the angel's version of
the story. You will have a certain
amount of time to read and memorise it.""")
    print()
    print("""After this you will be presented with
the demon's version of the sentences in
order, one at a time and will be
prompted to enter the corrections with
each.""")
    print()
    print("""On a single line, for each correction
that you recall, type in the word to be
replaced, then an equals sign, then the
word to replace it. For Example:""")
    print()
    print("red=blue bear=dragon")
    print()
    print("You can leave the games any time by\nentering Q")
    user_input = input("ENTER to continue, Q to quit: \n")
    if user_input == "Q" or user_input == "q":
        raise SystemExit()


def enter_num_paras():
    """
        Collect the number of paragraphs for the story from the user
    """
    invalid = True
    while invalid:
        print()
        user_input = input("""Please enter number of paragraphs for
the story (1 to 4): \n""")
        if user_input == "Q" or user_input == "q":
            raise SystemExit()
        if len(user_input) != 1:
            print("Value entered was not valid")
        elif user_input not in "1234":
            print("Number not valid")
        else:
            n = int(user_input)
            invalid = False
    return n


def enter_player_level():
    """
        Collect the player difficulty level from the user
    """
    invalid = True
    while invalid:
        print()
        user_input = input("""Please enter player level
(1 to 4, 1 easiest): \n""")
        if user_input == "Q" or user_input == "q":
            raise SystemExit()
        if len(user_input) != 1:
            print("Value entered was not valid")
        elif user_input not in "1234":
            print("Number not valid")
        else:
            n = int(user_input)
            invalid = False
    return n

# Class Definitions


class TemplateHandler:
    """
        Methods for handling the sentence and paragraph template
        data to generate variable stories.

        Add in the template_paragraphs dictionary
        and declare the token list
    """
    def __init__(self, template_paras, max_differences_per_sentence):
        self.template_paragraphs = template_paras
        self.token_list = []
        self.max_differences_per_sentence = max_differences_per_sentence

    def clear(self):
        """
            Clear the list of tokens and their values
        """
        self.token_list = []

    def get_num_paragraphs(self):
        """
            Get the total number of paragraphs in the story template
        """
        return len(self.template_paragraphs)

    def get_sentence_texts(self, paragraph_num, sentence_num):
        """
            Collect the angel and demon versions of a sentence as well as
            the good and ill consequence sentences
        """
        # Get the angel's and demon's versions of the main sentence
        dual_text = self._get_angel_and_demon_text(paragraph_num, sentence_num)
        sentence_data = self.template_paragraphs[paragraph_num][sentence_num]
        ill_consequence = ""
        if sentence_data["ill_consequence"]:
            ill_consequence = self._get_single_sentence_text(
                sentence_data["ill_consequence"], False)
        good_consequence = ""
        if sentence_data["good_consequence"]:
            good_consequence = self._get_single_sentence_text(
                sentence_data["good_consequence"], True)
            # This is the final sentence of the paragraph, so clear tokens
            self.clear()

        return {
            "angel_text": dual_text[0],
            "demon_text": dual_text[1],
            "ill_consequence": ill_consequence,
            "good_consequence": good_consequence
        }

    def _get_single_sentence_text(self, sentence_data, is_angel):
        """
            Perform the word substitutions for either the demon or the angel
        """
        out_text = sentence_data["template"]
        alternatives = sentence_data["alternatives"]
        # Perform each substitution
        for alt in alternatives:
            word = ""
            # Check whether a token
            if alt["acquired_id"]:
                word = self._get_token(alt["acquired_id"], is_angel)
            else:
                word = random.choice(alt["options"])
            # Insert the word
            out_text = out_text.replace("?", word, 1)

        return out_text

    def _get_angel_and_demon_text(self, paragraph_num, sentence_num):
        """
            Perform the word substitutions for both angel and demon to
            produce two sentences
        """
        angel_text = ""
        demon_text = ""
        p = paragraph_num
        s = sentence_num
        sentence_data = self.template_paragraphs[p][s]['main_sentence']
        demon_text = sentence_data["template"]
        angel_text = sentence_data["template"]
        # Get set of word numbers in which the demon's choice is to be
        # different
        word_diff_list = []
        word_diff_list = self._get_word_diff_list(sentence_data["template"])
        # For each alternative word option
        count = 0
        diff_count = 0
        for alt in sentence_data["alternatives"]:
            demon_word = ""
            angel_word = ""
            # Check whether this is a token to be re-used
            if alt["acquired_id"] != "":
                demon_word = self._get_token(alt["acquired_id"], False)
                angel_word = self._get_token(alt["acquired_id"], True)
            else:
                # Select the words from the list of alternatives
                word_choice = random.sample(alt["options"], 2)
                if alt["definitive_id"] != "":
                    self._set_token(alt["definitive_id"], word_choice)
                angel_word = word_choice[0]
                demon_word = word_choice[1]

            # Assign the words to the relevant sentences
            angel_text = angel_text.replace("?", angel_word, 1)
            # Check whether the demon's choice is different
            if diff_count < len(word_diff_list):
                if count == word_diff_list[diff_count]:
                    demon_text = demon_text.replace("?", demon_word, 1)
                    diff_count += 1
                else:
                    demon_text = demon_text.replace("?", angel_word, 1)
            else:
                demon_text = demon_text.replace("?", angel_word, 1)

            count += 1

        return [angel_text, demon_text]

    def _set_token(self, token_name, values):
        """
            Insert a token into the token list. This contains both the
            angel's and the demon's values
        """
        token_obj = [token_name, values[0], values[1]]
        self.token_list.append(token_obj)

    def _get_token(self, token_name, is_angel):
        """
            Search and get the token (angel or demon value) from the token
            list
        """
        for token in self.token_list:
            if token[0] == token_name:
                value = token[1] if is_angel else token[2]
                return value
        # If token not found, then this is an error
        print(f"_get_token: token not found: {token_name}")
        raise SystemExit()

    def _get_word_diff_list(self, template_text):
        """
            Get list of template word replacement numbers that are
            to be different between angel and demon
        """
        num_substitutes = template_text.count("?")
        num_list = list(range(num_substitutes))
        # Select the word numbers to change
        if num_substitutes <= self.max_differences_per_sentence:
            return num_list

        # Otherwise, choose a subset and order it
        num_list = random.sample(num_list,
                                 self.max_differences_per_sentence)
        num_list.sort()
        return num_list


# -------------------------------------------------------------------------


class StoryHandler(TemplateHandler):
    """
        Handler to generate and retain a specific story created by the
        template handler. Methods for accessing the completed story
    """
    def __init__(self, template_paras, num_paragraphs,
                 max_differences_per_sentence, story_sents, line_width):
        """
            Assign the initial data
        """
        # Set-up the template object
        super().__init__(template_paras,
                         max_differences_per_sentence)
        self.num_paragraphs = num_paragraphs
        self.story_sentences = story_sents
        self.story_created = False
        self.current_sentence_num = 0
        self.line_width = line_width

    def _clear(self):
        self.story_sentences = []
        self.reset()

    def reset(self):
        """
            Do settings to start or restart story
        """
        self.current_sentence_num = 0

    def create_story(self):
        """
            Create a story from the template and append sentence data to
            the story_sentences dictionary
        """
        # Clear any existing story
        self._clear()
        # Get the list of template paragraph numbers to use
        num_template_paras = super().get_num_paragraphs()
        para_list = []
        for _ in range(self.num_paragraphs):
            para_list.append(random.randint(0, num_template_paras - 1))
        # Get the paragraphs and build the story data
        for para_num in para_list:
            para_finished = False
            sentence_num = 0
            while not para_finished:
                sentence_data = {}
                sentence_data["template_paragraph_num"] = para_num
                sentence_data["template_sentence_num"] = sentence_num
                sentence_data = super().get_sentence_texts(
                    para_num, sentence_num)
                self.story_sentences.append(sentence_data)
                if sentence_data["good_consequence"]:
                    para_finished = True
                sentence_num += 1
        self.story_created = True

    def print_angel_story(self):
        """
            Print the angel's version of the story
        """
        for sentence_data in self.story_sentences:
            # Get text and wrap it to line width
            self.wrap_and_print(sentence_data["angel_text"])
            if sentence_data["good_consequence"]:
                self.wrap_and_print(sentence_data["good_consequence"])
                print()

    def print_demon_current_sentence(self):
        """
            Display the demon's version of the  current sentence
        """
        paragraph_end = False
        sentence_data = self.story_sentences[self.current_sentence_num]
        self.wrap_and_print(sentence_data["demon_text"])
        if sentence_data["good_consequence"]:
            paragraph_end = True
        self.current_sentence_num += 1
        return paragraph_end

    def print_demon_previous_sentence(self):
        """
            Display the same demon's version of the sentence again
        """
        sentence_data = self.story_sentences[self.current_sentence_num - 1]
        self.wrap_and_print(sentence_data["demon_text"])

    def print_good_consequence(self):
        """
            Display the good consequence sentence arising from the current
            sentence
        """
        sentence_data = self.story_sentences[self.current_sentence_num - 1]
        self.wrap_and_print(sentence_data["good_consequence"])

    def print_ill_consequence(self):
        """
            Display the ill consequence sentence arising from the current
            sentence
        """
        sentence_data = self.story_sentences[self.current_sentence_num - 1]
        self.wrap_and_print(sentence_data["ill_consequence"])

    def test_angel_substitutes(self, subs):
        """
            Check the substitution string entered by the user as a string of
            " red=blue ..." against the (angel's) sentence displayed (previous)
            returns one of:
                "invalid"
                "match"
                "no match"
        """
        sub_list = subs.split()
        if len(sub_list) == 0:
            return "invalid"
        # Check each term for errors
        for term in sub_list:
            if term.count("=") != 1:
                return "invalid"
            terms = term.split("=")
            if len(terms) != 2:
                return "invalid"
            for i in range(2):
                if fullmatch("^[a-z]+$", terms[i]) is None:
                    return "invalid"

        # Loop through each term and make substitutions
        n = self.current_sentence_num - 1
        demon_text = self.story_sentences[n]["demon_text"]
        angel_text = self.story_sentences[n]["angel_text"]
        for term in sub_list:
            terms = term.split("=")
            demon_word = terms[0]
            angel_word = terms[1]
            # Replace the demon word in the demon text by the angel word
            demon_text = demon_text.replace(demon_word, angel_word)

        # Compare with angel's sentence
        if demon_text != angel_text:
            return "no match"
        return "match"

    def wrap_and_print(self, text):
        """
            Wrap the text string at the set width and print it
        """
        w = wrap(text, self.line_width)
        for s in w:
            print(s)


# ------------------------------------------------------------------------
# Array of the following:
#       template_paragraph_num: integer
#       template_sentence_num: integer
#       angel_text: string
#       demon_text: string
#       ill_consequence: string
#       good_consequence: string
story_sentences = []

# Call to user-interaction loop
main()
