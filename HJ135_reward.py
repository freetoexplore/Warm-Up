ratings = [1,2,2]
ratings = [1,0,2]
reward = len(ratings)
for ix in range(len(ratings)):
    if ix>=1 and ratings[ix-1]<ratings[ix] :
        reward += 1
    if ix <= (len(ratings) -2) and ratings[ix+1]<ratings[ix]:
        reward += 1
        
print(reward)