import random
import sys

dict1_1 = "dispossess drencher barstool interval cardiacs vixens mooncalves tinnily perineal panamanian unparalleled unsoundness goalkeeper torchier eclat bartisans jewed claudius evading monogamy automatically shuckings electromagnetic coatee swallowing padrone dispensaries mexicans opulently monumentally intent homebreds concordantly elitists monopolism crimps catastrophical vulnerable bicepses julius brainier sinker supt sluggishly doctrine revives pupate towability openendedness bagginess transcribing"
dict1_2 = "portaled grouter martha staving convinces glucoses engild slideways brewages recommend retorted duchesses temporalties architecturally sneered nonresidence enfilade attn buxomest delouses whammy humiliation larker inhabiter drowsiness cobbles femaleness redeemability peremptorily fluencies chemosensitivities duality semestrial adsorbates upholder obligator resituating prolix unassailable diminishments manipulating winnable bedazzling whereby libeled theologians attentiveness pillboxes idolisms i"
dict1_3 = "mopeds exemptions finial misfiles dandyism transistors chemoreceptivity pickerels opprobriums pessimist livingly formulary entombment pratfalls libelously yahooism zippier conventionalizing reconsolidates draftsmen playoff dissonant assert belgrade cosecs chamfer outrageously buglers blouses denigrates sequencies nonactives steers reassumed tenantry operated panty white retsina mystifiers eyedropperful management bindweed hansom verbalizing overacted interlaced scavengery spattering lurcher obla"
dict1_4 = "corpuscular malines kit abortiveness beseemed pyramidal scollops vinously loggerhead stockrooms kabob stilbestrol vascularly digraph rapport repressively herpetological shushes toothless huddled backtracks diabetics darklier waning coplots heartlessness reconstitution camellia seral abattoir nonmembership whisper jaywalked misinstruction joggled courteous mandarin wavelets soother marginality guttering maladroit oblong nomadism greenwood postelection cinquefoils dubiety webless marts questor sco"
dict1_5 = "stratocumuli diesels pegless queuers invaluably halberd gluteal administration midbody fault stub recrate transship unthawed coercions lunations slangs moults gracing incompletely circumnavigate impeded inning windiness developments peculates insensateness forevermore unsteady houston assonant dicotyledons douser biotins rebaptized tinny majorem sociosexualities informatively throve bruited grassy hermeneutical reindexed screwier doubter guiltlessly monomaniacs hygienist wearying triune chias bu"

dictionary_1 = [dict1_1,dict1_2,dict1_3,dict1_4,dict1_5]


class PlaintextShifts:
    def __init__(self, plaintext, r_shifts):
        self.plaintext = plaintext
        self.r_shifts = r_shifts

    def find_ngram_freq(self, n):
        ngram_dict = {}
        for each in self.r_shifts:
            l = len(each)
            for i in range(0,l-n+1):
                ngram = tuple(each[i:i+n])
                if ngram not in ngram_dict:
                    ngram_dict[ngram] = 1
                else:
                    ngram_dict[ngram] += 1
        return ngram_dict

# get the character index in the alphabet with 'space' being index 0
def get_char_ind(char):
    if char == ' ': 
        return 0 
    else:
        return ord(char) - ord('a') + 1

# calculate how many shifts it take to turn pChar into cChar
def calculateShifts(pChar, cChar):
    p = get_char_ind(pChar)
    c = get_char_ind(cChar)
    if c >= p:
        return c - p
    return 27 - p + c

# make a list of all shifts of each character
def lstShifts(pText, cText):
    return list(map(calculateShifts, pText, cText))

# if there are r random characters inserted, compare the plaintext to r substrings 
# of same length from the ciphertext, each time moving up one character
def get_r_shifts(c):
    r_shifts = []
    for p in dictionary_1:
        if len(p) >= len(c):
            continue
        shifts = []
        r = len(c) - len(p)
        for i in range(0,r+1):
            shifts.append(lstShifts(p, c[i:i+len(p)]))
        r_shifts.append(PlaintextShifts(p,shifts))
    return r_shifts

# solver function
def decrypt_dict1(cipher):
    r_shifts = get_r_shifts(cipher)
    if len(r_shifts) == 0:
        return None
    # find the maximum ngram value of each plaintext and return the one with the largest value
    max_ngram = list(map(lambda x: (x.plaintext, max(x.find_ngram_freq(5).values())), r_shifts))
    result = max(max_ngram, key=lambda x: x[1])   
    return result[0]



def __main__():
    sys.stdout.write('Welcome! Enter Ciphertext below. \n')
    cipher = input()
    test1_decryption = decrypt_dict1(cipher)
    sys.stdout.write('Decryption complete! Here is our guess: \n')
    sys.stdout.write(test1_decryption)

__main__()