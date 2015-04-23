NUM_GAMES=4
for ((i = 1; i <= $NUM_GAMES; i++ )); do
    cd game$i && evennia stop && cd ..;
    rm -rf game$i;
    evennia --init game$i;
    cd game$i;
    evennia migrate;
    echo "TELNET_PORTS = ["$((i + 4000))"]" >>server/conf/settings.py
    echo "AMP_PORT = "$((6000 + i)) >> server/conf/settings.py;
    echo "WEBSERVER_PORTS = [("$((8000+i))", "$((5100 + i))")]" >> server/conf/settings.py;
    echo "WEBSOCKET_CLIENT_PORT = "$((8100 + i)) >> server/conf/settings.py;
    evennia -i start;
    cd ..
done;
