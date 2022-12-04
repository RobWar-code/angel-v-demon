# ANGEL V DEMON

A command-line adventure/memory game for a solo player.

![Media Samples](/doc/readme-images/media-shots-crop.png "Media Samples")

## How To Play

To start the game, the player is presented with a short story (by an angel) 
about a knight. The player is given a limited amount of time to memorise
this and is then presented with each line of the story with one or more
words altered (by a "demon") which he is to correct by entering the words
to be altered and their replacements. The player is given a score if
they successfully complete the correct story. A fairy may intervene
to offer the player another chance in the case of error.

At the end of each game the player is offered a chance to play the game
with the same story (if the player failed) or to start a new game.

## Features

The line width for the display is now taken to be 40 characters, to allow
for mobiles.

The game can be played at 4 skill levels, and stories can have one to four
paragraphs.

Stories are generated at random from template paragraphs which have multiple
choices of alternative words. Furthermore, paragraphs may be given in the story
in any arrangement.

The words chosen by the "demon" are selected from the possible substitutions at
random.

During any session a track is kept of the high-score which is presented
with the users score when a game is won.

Keyboard input is validated and input requests re-presented where necessary
for the flow of the game. These inputs are tested as in Systems Tests below.

## Future Features
Additional template paragraphs can be added.

Keywords may be linked to other words, so that the player can "learn"
what is associated with what.

A fairy could give a hint/clue for a word, if hints are included in the
templates or in a word dictionary.

## Data Model

Each story is modelled as a class instance, by inheriting the story template
class, which has methods for handling the paragraph template dictionary.
The story itself is created as an instance at the start of each game.

The story class also provides the methods for keeping track of and presenting
each sentence to the user.

## Background Documentation

Further documentation is provided in the /doc directory.

The project analysis and flow-diagram appear in /doc/project-analysis.txt


## Testing 

Each input has been manually tested as in Systems Tests below.

## Development Staging

The program was developed in Python on gitpod, using the gitpod editor and 
python3 command.

The project began on angel-v-demon-old repository on github/gitpod, which used the
standard CI template.

It was then transferred to the angel-v-demon github/gitpod repository using the
necessary CI Template for the Heroku browser terminal.

Stage by stage commits were made, using the git version control system.

## Deployment
Set-up was from the CI gitpod template for heroku web terminal.
To link-up the python app to the web-page run simulation:
1. Logon to the Heroku.com site
2. Go to the dashboard
3. Click on Create App
4. Click on Settings
5. Click on Config Vars
6. Set Key: PORT, Value: 8000
7. Click on Deploy tab
8. Click on Connect to GitHub
9. connect to angel-v-demon
10. Click on Automatic Deploy
11. Click on Manual Deploy
12. Click on View when it appears, to ensure this is working

The browser implementation can be found at:

[Browser App](https://angel-v-demon.herokuapp.com/ "Browser App")

## Credits
CI Code Institute - The web browser terminal

## Screen Shots

Heroku Client Introduction

![Heroku Client Introduction](/doc/readme-images/introduction-heroku.png "Heroku Client Introduction")

Heroku Client Instructions

![Heroku Client Instructions](/doc/readme-images/instructions-heroku.png "Heroku Client Instructions")

Heroku Client Game Start

![Heroku Client Game Start](/doc/readme-images/game-start-heroku.png "Heroku Client Game Start")

## Systems Tests
### Game Start Texts

* Introduction Text

![Introduction Text](/doc/readme-images/introduction-crop.png "Introduction Text")

* Instruction Text

![Instructions Text](/doc/readme-images/instructions-crop.png "Instructions Text")

### Input Point Tests
All input tests are performed on game 1 paragraph, player level 1.
The Inn references relate to points on the flow-chart in 
doc/project-analysis.txt

Items completed are marked with * and screen shots given where
appropriate.

I01 Continue from introduction

a. * Ensure input prompt is clearly understandable

b. * Check response to garbage input

c. N/A Check input validation

d. * Check for availability of the quit option

e. * Check that the logic flows correctly from the inputs

![I01 Introduction](/doc/readme-images/introduction-crop.png "I01 introduction")

I02 Continue from instructions

a. * Ensure input prompt is clearly understandable

b. * Check response to garbage input

c. N/A Check input validation

d. * Check for availability of the quit option

e. * Check that the logic flows correctly from the inputs

![I02 Instructions](/doc/readme-images/instructions-crop.png)

I03 Input number of paragraphs

a. * Ensure input prompt is clearly understandable

b. * Check response to garbage input

c. * Check input validation

d. * Check for availability of the quit option

e. * Check that the logic flows correctly from the inputs

Prompt for number of paragraphs

![I03 Number of Paragraphs](/doc/readme-images/i03-crop.png "I03 Number of Paragraphs")

Garbage entered

![I03 garbage entered](/doc/readme-images/i03-garbage-crop.png "I03 garbage entered")

Invalid Number

![I03 invalid number](/doc/readme-images/i03-invalid-number-crop.png "I03 invalid number")

I04 Input player level

a. * Ensure input prompt is clearly understandable

b. * Check response to garbage input

c. * Check input validation

d. * Check for availability of the quit option

e. * Check that the logic flows correctly from the inputs

![I04 Input player level](/doc/readme-images/i04-crop.png "I04 Input player level")

Input garbage

![I04 Input garbage](/doc/readme-images/i04-garbage-crop.png "I04 Input garbage")

Input invalid number

![I04 Input invalid number](/doc/readme-images/i04-invalid-number-crop.png "I04 Input invalid number")

Logic flow from valid player level

![I04 Valid logic flow](/doc/readme-images/i04-logic-flow-crop.png "I05 Valid logic flow")

I05 Input for replacement words

a. * Ensure input prompt is clearly understandable

b. * Check response to garbage input

c. * Check input validation

d. * Check for availability of the quit option

e. Check that the logic flows correctly from the inputs

    * Correct Answer

        * General
            Bug: word_loop() while condition not cancelled
            Fix: inserted else and reset flag

        * End of Paragraph

        * End of Game

    Incorrect Answer

        * Another Chance
            Bug: word_loop() fairy-count not found
            Fix: pass and return the fairy_count variable from the calling function
            Bug: word_loop() math.random() does not exist
            Fix: use random.random()
            Bug: sentence_loop() invalid use of . notation for dict reference
            Fix: used bracketed notation ["xx"]

        * Fairy Saves Life

            * Continue to next sentence

            * End of Game

        Knight Fails
            Bug: story_template.py print_ill_consequence() misspelled variable name
            Fix: corrected spelling

Enter Correction

![I05 Enter Correction](/doc/readme-images/i05-crop.png "I05 Enter Correction")

Correct Answer

![I05 Correct Answer](/doc/readme-images/i05-correct-answer-crop.png "I05 Correct Answer")

Fairy Saves Life after Incorrect Answer

![I05 Fairy Saves Life](/doc/readme-images/i05-fairy-saves-life-crop.png "I05 Fairy saves life")

Garbage entered

![I05 Garbage Entered](/doc/readme-images/i05-garbage-crop.png "I05 Garbage Entered")

Incorrect answer, another chance

![I05 Incorrect - Another Chance](/doc/readme-images/i05-incorrect-other-chance-crop.png "I05 Incorrect - Another Chance")

Invalid Inputs

![I05 Invalid Input Sample 1](/doc/readme-images/i05-invalid-01-crop.png "I05 Invalid Input Sample 1")

![I05 Invalid Input Sample 2](/doc/readme-images/i05-invalid-02-crop.png "I05 Invalid Input Sample 2")

Paragraph Correct

![I05 Paragraph Correct](/doc/readme-images/i05-paragraph-correct-crop.png "I05 Paragraph Correct")

Player Wins 1

![I05 Player Wins](/doc/readme-images/i05-win-crop.png "I05 Player Wins")

Player Wins 2

![I05 Player Wins 2](/doc/readme-images/i05-win-2-crop.png "I05 Player Wins 2")

I06 Input repeat same game

a. * Ensure input prompt is clearly understandable

b. * Check response to garbage input

c. N/A Check input validation

d. * Check for availability of the quit option

e. * Check that the logic flows correctly from the inputs

    Bug: story.print_demon_current_sentence() list index out of range
    Fix: add a reset function to StoryHandler and call from replay in repeat_game_loop()

![I06 Play game again](/doc/readme-images/i06-crop.png "I06 Play game again")

I07 Input start another game

a. * Ensure input prompt is clearly understandable

b. * Check response to garbage input

c. N/A Check input validation

d. * Check for availability of the quit option

e. * Check that the logic flows correctly from the inputs

    Bug: New stories doubled
    Fix: story_template.py StoryHandler.create_story() clear down story list

![I07 Start new game](/doc/readme-images/i07-crop.png "I07 Start new game")

I08 Input start another game - from I05 win

*a. Ensure input prompt is clearly understandable

*b. Check response to garbage input

*c. Check input validation

*d. Check for availability of the quit option

*e. Check that the logic flows correctly from the inputs

### Random Branch Point Tests
    See: I05

### Playability Tests

Apart from the functionality of the inputs tested above, we need
to check that the time which the user is given to memorise the
text is believable. This is about 8 seconds for one paragraph
at level 4 (the most difficult), just enough for a couple of quick scans.
