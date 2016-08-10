def parseText(parse, roomSyn):
    #Parse the players raw input into verbs, nouns, attributes etc.
  
    #Reset parse data (except raw)
    parse['words'] = [] #All known words (verbs + objs + other)
    parse['verbs'] = [] #All known verbs
    parse['objs'] = [] #All known objects
    parse['other'] = [] #All other known words
    parse['attr'] = [] #Some words set attributes, i.e. attack would all yield violent attr
    parse['unknown'] = [] #All unknown words
    parse['modifier'] = '' #Modifier words 'in', 'over', 'under', or 'behind' (used by look commands)
    parse['num'] = None #Stores any number specified (or the word all = 9999)

    #Check for any numbers (Word numbers such as "three" are checked later)
    tempList = parse['raw'].split() #Create a temp list of words
    for word in tempList:
        if word.isdigit(): #Check if it is numerical
            n = int(word)
            if n >= 2: parse['num'] = n #Only values of 2 or over are used

    #Remove all characters other than spaces and letters
    txt = ''
    for char in parse['raw']:
        if char in ' abcdefghijklmnopqrstuvwxyz':
            txt += char

    #Split the raw input into a list of words
    rawList = txt.split()

    #Remove (collapse to empty string) some words such as 'a' and 'the'
    for word in rawList:
        if word in ['a', 'an', 'the', 'and', 'or', 'if', 'at', 'to', 'for', 'then', 'with', 'it', 'i',
                    'on', 'of']:
            rawList[rawList.index(word)] = ''

    #Check for synonyms:
    for word in rawList:
        if word == '': continue
        for synData in synonyms:
            if word in synData[1]:
                rawList[rawList.index(word)] = synData[0]

    #Check for room specific synonyms:
    for word in rawList:
        if word == '': continue
        for synData in roomSyn:
            if word in synData[1]:
                rawList[rawList.index(word)] = synData[0]
    
    #Look for words on accepted list of nouns, verbs, and other; collapse word if found
    for word in rawList:
        if word == '': continue
        if word in objs:
            parse['objs'].append(word)
            parse['words'].append(word)
            rawList[rawList.index(word)] = ''
        elif word in verbs:
            parse['verbs'].append(word)
            parse['words'].append(word)
            rawList[rawList.index(word)] = ''
        elif word in other:
            parse['other'].append(word)
            parse['words'].append(word)
            rawList[rawList.index(word)] = ''

    if settings['typoAssist'][0] > 0:
        #Check for close word matches in accepted nouns, verbs, and other
        for word in rawList:
            if word == '': continue
            matchList = closeMatch(word, verbs + objs + other)
            if matchList:
                rawList[rawList.index(word)] = ''
                word = matchList[0]
                #If word is in room syn list, it is overwritten with the syn value
                for synData in roomSyn:
                    if word in synData[1]:
                        word = synData[0]
                parse['words'].append(word)
                if word in objs:
                    parse['objs'].append(word)
                elif word in verbs:
                    parse['verbs'].append(word)
                elif word in other:
                    parse['other'].append(word)  

        #Check for close matches on list of words with synonyms
        for word in rawList:
            if word == '': continue
            matchList = closeMatch(word, synonymList)
            if matchList:
                rawList[rawList.index(word)] = matchList[0]

        #Create a list of all words in room specific synonyms 
        roomSynList = []
        for synData in roomSyn:
            for word in synData[1]:
                roomSynList.append(word)
        
        #Check for close matches on list of room synonyms
        for word in rawList:
            if word == '': continue
            matchList = closeMatch(word, roomSynList)
            if matchList:
                rawList[rawList.index(word)] = matchList[0]

        #Recheck for synonyms:
        for word in rawList:
            if word == '': continue
            for synData in synonyms:
                if word in synData[1]:
                    rawList[rawList.index(word)] = synData[0]
    
        #Recheck for room specific synonyms:
        for word in rawList:
            if word == '': continue
            for synData in roomSyn:
                if word in synData[1]:
                    rawList[rawList.index(word)] = synData[0]
    
        #Relook for words on accepted list of nouns, verbs, and other; collapse word if found
        for word in rawList:
            if word == '': continue
            if word in objs:
                parse['objs'].append(word)
                parse['words'].append(word)
                rawList[rawList.index(word)] = ''
            elif word in verbs:
                parse['verbs'].append(word)
                parse['words'].append(word)
                rawList[rawList.index(word)] = ''
            elif word in other:
                parse['other'].append(word)
                parse['words'].append(word)
                rawList[rawList.index(word)] = ''
    
    #If any words are left uncollapsed, place them on unknown list
    for word in rawList:
        if word == '': continue
        parse['unknown'].append(word)

    #Some words set general attributes or the modifier
    for word in parse['words']:
        for att in attributes:
            if word in att[1]:
                parse['attr'].append(att[0])
        if word in ['in', 'under', 'behind', 'over']:
            parse['modifier'] = word

    #Check for number words "two" through "ten" (no need for one)
    numList = ['two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten']
    for word in numList:
        if word in parse['other']:
            parse['num'] = numList.index(word) + 2 #Ajust so that index 0 matches 2 etc
    
    #If the word "all" was found, set num to 9999
    if 'all' in parse['words']: parse['num'] = 9999
