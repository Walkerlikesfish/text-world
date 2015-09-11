Setting up the Evennia server
---------------------
1. Clone this repository and follow instructions in INSTALL.md to install evennia up till the 'Evennia package install' section.  
2. Change directory using `cd evennia/`.  
3. Run `start.sh <n>` to start up `n` different game servers - each server will use a different port.   
During server start, you will be asked to provide username and password - make sure this matches the framework code
(the defaults are root and root for both username and password)  
4. Use telnet localhost <gameport> to connect to the game server. The default game ports start from 4001 for the first game server, 
4002 for the next and so on. 
5. Login using the username and password you provided and then run the following command(s) to setup the game environment:  
  @batchcommand text_sims.build for the Home world (use branch `master` for this)  
  @batchcommand tutorial_world.build for the Fantasy world (use branch `fantasy` for this)  
  
Now, the server and the game should be fully setup. You can test by logging in using telnet
and trying to play the game (make sure you know what the commands are).
