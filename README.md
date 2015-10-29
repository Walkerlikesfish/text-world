Installing Python
---------------------

First install [Python](https://www.python.org/). Linux users should
have it in their repositories, Windows/Mac users can get it from the
Python homepage. You need the 2.7.x version (Python 3 is not yet
supported). Windows users, make sure to select the option to make
Python available in your path - this is so you can call it everywhere
as `python`. Python 2.7.9 and later also includes the
[pip](https://pypi.python.org/pypi/pip/) installer out of the box,
otherwise install this separately (in linux it's usually found as the
`python-pip` package).


Setting up games
---------------------
1. Clone this repository.
2. Run `pip install -e .` 
(note the period "." at the end, this tells pip to install from the
current directory). This will install Evennia and all its dependencies and make the `evennia`
command available on the command line. You can find Evennia's
dependencies in `evennia/requirements.txt`.  
3. Change directory using `cd evennia/`.  
4. Run `start.sh <n>` to start up `n` different game servers - each server will use a different port.   
During server start, you will be asked to provide username and password - make sure this matches the framework code
(the defaults are root and root for both username and password)  
5. Use `telnet localhost <gameport>` to connect to the game server. The default game ports start from 4001 for the first game server, 
4002 for the next and so on. 
6. Login using the username and password you provided and then run the following command(s) to setup the game environment:  
  @batchcommand text_sims.build for the Home world (use branch `master` for this)  
  @batchcommand tutorial_world.build for the Fantasy world (use branch `fantasy` for this)  
  
Now, the server and the game should be fully setup. You can test by logging in using telnet
and trying to play the game (make sure you know what the commands are).

You can stop the game servers by using `stop.sh`.
