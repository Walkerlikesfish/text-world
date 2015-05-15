NUM_GAMES=$1
for ((i = 1; i <= $NUM_GAMES; i++ )); do
    cd game$i && evennia stop && cd ..
done;
