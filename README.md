# Space Races
Space Races is game written in object-oriented Python, which can currently be played in full from the console. The web app designs are mobile-first but have yet to be implemented beyond a landing page.

The user is tasked with saving humanity on Earth by finding another suitable planet. It requires puzzle-solving in a choose-your-own-adventure style.

![LandingPage](https://res.cloudinary.com/dckkkjkuz/image/upload/v1664659706/space-races_landing_page_screenshot_without_tab_zcxbzt.png)

## To run this program
*The backend logic in Python is complete so game can be run from command line.*
* From command line: `python3 game.py`

## Technology & Dependencies
* Command line game: Python 3.12.7
* Hosted content: Node 22.12.0, Express 4.21.2

## Local Development
To verify landing page:
* Install dependencies: `npm install`
* Launch static assets locally: `open public/index.html` or `heroku local web --port 5001`
* Update dependencies: 
    * `npm i -g npm-check-updates`
    * `ncu  -u`
    * `npm install`


## Wireframe Samples

#### Selecting a Planet
![UnlockCoordinates](https://res.cloudinary.com/dckkkjkuz/image/upload/c_scale,w_400/v1509154912/space-races/SelectPuzzle.png)


#### Unlocking Planet 1 Coordinates
![SelectPlanet1](https://res.cloudinary.com/dckkkjkuz/image/upload/c_scale,w_400/v1509161143/space-races/UnlockPlanet1.png)


#### Unlocking Planet 3 Coordinates
![SelectPlanet3](https://res.cloudinary.com/dckkkjkuz/image/upload/c_scale,w_400/v1509154921/space-races/UnlockPlanet3.png)


See [development documents][docs] for all wireframes

[docs]: docs/


## Future Development
* Build out frontend with regular JavaScript so users can play the game on the web
