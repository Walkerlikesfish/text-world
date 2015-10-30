#USAGE: ./stop.sh <num_of_parallel_game_servers>

NUM_GAMES=$1
for ((i = 1; i <= $NUM_GAMES; i++ )); do
    cd game$i && evennia stop && cd ..
done;
