# ANGEL V DEMON

A command-line adventure/memory game for a solo player.

![Media Samples](/doc/readme-images/media-shots-crop.png "Media Samples")

## Development Staging

The program was developed in Python on gitpod, using the gitpod editor and 
python3 command.

The project began on [angel-v-demon-old repository](https://github.com/RobWar-code/angel-v-demon-old) 
on github/gitpod, which used the standard CI template, update/commit history can be viewed prior 
to the move.

It was then transferred to the angel-v-demon github/gitpod repository using the
necessary CI Template for the Heroku browser terminal.

Stage by stage commits were made, using the git version control system.

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

```python

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

```

Keywords may be linked to other words, so that the player can "learn"
what is associated with what.

A fairy could give a hint/clue for a word, if hints are included in the
templates or in a word dictionary.

Story Dictionary

```python

# Array of the following:
#       template_paragraph_num: integer
#       template_sentence_num: integer
#       angel_text: string
#       demon_text: string
#       ill_consequence: string
#       good_consequence: string
story_sentences = []

```

## Data Model

Each story is modelled as a class instance, by inheriting the story template
class, which has methods for handling the paragraph template dictionary.
The story itself is created as an instance at the start of each game.

The story class also provides the methods for keeping track of and presenting
each sentence to the user.

TemplateHandler

A class for creating paragraphs from templates

```python

class TemplateHandler:
    def __init__(self, template_paras, max_differences_per_sentence):
        self.template_paragraphs = template_paras
        self.token_list = []
        self.max_differences_per_sentence = max_differences_per_sentence

	def clear_self():
	
	def get_num_paragraphs():

	def get_sentence_texts():

	def _get_single_sentence_text():

	def _get_angel_and_demon_text():

	def _get_token()

	def _set_token()

	def _get_word_diff_list()

	

```

StoryHandler

To generate and retain a specific story created by the template
handler. Methods for accessing the completed story.

```python

    class StoryHandler(TemplateHandler):
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

		def _clear():

		def reset():

		def create_story():

		def print_angel_story():

		def print_demon_current_sentence():

		def print_demon_previous_sentence():

		def print_good_consequence():

		def print_ill_consequence():

		def test_angel_substitutes():

		def wrap_and_print():

```

## Libraries Used

- math - integer and floating point conversion
- random - sampling and selection
- platform - to determine os command to use
- os - for the console clear operation
- time - to set timer for game and for time dependent display of story
- re - for matching validity of text entered
- colorama - screen text colors
- textwrap - to adjust text to line width

## Background Documentation

Further documentation is provided in the /doc directory.

The project analysis and flow-diagram appear in [project-analysis](/doc/project-analysis.txt)

Work progress appears in [work-log](/doc/work-log.txt)

## Deployment
Code Institute has provided a [template](https://github.com/Code-Institute-Org/python-essentials-template) to display the terminal view of this backend application in a modern web browser. This is to improve the accessibility of the project to others.

The live deployed application can be found deployed on [Heroku](https://angel-v-demon.herokuapp.com/).

### Local Deployment

*Gitpod* IDE was used to write the code for this project.

You can clone the repository by following these steps:

1. Go to the [GitHub repository](https://github.com/RobWar-code/angel-v-demon) 
2. Locate the Code button above the list of files and click it 
3. Select if you prefer to clone using HTTPS, SSH, or GitHub CLI and click the copy button to copy the URL to your clipboard
4. Open Git Bash or Terminal
5. Change the current working directory to the one where you want the cloned directory
6. In your IDE Terminal, type the following command to clone my repository:
	- `git clone https://github.com/RobWar-code/angel-v-demon.git`
7. Press Enter to create your local clone.

Alternatively, if using Gitpod, you can click below to create your own workspace using this repository.

[![Open in Gitpod](https://gitpod.io/button/open-in-gitpod.svg)](https://gitpod.io/#https://github.com/RobWar-code/angel-v-demon)

Please note that in order to directly open the project in Gitpod, you need to have the browser extension installed. A tutorial on how to do that can be found [here](https://www.gitpod.io/docs/configure/user-settings/browser-extension).

### Heroku Deployment

This project uses [Heroku](https://www.heroku.com), a platform as a service (PaaS) that enables developers to build, run, and operate applications entirely in the cloud.

Deployment steps are as follows, after account setup:

- Select *New* in the top-right corner of your Heroku Dashboard, and select *Create new app* from the dropdown menu.
- Your app name must be unique, and then choose a region closest to you (EU or USA), and finally, select *Create App*.
- From the new app *Settings*, click *Reveal Config Vars*, and set the value of KEY to `PORT`, and the value to `8000` then select *add*.
- Further down, to support dependencies, select *Add Buildpack*.
- The order of the buildpacks is important, select `Python` first, then `Node.js` second. (if they are not in this order, you can drag them to rearrange them)

Heroku needs two additional files in order to deploy properly.
- requirements.txt
- Procfile

You can install this project's requirements (where applicable) using: `pip3 install -r requirements.txt`. If you have your own packages that have been installed, then the requirements file needs updated using: `pip3 freeze --local > requirements.txt`

The Procfile can be created with the following command: `echo web: node index.js > Procfile`

For Heroku deployment, follow these steps to connect your GitHub repository to the newly created app:

- In the Terminal/CLI, connect to Heroku using this command: `heroku login -i`
- Set the remote for Heroku: `heroku git:remote -a <app_name>` (replace app_name with your app, without the angle-brackets)
- After performing the standard Git `add`, `commit`, and `push` to GitHub, you can now type: `git push heroku main`

The frontend terminal should now be connected and deployed to Heroku.

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

For the following systems tests, see: [Systems Tests](/SYSTEMS_TESTS.md)

Responsiveness

Browser Compatibility

Code Test

Systems Tests


## Credits
CI Code Institute - The web browser terminal
