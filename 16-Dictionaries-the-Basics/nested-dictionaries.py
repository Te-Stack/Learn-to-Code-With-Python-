tv_shows = {
    "The X-Files":{
        "Season 1":{
            "Episodes":["Scary Monster", "Scary Aliens"],
            "Genre":"Science Fiction",
            "Year":1983
        },
        "Season 2":{
            "Episodes":["Scary Conspiracy"],
            "Genre":"Horror",
            "Year":1994
        }
    },
    "lost":{
        "Season 1":{
            "Episodes":["What the heck is happening on this island"],
            "Genre":"Science Fiction",
            "Year":2004
        }
    }
}

print(tv_shows["The X-Files"]["Season 1"]["Episodes"][1])
print(tv_shows["The X-Files"]["Season 2"]["Year"])
print(tv_shows["lost"]["Season 1"]["Genre"])