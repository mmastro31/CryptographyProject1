import random
import sys

####################################################################################
# Dictionary Handling

dict1_1 = "dispossess drencher barstool interval cardiacs vixens mooncalves tinnily perineal panamanian unparalleled unsoundness goalkeeper torchier eclat bartisans jewed claudius evading monogamy automatically shuckings electromagnetic coatee swallowing padrone dispensaries mexicans opulently monumentally intent homebreds concordantly elitists monopolism crimps catastrophical vulnerable bicepses julius brainier sinker supt sluggishly doctrine revives pupate towability openendedness bagginess transcribing "
dict1_2 = "portaled grouter martha staving convinces glucoses engild slideways brewages recommend retorted duchesses temporalties architecturally sneered nonresidence enfilade attn buxomest delouses whammy humiliation larker inhabiter drowsiness cobbles femaleness redeemability peremptorily fluencies chemosensitivities duality semestrial adsorbates upholder obligator resituating prolix unassailable diminishments manipulating winnable bedazzling whereby libeled theologians attentiveness pillboxes idolisms i"
dict1_3 = "mopeds exemptions finial misfiles dandyism transistors chemoreceptivity pickerels opprobriums pessimist livingly formulary entombment pratfalls libelously yahooism zippier conventionalizing reconsolidates draftsmen playoff dissonant assert belgrade cosecs chamfer outrageously buglers blouses denigrates sequencies nonactives steers reassumed tenantry operated panty white retsina mystifiers eyedropperful management bindweed hansom verbalizing overacted interlaced scavengery spattering lurcher obla"
dict1_4 = "corpuscular malines kit abortiveness beseemed pyramidal scollops vinously loggerhead stockrooms kabob stilbestrol vascularly digraph rapport repressively herpetological shushes toothless huddled backtracks diabetics darklier waning coplots heartlessness reconstitution camellia seral abattoir nonmembership whisper jaywalked misinstruction joggled courteous mandarin wavelets soother marginality guttering maladroit oblong nomadism greenwood postelection cinquefoils dubiety webless marts questor sco"
dict1_5 = "stratocumuli diesels pegless queuers invaluably halberd gluteal administration midbody fault stub recrate transship unthawed coercions lunations slangs moults gracing incompletely circumnavigate impeded inning windiness developments peculates insensateness forevermore unsteady houston assonant dicotyledons douser biotins rebaptized tinny majorem sociosexualities informatively throve bruited grassy hermeneutical reindexed screwier doubter guiltlessly monomaniacs hygienist wearying triune chias bu"

dict2 = "lacrosses protectional blistered leaseback assurers frizzlers submerse rankness moonset farcer brickyard stolonic trimmings glottic rotates twirlier stuffer publishable invalided harshens tortoni unlikely alefs gladding favouring particulate baldpates changeover lingua proctological freaking outflanked amulets imagist hyped pilfers overachiever clarence outdates smeltery"

dictionary_1 = [dict1_1,dict1_2,dict1_3,dict1_4,dict1_5]
dictionary_2 = dict2.split(' ')

alphabet = ' abcdefghijklmnopqrstuvwxyz'
abc_lst = [' '] + [chr(i + ord('a')) for i in range(26)]

letter_frequencies = {' ': 0.1918182,'a':0.0651738,'b':0.0124248,'c':0.0217339,'d':0.0349835,'e':0.1041442,'f':0.0197881,'g':0.0158610,'h':0.0492888,'i':0.0558094,'j':0.0009033,'k':0.0050529,'l':0.0331490,'m':0.0202124,'n':0.0564513,'o':0.0596302,'p':0.0137645,'q':0.0008606,'r':0.0497563,'s':0.515760,'t':0.0729357,'u':0.0225134,'v':0.0082903,'w':0.0171272,'x':0.0013692,'y':0.0145984,'z':0.0007836}


####################################################################################
# Case 1: cipher and plaintext are same length

#modular decryption for final decryption scheme
def mod_encrypt(index):
    return abc_lst[(index % 27)]

#reindex so that ' '=0, a=1,...,z=27
def reindex(text,int):
    original_index = ord(text[int]) - ord('a') + 1
    if text[int] == ' ':
        original_index = 0 
    return original_index

#calculate the distance to get from cipher[i] to plaintext[i]
def compare_cipher_and_dict(ciphertext, dict):
    key = []
    for i in range(0,len(ciphertext)):
      newindex_cipher = reindex(ciphertext,i)
      newindex_plain = reindex(dict,i)
      difference = (newindex_cipher - newindex_plain + 27) % 27
      key.append(difference)
    return key

#finding the key length by testing if 
def find_key_length(keyArray):
    keyLength = 0
    keyGuess = []
    for t in range(24,1,-1):  #each t
        if keyArray[0:t+1] == keyArray[t:2*t+1]:
            keyLength = t
            keyGuess = keyArray[0:t]
            break
        else:
            keyLength = 0
            keyGuess = []
    return(keyLength,keyGuess)

#decryption scheme for when there is no random characters
def decrypt_norandom(cipher, keyguess):
    decrypted = ""
    i = 0
    while len(decrypted) < len(cipher):
        for j in range(0,len(keyguess)):
            if len(decrypted) < len(cipher):
                original_index = ord(cipher[i]) - ord('a') + 1
            else:
                break
            if cipher[i] == ' ':
                original_index = 0 
            original_index -= keyguess[j]
            templetter = mod_encrypt(original_index)
            decrypted = decrypted + templetter
            i += 1
    return decrypted

#compare each plaintext to the cipher
#when a key is found, that plaintext is the answer
def test1_norandom(cipher,dict1):
    for i in range(0,len(dict1)):
        tempkey = compare_cipher_and_dict(cipher,dict1[i])
        keyLength,keyGuess = find_key_length(tempkey)
        if keyLength != 0:
            decrypted_text=decrypt_norandom(cipher,keyGuess)
            break
    return (decrypted_text, 100)

########################################################################
#Case 2: cipher and plaintext are not the same length
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
    return result

##################################################################################
# Test 2

#gets the index of coincidence for a specific 
#for each letter in alphabet, sum the count * (count-1)
def index_coincidence(cipher):
	
	N = float(len(cipher))
	sum = 0.0

	for letter in alphabet:
		sum+= cipher.count(letter) * (cipher.count(letter)-1)

	ic = sum/(N*(N-1))
	return ic

#index of coincidence to guess the key
def get_key_length(cipher):
	ic_table=[]
	for t in range(1,24):  #try for each t
		sum=0.0
		avg=0.0
		for i in range(t): #go through t
			sequence=""
			for j in range(0, len(cipher[i:]), t):
				sequence += cipher[i+j]
			sum+=index_coincidence(sequence)

		avg=sum/t
		ic_table.append(avg)

	best_guess = ic_table.index(sorted(ic_table, reverse = True)[0])
	second_best_guess = ic_table.index(sorted(ic_table, reverse = True)[1])

	#if the first guess is divisible by the second, return the second
	if best_guess % second_best_guess == 0:
		return second_best_guess
	else:
		return best_guess + 1

def get_char(c):
    return abc_lst[(c % 27)]


def decipher(cipher, t,alpha_frequencies):
    keys = []
    for jump in range(t):
        dic = {}
        freq = {}
        total_values=[]
        total = 0
        for i in range(jump,len(cipher),t):
            if cipher[i] in dic:
                dic[cipher[i]] += 1
            else:
                dic[cipher[i]] = 1
        for value in dic.values():
            total += value
        for key, value in dic.items():
            frequency = value/total
            if key not in freq:
                freq[key] = frequency
                #['a':0.25]
        total = 0
        freq = sorted(freq.items())
        order_of_chars =[]
        for i in freq:
            order_of_chars.append(alpha_frequencies[i[0]])
        for i in range(len(freq)):
            total = 0
            for j in range(len(freq)):
                val = freq[j][1]
                total += order_of_chars[j]*val
            total_values.append(total)
            first_char = freq[0]
            for k in range(len(freq)):
                if k == len(freq)-1:
                    freq[k] = first_char
                else:
                    freq[k] = freq[k+1]
        mx=0
        mx_index=0
        for i in range(len(total_values)):
            if total_values[i] > mx:
                mx = total_values[i]
                mx_index = i
        keys.append(mx_index)
    return keys
            


def decrypt_dict2(cipher):
    result = None
    key_length = get_key_length(cipher)
    key_guess = decipher(cipher,key_length,letter_frequencies)
    result = decrypt_norandom(cipher,key_guess)
    return result


def __main__():
    sys.stdout.write('Welcome! Enter Ciphertext below. \n')
    cipher = input()
    if len(cipher) <= len(dict1_1):
        test1_result = test1_norandom(cipher,dictionary_1)
    else:
        test1_result = decrypt_dict1(cipher)
    if test1_result[1] < 7:
        test2_result = decrypt_dict2(cipher)
        sys.stdout.write('Decryption complete! Here is our guess: \n')
        sys.stdout.write(test2_result)
    else:
        sys.stdout.write('Decryption complete! Here is our guess: \n')
        sys.stdout.write(test1_result[0])

__main__()