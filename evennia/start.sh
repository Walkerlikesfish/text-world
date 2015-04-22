cd game && evennia stop && cd ..
rm -rf game
evennia --init game
cd game
evennia migrate
evennia -i start
cd ..
