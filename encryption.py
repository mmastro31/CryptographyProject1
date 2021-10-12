import sys
import random

#test 1
dict1_1 = "dispossess drencher barstool interval cardiacs vixens mooncalves tinnily perineal panamanian unparalleled unsoundness goalkeeper torchier eclat bartisans jewed claudius evading monogamy automatically shuckings electromagnetic coatee swallowing padrone dispensaries mexicans opulently monumentally intent homebreds concordantly elitists monopolism crimps catastrophical vulnerable bicepses julius brainier sinker supt sluggishly doctrine revives pupate towability openendedness bagginess transcribing"
dict1_2 = "portaled grouter martha staving convinces glucoses engild slideways brewages recommend retorted duchesses temporalties architecturally sneered nonresidence enfilade attn buxomest delouses whammy humiliation larker inhabiter drowsiness cobbles femaleness redeemability peremptorily fluencies chemosensitivities duality semestrial adsorbates upholder obligator resituating prolix unassailable diminishments manipulating winnable bedazzling whereby libeled theologians attentiveness pillboxes idolisms i"
dict1_3 = "mopeds exemptions finial misfiles dandyism transistors chemoreceptivity pickerels opprobriums pessimist livingly formulary entombment pratfalls libelously yahooism zippier conventionalizing reconsolidates draftsmen playoff dissonant assert belgrade cosecs chamfer outrageously buglers blouses denigrates sequencies nonactives steers reassumed tenantry operated panty white retsina mystifiers eyedropperful management bindweed hansom verbalizing overacted interlaced scavengery spattering lurcher obla"
dict1_4 = "corpuscular malines kit abortiveness beseemed pyramidal scollops vinously loggerhead stockrooms kabob stilbestrol vascularly digraph rapport repressively herpetological shushes toothless huddled backtracks diabetics darklier waning coplots heartlessness reconstitution camellia seral abattoir nonmembership whisper jaywalked misinstruction joggled courteous mandarin wavelets soother marginality guttering maladroit oblong nomadism greenwood postelection cinquefoils dubiety webless marts questor sco"
dict1_5 = "stratocumuli diesels pegless queuers invaluably halberd gluteal administration midbody fault stub recrate transship unthawed coercions lunations slangs moults gracing incompletely circumnavigate impeded inning windiness developments peculates insensateness forevermore unsteady houston assonant dicotyledons douser biotins rebaptized tinny majorem sociosexualities informatively throve bruited grassy hermeneutical reindexed screwier doubter guiltlessly monomaniacs hygienist wearying triune chias bu"

dictionary_1 = [dict1_1,dict1_2,dict1_3,dict1_4,dict1_5]

#test 2
dict2 = "lacrosses protectional blistered leaseback assurers frizzlers submerse rankness moonset farcer brickyard stolonic trimmings glottic rotates twirlier stuffer publishable invalided harshens tortoni unlikely alefs gladding favouring particulate baldpates changeover lingua proctological freaking outflanked amulets imagist hyped pilfers overachiever clarence outdates smeltery"


# space character is at index 0, then a, b, c, d, e, f,..., z
abc_lst = [' '] + [chr(i + ord('a')) for i in range(26)]

# get character from a given index (can be larger than 27)
def get_char(c):
    return abc_lst[(c % 27)]

def get_ind(char):
    return ord(char) - ord('a') + 1

# key character scheduling computes “j(i') = (i' mod t) + 1”
def j(i, t):
    return (1 + i) % t

# probablity for random character
def coin():
    return random.uniform(0,1)

# get random character
def random_char():
    return abc_lst[random.randint(0,26)]

#generate a plaintext of length L using dict2
def combine_words(L):
  potential_words = dict2.split()
  plaintext = ""
  while len(plaintext) < L:
    random_index = random.randrange(0, len(potential_words))
    if len(plaintext) == 0:
      plaintext += potential_words[random_index]
    else:
      plaintext += " "
      plaintext += potential_words[random_index]
  plaintext = plaintext[:500]
  return plaintext


# encrypt with shift
# message m
# key space: 0 <= k <= 26 
# 0 <= t <= 24
# prob = 0.05 but able to test for more randomness

def encrypt(m, j, k, t,prob):
    newText = ""
    for i in range(len(m)):
        
        probCoin = coin()

        if probCoin < prob:
            newText += random_char()
        
        char_index = ord(m[i]) - ord('a') + 1
        if m[i] == ' ':
            char_index = 0

        newText += get_char(char_index + k[j(i, t)])

    return newText


#prob = probability of random character
def get_encrypted_text(prob):
    prob = float(prob)
    t = random.randint(1,24)
    k = [random.randint(0,26) for i in range(t)]
    coinflip = random.randint(0,1)
    if coinflip == 1:
        testnum = 1
        randomint = random.randint(0,4)
        message = dictionary_1[randomint]
    else:
        testnum = 2
        message = combine_words(500)

    cipher = encrypt(message,j,k,t,prob)
    return cipher,testnum

def __main__():
    sys.stdout.write('Encryption scheme for testing \n')
    prob = input('Enter probability of random character insertion between 0 and 1 (recommended: 0.05): ')
    c,testnum = get_encrypted_text(prob)
    sys.stdout.write('Test: ' + str(testnum) + '\n')
    sys.stdout.write(c)


__main__()