import pandas as pd

# Your list
data = [['Now', 'should0', 'I1', 'slit2', 'my3', 'wrists4', 'Go', 'for5', 'it2', 'all6', 'or5', 'call6', 'it2', 'quits4', 'Picture', 'me', 'taking8', 'my3', 'life9', 'leaving8', 'my3', 'wife9', 'and10', 'my3', 'daughter7', 'shit2', 'Wish', 'I1', 'could0', 'slip', 'back', 'and10', 'switch11', 'the12', 'memories13', 'Lift', 'the12', 'felonies13', 'from14', 'my3', 'record', 'and10', 'respected', 'my3', 'enemies13', 'Live', 'like15', 'the12', "Kennedy's", 'â€”16', 'above17', 'the12', 'law18', 'fuck', "'em19", 'all!6', "I'm20", 'coming8', 'for5', 'the12', 'rich11', 'thieving8', "'em19", 'even21', 'if', 'I1', "wasn't22", 'poor7', 'I1', 'seen', 'it2', 'all6', 'like15', 'I1', 'said23', 'before5', 'The24', 'streets4', 'are5', 'for5', 'men', 'at', 'war7', 'and10', 'the12', 'beasts4', 'are5', 'the12', 'predators', 'I1', 'shed23', 'it2', 'all6', 'first25', 'and10', 'be', 'the12', 'primary26', 'source27', 'Of', 'course27', 'I1', 'bury26', 'any28', 'adversaries13', 'trying', 'to29', 'floss', 'Just', 'because', 'the12', 'reason30', 'I1', 'leave', "'em19", 'lost25', 'in21', 'the12', 'sauce', 'Teeing', 'off', 'like15', 'we32', 'up', 'North', 'just25', 'for5', 'being8', 'soft', 'A', 'beaten30', 'horse27', 'like15', 'a12', 'slave', 'getting8', 'minimum19', 'wage34', 'Filling', 'the12', 'gauge34', 'front22', 'page34', 'these', 'are5', 'the12', 'last31', 'days!35', 'Cash', 'pays35', 'and10', 'rules36', 'â€”16', 'the12', 'root37', 'of17', 'all6', 'evil38', 'Shooting', 'amigos39', 'for5', 'loot37', 'and10', 'perico', 'polluting8', 'our7', 'people38', 'Moving', 'kilos39', 'like15', "it's4", 'all6', 'good0', 'through40', 'every26', 'ghetto', 'I1', "ain't", 'judging8', 'but', 'bugging8', 'how', 'we32', 'fall6', 'so', 'many28', 'levels36', 'The24', "devil's36", 'got', 'us', 'by41', 'the12', 'balls36', "That's", 'why', 'the12', 'law18', 'allows', 'the12', 'drugs', 'to29', 'overflood', 'Knowing', 'we32', 'gonna33', 'buy41', 'it2', 'all6', "It's", 'time42', 'to29', 'call6', 'a12', 'world', 'order7', 'where7', 'every26', "girl's36", 'your7', 'daughter7', 'And', 'priceless', 'as', 'ice', 'is', 'and10', 'pearls36', 'fresh', 'out', 'the12', 'water7', "I'm20", 'gonna33', 'get2', 'mine', 'either7', 'from14', 'crime42', 'or5', 'through40', 'the12', 'Bible', 'Whichever', 'way33', 'it2', 'better7', 'pay33', "I'm20", 'feeling8', 'suicidal38']]


# Create a DataFrame
df = pd.DataFrame(data)

# Write to an Excel file
df.to_excel("Big Pun - Boomerang.xlsx", index=False, header=False)