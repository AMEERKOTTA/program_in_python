# Calculate the Highest Score from a List of Scores

scores = [112,223,123,3213,213,432,234,324,434,543]
# from the above list of scores
# find the highest score


# assume that first element in the list is highest
highest_score = scores[0]
for score in scores:
    if score > highest_score:
        highest_score = score

print("The Highest Score is : ", highest_score)


