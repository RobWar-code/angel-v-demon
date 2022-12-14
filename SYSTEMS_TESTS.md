## Responsiveness Tests

1000px

![1000px Introduction](/doc/readme-images/media-test-1000-a.png "1000px Introduction")

![1000px Instructions](/doc/readme-images/media-test-1000-b.png "1000px Instructions")

![1000px Story](/doc/readme-images/media-test-1000-c.png "1000px Story")

400px

![400px Introduction](/doc/readme-images/media-test-400-a.png "400px Introduction")

![400px Instructions](/doc/readme-images/media-test-400-b.png "400px Instructions")

![400px Story](/doc/readme-images/media-test-400-c.png "400px Story")

## Browser Compatibility

Chrome

![Chrome Browser View](/doc/readme-images/browser-chrome.png "Chrome Browser View")

Edge

![Edge Browser View](/doc/readme-images/browser-edge.png "Edge Browser View")

Firefox

![Firefox Browser View](/doc/readme-images/browser-firefox.png "Firefox Browser View")

Opera

![Opera Browser View](/doc/readme-images/browser-opera.png "Opera Browser View")

## Python PEP8 Linter Test

[Test Platform](https://pep8ci.herokuapp.com)

Main Module run.py

![Main Module Lint](/doc/readme-images/python_lint_run.png "Python Lint Main Module")

Template Module

![Template Module Lint](/doc/readme-images/python_lint_para_template.png "Template Module Lint")

## Systems Tests

For the flowchart with the input points (i01 etc) see [Project Analysis](/doc/project-analysis.txt)

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
    Continues as for Enter

c. N/A Check input validation

d. * Check for availability of the quit option

e. * Check that the logic flows correctly from the inputs

![I01 Introduction](/doc/readme-images/introduction-crop.png "I01 introduction")

Quit Option

![I01 Quit](/doc/readme-images/i01-quit-crop.png "I01 Quit Option")

I02 Continue from instructions

a. * Ensure input prompt is clearly understandable

b. * Check response to garbage input

c. N/A Check input validation

d. * Check for availability of the quit option

e. * Check that the logic flows correctly from the inputs

![I02 Instructions](/doc/readme-images/instructions-crop.png "I02 Instructions")

Quit Option

![I02 Quit](/doc/readme-images/i02-quit-crop.png "I02 Quit")

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

Bug: Printed message cleared immediately after print

Fix: Add sleep

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

Bug: Key Enter does not display quit message
Fix: Enter call to quit_game function

a. * Ensure input prompt is clearly understandable

b. * Check response to garbage input

c. N/A Check input validation

d. * Check for availability of the quit option

e. * Check that the logic flows correctly from the inputs

    Bug: New stories doubled
    Fix: story_template.py StoryHandler.create_story() clear down story list

![I07 Start new game](/doc/readme-images/i07-crop.png "I07 Start new game")

Quit Option

![I07 Quit Option](/doc/readme-images/i07-quit-crop.png "I07 Quit Option")

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
