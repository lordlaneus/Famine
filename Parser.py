blackList ={\
    "please",
    "a",
    "to",
    "the",
    "an",
    "at",
    }

simpleVerbDictionary={\
    "look around": "look",
    "look room": "look",
    "i": "inventory",
    "n": "go n",
    "s": "go s",
    "e" : "go e",
    "w" : "go w",
    "u" : "go u",
    "d" : "go d",
    "b" : "go b",
    "north": "go n", #direction verbs
    "south": "go s",
    "east" : "go e",
    "west" : "go w",
    "up" : "go u",
    "down" : "go d",
    "back" : "go b",
    }
verbDictionary = {\
    "i": "inv",
    "inventory": "inv",
    "grab": "get",
    "take": "get",
    "pick up": "get",
    "pickup": "get",
    "goto" : "go",
    "go to" : "go",
    "head": "go",
    "travel": "go",
    "walk to": "go",
    "walk": "go",
    "examine": "look",
    "tell": "say",
    "activate" : "use",
    

    }


def parse(cmd):
    cmd = cmd.lower()
    wordList = []
    verbLength =-1
    #find verb
    for key, value in simpleVerbDictionary.items():
        if cmd == key:
            cmd = value
            break
    for key, value in verbDictionary.items():
        if cmd.startswith(key):
            verb = value
            verbLength = len(key)
            break
    if verbLength >0:
        wordList.append(verb)
        cmd =cmd[verbLength+1:]
        
    #list words
    for word in cmd.split(" "):
        if word not in blackList:
            wordList.append(word)
    return wordList
