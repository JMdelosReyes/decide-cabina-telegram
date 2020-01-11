

def parseVotings(response):
    res = []
    for r in response:
        v = {'id': r['id'], 'name': r['name'], 'desc': r['desc'], 'end_date' : r['end_date'] , 'start_date' : r['start_date'], 'question': r['question'],'pub_key':r['pub_key']}
        res.append(v)
        
    return res

def createKeybVoting(votings):
    res = [[]]
    
    for v in votings:
        votingName = []
        votingName.append(v['name'])
        res.append(votingName)
    return res