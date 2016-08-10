def seeIfCloseMatch():
    pass

synonyms = [('look', ['examine', 'observe', 'view', 'inspect', 'study', 'describe']),
            ('take', ['get', 'obtain', 'grab', 'acquire']),
            ('talk', ['speak', 'communicate', 'chat', 'say']),
            ('attack', ['hit', 'punch', 'kick', 'ambush', 'fight', 'assault', 'slap']),
            ('kill', ['assassinate', 'murder', 'execute', 'slay', 'terminate']),
            ('break', ['destroy', 'smash', 'demolish', 'damage', 'crush']),
            ('move', ['pull', 'tug', 'drag']),
            ('press', ['push']),
            ('turn', ['rotate', 'spin', 'twist']),
            ('use', ['employ', 'utilize', 'drink', 'eat', 'consume']),
            ('go', ['head', 'walk', 'run', 'travel', 'journey']),
            ('under', ['below', 'underneath', 'beneath']),
            ('painting', ['picture', 'portrait', 'sketch', 'drawing']),
            ('in', ['inside']),
            ('jump', ['leap']),
            ('repair', ['fix', 'mend']),
            ('cave', ['cavern']),
            ('close', ['shut']),
            ('disarm', ['deactivate']),
            ('drop', ['discard']),
            ('person', ['guy', 'man', 'woman', 'lady', 'boy', 'girl']),
            ('all', ['everything']),
            ('carpet', ['rug']),
            ('rope', ['line', 'cord', 'cable']),
            ('footsteps', ['footprints', 'steps']),
            ('ceiling', ['up', 'sky']),
            ('floor', ['down', 'ground']),
            ('north', ['n']),
            ('south', ['s']),
            ('west', ['w']),
            ('east', ['e']),
            ('help', ['instructions'])]

def closeMatch(word, matches):
    #Used by parsing function to find words that are close to matching (to fix player typos)
    
    return difflib.get_close_matches(word, matches, 1, settings['typoAssist'][0])
