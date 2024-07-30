import random

def player(prev_play, opponent_history=[]):
    if prev_play:
        opponent_history.append(prev_play)

    n = 3  # Độ dài chuỗi để theo dõi

    # Xây dựng mô hình Markov
    if len(opponent_history) <= n:
        return random.choice(["R", "P", "S"])

    sequence = "".join(opponent_history)
    patterns = {}

    for i in range(len(sequence) - n):
        pattern = sequence[i:i + n]
        next_move = sequence[i + n]
        if pattern not in patterns:
            patterns[pattern] = {"R": 0, "P": 0, "S": 0}
        patterns[pattern][next_move] += 1

    last_pattern = "".join(opponent_history[-n:])
    if last_pattern in patterns:
        prediction = max(patterns[last_pattern], key=patterns[last_pattern].get)
    else:
        prediction = random.choice(["R", "P", "S"])

    ideal_response = {"R": "P", "P": "S", "S": "R"}
    return ideal_response[prediction]

