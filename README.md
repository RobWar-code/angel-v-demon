# ANGEL V DEMON

A command-line adventure/memory game for a solo player.

![Media Samples](/doc/readme-images/media-shots-crop.png "Media Samples")

## User Considerations

Any end-user who would like to play an adventure or memory game with a 
simple command-line interface.

The game provides the user with a slightly different story at each play.
To allow for added interest and abilities the game can be played at
different skill levels.

Both score and high score are reported for a player win, to allow
the player to gauge their performance.

All user inputs are clearly explained and checked for validity, with
errors reported clearly to the user.

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

Template is as follows:

///python

		template_paragraphs = [
			[
				{  # First Sentence

					main_sentence: {
						template: "words .. ? .. ?",
						alternatives: [ 
							{	
								definitive_id: "",  # string "" if n/a
								acquired_id: "",  # string "" if n/a
								opts: [],  # [string, ...]
							}
							...
						]
					},
					ill_consequence: {
					# template as above
					}
				},
				# ...,
				{  # Final Sentence
					main_sentence: {
						template: "words .. ? .. ?"
						alternatives: [ 
							{	
								definitive_id:  # string "" if n/a
								acquired_id:  # string "" if n/a
								opts:  # [string, ...]
							}
							# ...
						]
					},
					good_consequence: {
						# template as above
					}
					ill_consequence: {
						# template as above
					}
				}
			],
			# ...
		]

///
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

TemplateHandler

///python

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
///

StoryHandler

///python

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

///

## Libraries Used

math - integer and floating point conversion
random - sampling and selection
platform - to determine os command to use
os - for the console clear operation
time - to set timer for game and for time dependent display of story
re - for matching validity of text entered
textwrap - to adjust text to line width

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

## Tools and Technologies

- [python](https://www.python.org ) - used for the project code
- [heroku](https://heroku.com) - used for linking the app to the browser
- [CI Code Institute Template](https://github.com/Code-Institute-Org/python-essentials-template) - the github/gitpod template
- [Gitpod](https://gitpod.io/) - used as the cloud-based IDE for development
- [Git](https://git-scm.com/) - used for version control and commits
- [GitHub](https://github.com/) - used as secure online storage of code
- [GIMP](https://www.gimp.org/) - used for image cropping and resizing

## Screen Shots

Heroku Client Introduction

![Heroku Client Introduction](/doc/readme-images/introduction-heroku.png "Heroku Client Introduction")

Heroku Client Instructions

![Heroku Client Instructions](/doc/readme-images/instructions-heroku.png "Heroku Client Instructions")

Heroku Client Game Start

![Heroku Client Game Start](/doc/readme-images/game-start-heroku.png "Heroku Client Game Start")

## Systems Tests

see: [Systems Tests](/SYSTEMS_TESTS.md)

## Credits
CI Code Institute - The web browser terminal
