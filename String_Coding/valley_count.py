str = "UDDDUDUU"

def check(str):
    altitude = 0    # sea level
    valley_count = 0

# we only increment the valley counter when the hiker reaches sea level
# after a climb from below sea level.
    
    for i in str:
        if i=="U":
            altitude+=1
            if altitude==0:    # to check if we are starting from below sea level
                valley_count+=1
        else:
            altitude-=1

    print(valley_count)

check(str)
