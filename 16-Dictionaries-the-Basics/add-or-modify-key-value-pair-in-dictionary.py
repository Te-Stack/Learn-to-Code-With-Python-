sport_teams_rosters = {
    "New England Patroits": ["Tom Brady","Rob Gronkowski","Julian Edelman"],
    "New York Giants": ["Eli Manning","Odell Beckham"]   
} 

sport_teams_rosters["Pittsburgh Steelers"] = ["Ben Roethlisberger","Antonio Brown"]
print(sport_teams_rosters)

sport_teams_rosters["New York Giants"] = ["Eli Manning"]


video_game_options = {}
#video_game_options = dict()

video_game_options["subtitles"] = True
video_game_options["difficulty"] = "Medium"
video_game_options["volume"] = 7
print(video_game_options)

words = ["danger","beware","danger","beware","beware"]

def count_words(words):
    count = {}
    for word in words:
        if word in count:
            count[word] +=1
        else:
            count[word] = 1
    return count


print(count_words(["Quincy","Tejiri","Quincy"]))   
