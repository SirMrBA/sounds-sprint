from pathlib import Path
import json
root=Path(__file__).parent
words=json.loads((root/'words.json').read_text())
for w in words:
 w['original']={'rp':w['rp'],'ga':w['ga']}
 w['rp']=w['rp'].replace('ᵊ','(ə)');w['ga']=w['ga'].replace('ᵊ','(ə)')
 w['note']='Course-key model. Optional schwa is shown as (ə). Other dictionary variants may also be valid.'
 if w['id']==153:w['word']='wound (past of wind)'
 if w['id']==21:
  w['rp']='ˈtʊənəmənt';w['note']='The RP key prints /tʊe…/. Corrected to /tʊə…/ using Cambridge Dictionary. /ˈtɔːnəmənt/ is also accepted.';w['alternatives']={'rp':['ˈtɔːnəmənt'],'ga':['ˈtɝːnəmənt']};w['reference']='https://dictionary.cambridge.org/pronunciation/english/tournament'
 if w['id']==3:w['note']='Bass = low musical pitch here. The fish has /bæs/.'
 if w['id']==89:w['note']='Adjective appropriate. The verb ends in /eɪt/.'
 if w['id']==160:w['note']='Course-list pronunciation retained. Proper names depend on the place/person: Berkeley in Britain and Berkeley, California may differ.'
 if w['id']==10:w['note']='The key includes an epenthetic /p/. /ˈkʌmftəbəl/ is also common. Use Compare, then rate your answer.';w['alternatives']={'rp':['ˈkʌmftəbəl'],'ga':['ˈkʌmftəbəl']}
 if w['id']==38:w['note']='Course form retained, including the GA sequence /ɝːr/. Dictionary transcriptions vary; compare manually.'
 w['band']='1–55' if w['id']<=55 else '56–83' if w['id']<=83 else '84–136' if w['id']<=136 else '137–176'

consonants=[]
rows='''p|voiceless|bilabial|plosive|pin
b|voiced|bilabial|plosive|bin
t|voiceless|alveolar|plosive|tin
d|voiced|alveolar|plosive|din
k|voiceless|velar|plosive|coat
g|voiced|velar|plosive|goat
f|voiceless|labiodental|fricative|fan
v|voiced|labiodental|fricative|van
θ|voiceless|dental|fricative|thin
ð|voiced|dental|fricative|this
s|voiceless|alveolar|fricative|sip
z|voiced|alveolar|fricative|zip
ʃ|voiceless|palato-alveolar|fricative|ship
ʒ|voiced|palato-alveolar|fricative|measure
h|voiceless|glottal|fricative|hat
tʃ|voiceless|palato-alveolar|affricate|church
dʒ|voiced|palato-alveolar|affricate|judge
m|voiced|bilabial|nasal|man
n|voiced|alveolar|nasal|no
ŋ|voiced|velar|nasal|sing
l|voiced|alveolar|lateral approximant|leaf
r|voiced|post-alveolar|approximant|red
j|voiced|palatal|approximant|yes
w|voiced|labio-velar|approximant|wet'''
for row in rows.splitlines():
 s,v,p,m,e=row.split('|');consonants.append(dict(symbol=s,voice=v,place=p,manner=m,example=e))
vowels=[]
for row in '''iː|close|front|unrounded|fleece|17|14
ɪ|near-close|near-front|unrounded|kit|28|27
e|mid|front|unrounded|dress|29|49
æ|near-open|front|unrounded|trap|43|84
ɑː|open|back|unrounded|palm|87|91
ɒ|open|back|rounded|lot (RP)|87|79
ɔː|open-mid|back|rounded|thought|87|57
ʊ|near-close|near-back|rounded|foot|73|27
uː|close|back|rounded|goose|87|14
ʌ|open-mid|central|unrounded|strut|57|70
ɜː|mid|central|unrounded|nurse (RP)|58|49
ə|mid|central|unrounded|about|62|40'''.splitlines():
 s,h,b,l,e,x,y=row.split('|');vowels.append(dict(symbol=s,height=h,backness=b,lips=l,example=e,x=int(x),y=int(y)))

# Each topic is a short lesson, with independently reviewable rule cards.
topics=[]
def topic(id,title,subtitle,source,rows):
 rules=[]
 for row in rows.strip().split('\n'):
  q,a,ex,trap=row.split('|');rules.append(dict(q=q,a=a,example=ex,trap=trap))
 topics.append(dict(id=id,title=title,subtitle=subtitle,source=source,rules=rules))
topic('basics','Sounds, not spelling','Build the distinctions everything else depends on.','Introduction · pp. 7–15; Phonology · pp. 3–14', '''Phonetics vs phonology|Phonetics studies how speech sounds are produced, transmitted and perceived. Phonology studies how sounds function and pattern in a language.|Articulatory = production; acoustic = signal; auditory = perception.|A phoneme is a language-specific category, not a letter.
Phone, phoneme, allophone|A phone is an actual sound [tʰ]. A phoneme /t/ is an abstract meaning-distinguishing unit. Allophones are realizations of one phoneme.|Aspirated [tʰ] in top and unaspirated [t] in stop realize /t/.|Use / / for phonemes and [ ] for phones.
The minimal-pair test|Two words with different meanings differ in exactly one phoneme in the same position.|price /praɪs/ vs prize /praɪz/; height /haɪt/ vs hide /haɪd/.|bury and berry are homophones, not a minimal pair. thin–than changes two phonemes.
Count phonemes, not characters|Count each phoneme once. Diphthongs and English affricates count as one each; silent letters count as zero.|child = /tʃ aɪ l d/ = 4; aisle = /aɪ l/ = 2; psyche = /s aɪ k i/ = 4.|sword has 3 in RP but 4 in GA because of /r/.
Accent vs dialect|An accent concerns pronunciation. A dialect can also differ in grammar and vocabulary.|RP and GA are pronunciation reference models used in this course.|Every speaker has an accent. Neither model is inherently better.
The traditional RP inventory|The course uses 24 consonants, 12 monophthongs and 8 diphthongs for traditional RP.|44 phonemes in this teaching model.|Do not apply the traditional RP vowel count to every English accent.''')
topic('production','How sounds are made','Airflow, voicing and the three-part consonant description.','Production · pp. 3–20; Consonants · pp. 3–22', '''The English airstream|English speech sounds use a pulmonic egressive airstream: air is pushed out from the lungs.|Lungs → trachea → larynx → oral/nasal cavity.|Egressive means outward, not inward.
Voicing and the glottis|The glottis is the opening between the vocal folds. Vibration produces voiced sounds; open folds without vibration produce voiceless sounds.|Compare /s/ and /z/ with your fingers on your throat.|Complete closure can produce the glottal stop [ʔ].
The consonant formula|Give voicing, then place, then manner of articulation.|/d/ = voiced alveolar plosive.|All three features are needed for a full description.
Plosive, fricative, affricate|Plosive: complete closure and release. Fricative: narrow passage and friction. Affricate: stop released into a fricative as one phoneme.|/t/, /s/, /tʃ/.|Two symbols in /tʃ/ do not make two phonemes.
Nasals and the velum|For a nasal, the velum lowers so air can escape through the nose. English has /m n ŋ/.|/m/ bilabial; /n/ alveolar; /ŋ/ velar.|All three are voiced in the course's phoneme inventory.
Approximants and laterals|Approximants bring articulators close without the friction of a fricative. /l/ allows airflow around the sides of the tongue.|/w/ = voiced labio-velar approximant; /j/ = voiced palatal approximant.|The /j/ symbol is the initial sound in yes, not in judge.
Pitch, loudness and length|Pitch relates to vibration frequency; loudness to amplitude; duration to the time a sound lasts.|Stress can involve greater loudness, duration and pitch prominence.|Pitch and loudness are different properties.''')
topic('vowels','Map the vowels','Tongue height, front/back position and lip shape.','Vowels I · pp. 9–29; Vowels II · pp. 3–21', '''The vowel formula|Describe tongue height, tongue backness and lip rounding. Add length when useful.|/iː/ = close front unrounded; /uː/ = close back rounded.|Long versus short is not the only contrast: quality also differs.
Schwa /ə/|A mid central unrounded vowel, typical of unstressed syllables and weak forms.|about /əˈbaʊt/; a /ə/.|In the course's RP model, schwa is not stressed. It is different from /ɜː/.
Monophthong vs diphthong|A monophthong has a relatively steady quality. A diphthong glides within a single syllable.|/iː/ vs /aɪ/ in fleece and price.|A diphthong is one phoneme and one syllabic nucleus.
Closing diphthongs|The closing diphthongs glide towards /ɪ/ or /ʊ/.|/eɪ aɪ ɔɪ aʊ əʊ/ in RP; /oʊ/ replaces /əʊ/ in GA.|Use /əʊ/ for RP goat and /oʊ/ for GA goat consistently.
Centring diphthongs|Traditional RP has /ɪə eə ʊə/, gliding towards the centre.|near /nɪə/, square /skweə/, cure /kjʊə/.|/ʊə/ is increasingly replaced by /ɔː/. Use the course model consistently.
HappY tensing|Word-final unstressed happy uses /i/ in the course: the quality is close to /iː/ without marking it long.|happy /ˈhæpi/; city /ˈsɪti/.|Do not automatically write /ɪ/ or /iː/ for every final happy vowel.''')
topic('accents','Keep RP and GA apart','Choose one accent before you transcribe.','Consonants · p. 20; Vowels II · pp. 19–21; word keys', '''Rhotic vs non-rhotic|GA is rhotic: postvocalic /r/ is pronounced. RP is non-rhotic: /r/ normally appears only before a vowel.|car: RP /kɑː/, GA /kɑːr/.|Non-rhotic does not mean that /r/ is never pronounced: red still has /r/.
BATH, LOT and GOAT|In the course, BATH words may have RP /ɑː/ vs GA /æ/; LOT RP /ɒ/ vs GA /ɑː/; GOAT RP /əʊ/ vs GA /oʊ/.|task /tɑːsk/ vs /tæsk/; hot /hɒt/ vs /hɑːt/; go /gəʊ/ vs /goʊ/.|BATH is a lexical set, not a rule to apply to every written a.
NURSE in GA|The course accepts r-coloured /ɝː/ or the sequence /ɜːr/.|bird: RP /bɜːd/, GA /bɝːd/ or /bɜːrd/.|Do not add another /r/ to /ɝː/ automatically.
GA tapping|In suitable contexts, especially after a stressed vowel before an unstressed vowel, /t/ can be realized as a tap [ɾ].|city [ˈsɪɾi]; the course key often writes t̬.|This is an allophone, not a new phoneme in the word.
Yod and lexical differences|Some words differ beyond rhoticity: GA often drops /j/ after certain consonants. Individual words may have different stress or consonants.|new /njuː/ vs /nuː/; schedule /ˈʃedjuːl/ vs /ˈskedʒuːl/.|Do not mechanically convert every /juː/ to /uː/: you begins with /j/ in both.''')
topic('allophones','Phonemes in real speech','Recognise a contrast and a contextual variant.','Phonology · pp. 7–20; Wrap-up · pp. 24–25', '''Complementary distribution|Allophones occur in mutually exclusive, predictable environments.|In the RP teaching model, clear [l] before a vowel versus dark [ɫ] before a consonant or pause.|Different distribution alone is not enough: the sounds must also be related realizations of a phoneme.
Free variation|Different realizations may occur in the same environment without changing the word's meaning.|Different realizations of /t/ can occur across speakers and styles.|Free variation is influenced by accent, context and style; it is not unrestricted randomness.
Aspiration|/p t k/ are strongly aspirated at the beginning of a stressed syllable, except after /s/ in the same onset.|pin [pʰɪn] versus spin [spɪn].|The cluster in play can be aspirated; the important exception is /s/ + plosive.
Clear and dark l in RP|Clear [l] before a vowel or /j/; dark [ɫ] before a consonant or a pause.|life vs milk; fall in can have clear l because a vowel follows.|Look across word boundaries. This RP rule is not a universal rule for all accents.
Final devoicing|German devoices final obstruents; English preserves a phonological contrast such as /t/ versus /d/.|German Rad and Rat are homophones; English pat and pad contrast.|English final voiced sounds can be partly devoiced phonetically, but the contrast remains.''')
topic('syllables','Syllables and stress','Find the nucleus, then find what carries the emphasis.','Syllables and stress · pp. 3–18', '''Onset, nucleus, coda|Onset precedes the nucleus. Coda follows it. Nucleus plus coda make the rhyme.|/striːts/: onset /str/, nucleus /iː/, coda /ts/.|The onset and coda are optional; the nucleus is required.
Syllabic consonants|An unstressed /ə/ may disappear before /n/ or /l/, leaving a consonant as the syllable nucleus.|little [ˈlɪtl̩]; garden RP [ˈgɑːdn̩].|The early slide's vowel-only definition is simplified: a syllabic consonant can be a nucleus.
Read a CV pattern|C means consonant phoneme and V means vowel nucleus, including a diphthong.|tasks = CVCCC; eye = V; key = CV; ache = VC.|Adding a consonant does not necessarily add a syllable.
Mark lexical stress|Primary stress ˈ goes before the stressed syllable; secondary stress ˌ before a less prominent stressed syllable.|photographic /ˌfəʊtəˈgræfɪk/.|Do not put the stress mark after the vowel or omit it in polysyllabic words.
Stress can change meaning|The same written word may have different stress as a noun and a verb.|an ˈimport versus to imˈport; a ˈproject versus to proˈject.|Know the intended meaning of minute, desert, row and wound.
Compound vs phrase|Many compounds have early stress; a phrase often has later, stronger stress.|ˈgreenhouse = structure for plants; ˈgreen ˈhouse = a house that is green.|This is a tendency, not a universal rule.
Compound exceptions to learn|Material/ingredient compounds often have double stress. Road names often have double stress, except names ending in Street.|ˈcheese ˈsandwich; ˈOxford ˈRoad; ˈOxford Street; ˈapple juice.|The exceptions cake, juice and water often have single early stress.''')
topic('weak','Strong and weak forms','Transcribe a sentence as speech, not a row of dictionary entries.','Strong and weak forms · pp. 5–15', '''Content vs function words|Content words usually carry stress; function words are commonly unstressed and reduced.|Lexical verbs, nouns and adjectives versus articles, prepositions and auxiliaries.|Context can give a function word contrastive stress.
Common weak forms|Use reduced vowels for unstressed grammatical words.|a /ə/, and /ən(d)/, to /tə/, of /əv/, can /kən/, at /ət/, that /ðət/.|Not every grammatical word reduces in every context.
The before a vowel|The commonly has /ðə/ before a consonant sound and /ði/ before a vowel sound.|the book /ðə ˈbʊk/; the apple /ði ˈæpəl/.|Listen to the sound, not the letter: the university begins with /j/.
When strong forms return|Use strong forms for contrast, emphasis, citation and isolation. Many prepositions also take a strong form in final position.|Who is it for? /fɔː/ in RP. I CAN do it: /kæn/.|Sentence-final pronouns are not automatically strong. Treat the slide rule as a tendency.
Auxiliary have vs lexical have|Auxiliary have often reduces; stressed or lexical uses commonly retain a full form.|I have seen it may use /həv/ or /əv/.|Meaning and stress decide; do not replace every have with /əv/.
English rhythm|The course describes English as stress-timed: stressed syllables tend to organize the rhythm; unstressed material is compressed.|ˈWalk ˈdown the ˈpath to the ˈend of the caˈnal.|This is a rhythmic tendency, not a stopwatch law.''')
topic('endings','Plural, past and ng','Let the final sound choose the ending.','Connected speech I · pp. 6–10; Wrap-up · p. 26', '''Plural and third-person -s|After sibilants /s z ʃ ʒ tʃ dʒ/, use /ɪz/. Otherwise use /s/ after voiceless sounds and /z/ after voiced sounds.|buses /ˈbʌsɪz/, cats /kæts/, dogs RP /dɒgz/.|Use the final sound, not the final written letter. kids ends in /z/.
Past-tense -ed|After /t d/, use /ɪd/. Otherwise use /t/ after voiceless sounds and /d/ after voiced sounds.|wanted /ˈwɒntɪd/, looked /lʊkt/, played /pleɪd/.|Most -ed endings do not add a syllable.
Allomorph vs allophone|An allomorph is a variant of a morpheme; an allophone is a variant of a phoneme.|Plural /s z ɪz/ are allomorphs. [tʰ] and [t] are allophones.|Different allomorphs may contain different phonemes.
The ng rule|At the end of a morpheme, ng is usually /ŋ/. Within a morpheme it is often /ŋg/.|singer /ˈsɪŋə/ vs finger /ˈfɪŋgə/ in RP.|Comparatives and superlatives such as longer and longest retain /g/.''')
topic('connected','Connect the speech','Assimilation, elision and linking r.','Connected speech I · pp. 11–21; Connected speech II · pp. 4–15', '''Assimilation|A sound becomes more like a neighbouring sound. Regressive assimilation is influence from the following sound.|good boy [gʊb bɔɪ]; /d/ becomes bilabial before /b/.|A change in place is not the same as deleting the sound.
Regressive vs progressive|Regressive influence travels backwards from the following sound. Progressive influence comes from the preceding sound.|ten boys may have [m] before /b/: regressive.|Name both the direction and the feature that changes when asked.
Elision|A sound is omitted, especially in rapid or casual speech and difficult consonant clusters.|next day may lose /t/; baked beans may be [beɪk biːnz].|A deleted /t/ is elision, not simply assimilation.
Linking r in RP|A historical or written final r can surface before a following vowel.|four eggs /fɔːr egz/; there is /ðər ɪz/.|No linking r before a consonant or across a clear pause.
Intrusive r|Some non-rhotic speakers insert [r] between suitable adjacent vowels without a historical written r.|law and order; media event.|Distinguish it from linking r. Do not insert it automatically everywhere.
Connected-speech variants|Natural fluent speech permits more than one realization. Apply a process only where its context licenses it.|hot potato may assimilate /t/ towards /p/; Bless you may have [ʃ].|A model is not the only possible sentence transcription.''')
topic('transcription','A reliable transcription routine','Five passes that catch different mistakes.','Course outline · p. 2; Mock 3/3; Moodle transcription solution', '''Pass 1: choose an accent|Write RP or GA at the top and keep its vowel and /r/ conventions consistent.|RP /ˈmelbən/ versus GA /ˈmelbərn/.|Do not mix RP /ɒ/ and omitted /r/ with GA /oʊ/ by accident.
Pass 2: transcribe the words|Ignore spelling traps, use IPA and check lexical stress.|debt /det/; recipe /ˈresəpi/; extraordinary /ɪkˈstrɔːdənəri/ in the RP mock key.|Silent letters have no symbol in the transcription.
Pass 3: add stress and weak forms|Mark stressed syllables and reduce unstressed function words where appropriate.|that /ðət/, an /ən/, of /əv/, to /tə/.|A dictionary transcription of each word is not a fluent-speech transcription.
Pass 4: check boundaries|Look for linking r, assimilation and elision where the task and context call for them.|there is /ðər ɪz/ in the mock.|A word boundary is not necessarily a sound boundary.
Pass 5: audit independently|Check symbols, stress, weak forms, accent consistency and connected speech separately.|Read your transcription back out loud, then compare it with the sentence.|Theory and transcription must each be passed; a strong theory score cannot compensate for transcription.''')
weak=[['a','eɪ','ə'],['an','æn','ən'],['and','ænd','ən(d)'],['at','æt','ət'],['but','bʌt','bət'],['can','kæn','kən'],['for (RP)','fɔː','fə'],['for (GA)','fɔːr','fər'],['from (RP)','frɒm','frəm'],['of (RP)','ɒv','əv'],['of (GA)','ʌv','əv'],['to','tuː','tə'],['that (conjunction)','ðæt','ðət'],['the','ðiː','ðə / ði'],['was (RP)','wɒz','wəz'],['have (auxiliary)','hæv','həv / əv'],['had','hæd','həd / əd'],['you','juː','ju / jʊ']]
# Mixed, authored retrieval questions; the answer is stored as text, never by shuffled position.
questions=[]
def q(topic,prompt,answer,wrong,ex,source=None):
 questions.append(dict(id='q'+str(len(questions)+1),topic=topic,prompt=prompt,answer=answer,options=[answer]+wrong,explanation=ex,source=source or next(t['source'] for t in topics if t['id']==topic)))
q('basics','Which pair is a minimal pair?','price – prize',['bury – berry','thin – than','car – war'],'Only /s/ versus /z/ changes in price–prize. thin–than changes consonant and vowel.')
q('basics','Which notation represents a phone?','[tʰ]',['/t/','<t>','the letter t'],'Square brackets represent phones. Slashes represent phonemes.')
q('basics','Which field studies the physical speech signal?','Acoustic phonetics',['Morphology','Segmental phonology','Syntax'],'Acoustic phonetics studies the physical properties of the signal.')
for word,n,ex in [('child',4,'/tʃ aɪ l d/: the affricate and diphthong each count once.'),('aisle',2,'/aɪ l/: silent s, one diphthong.'),('psyche',4,'/s aɪ k i/.'),('sew',2,'/s əʊ/ in RP, /s oʊ/ in GA.'),('knight',3,'/n aɪ t/: k and gh are not pronounced.'),('Chicago',6,'/ʃ ɪ k ɑː g əʊ/ in RP.'),('exam',5,'/ɪ g z æ m/: x represents two sounds here.'),('knowledge',5,'/n ɒ l ɪ dʒ/ in RP.'),('sword (RP)',3,'/s ɔː d/.'),('sword (GA)',4,'/s ɔː r d/ in the course model.')]:
 q('basics',f'How many phonemes are in {word}?',str(n),[str(i) for i in range(2,8) if i!=n][:3],ex)
for c in consonants:
 answer=f"{c['voice']} {c['place']} {c['manner']}"
 others=[x for x in consonants if x['symbol']!=c['symbol']]
 wrong=[f"{x['voice']} {x['place']} {x['manner']}" for x in sorted(others,key=lambda x:(x['manner']!=c['manner'],x['place']!=c['place']))[:3]]
 q('production',f"Give the full description of /{c['symbol']}/.",answer,wrong,f"/{c['symbol']}/ as in {c['example']}: {answer}.")
 q('production',f'Which symbol is a {answer}?','/'+c['symbol']+'/', ['/'+x['symbol']+'/' for x in others[:3]],f"Think of {c['example']}.")
for v in vowels:
 a=f"{v['height']} {v['backness']} {v['lips']}"
 others=[x for x in vowels if x['symbol']!=v['symbol']]
 q('vowels',f"Describe /{v['symbol']}/ in the course's RP vowel map.",a,[f"{x['height']} {x['backness']} {x['lips']}" for x in others[:3]],f"/{v['symbol']}/ as in {v['example']}. Positions are schematic; exact realizations vary.")
for topic_,prompt,a,wrong,ex in [
('vowels','How many syllabic nuclei does a diphthong form?','One',['Two','Three','It cannot be a nucleus'],'The glide belongs to one nucleus.'),
('vowels','Which RP vowel is typically restricted to unstressed syllables?','/ə/',['/ɜː/','/æ/','/iː/'],'Schwa is the typical reduced vowel.'),
('vowels','What is the GA GOAT vowel?','/oʊ/',['/əʊ/','/ɒ/','/ɔɪ/'],'The course contrasts RP /əʊ/ with GA /oʊ/.'),
('accents','Which transcription is RP?','/kɑː/',['/kɑːr/','/kær/','/kɝː/'],'RP car has no final /r/ in isolation.'),
('accents','Which is a course-accepted GA transcription of bird?','/bɝːd/',['/bɜːd/','/bɪəd/','/bɒd/'],'/ɝː/ or /ɜːr/ represents the rhotic NURSE vowel.'),
('accents','Does non-rhotic mean that /r/ is never pronounced?','No: it occurs before vowels',['Yes, always','Only written rr is pronounced','Only at the end of a sentence'],'RP red contains /r/, as does linking r before a vowel.'),
('allophones','Which onset usually has an unaspirated /p/?','spin',['pin','pill','pie'],'The preceding /s/ in the same onset blocks strong aspiration.'),
('allophones','In RP, which context usually has dark [ɫ]?','milk',['leaf','silly','fall in'],'In milk, /l/ is followed by a consonant.'),
('allophones','The t sounds in top and stop are…','Allophones of one phoneme',['Separate phonemes','Two letters only','Always identical phones'],'Aspiration differs, but the words still use the phoneme /t/.'),
('allophones','The final sounds of pat and pad are…','Separate phonemes',['Allophones of /t/','Always identical','Both /d/'],'The /t/–/d/ contrast distinguishes meaning.'),
('allophones','The vowels in any and red are…','The same vowel phoneme /e/',['/æ/ and /e/','Allophones of /iː/','/ə/ and /e/'],'Both use /e/ in the course model.'),
('syllables','What makes up the rhyme of a syllable?','Nucleus + coda',['Onset + nucleus','Onset + coda','Only onset'],'Rhyme groups the nucleus and any following consonants.'),
('syllables','What is the onset of streets?','/str/',['/st/','/s/','/striː/'],'All three consonants precede the nucleus /iː/.'),
('syllables','What is the CV structure of tasks?','CVCCC',['CCVCC','CVC','CV.CVC'],'/t ɑː s k s/ in RP: one onset C, one V, three coda Cs.'),
('syllables','Can a consonant be a syllable nucleus?','Yes: for example syllabic [n̩]',['No: never','Only /p/','Only in spelling'],'The syllabic nasal in garden can form the second nucleus.'),
('syllables','Which has double (late) stress in the course example?','green house (a house that is green)',['greenhouse (for plants)','hotdog','Church Street'],'A descriptive phrase has later emphasis; Church Street has the Street exception.'),
('syllables','Which compound has early stress?','apple juice',['cheese sandwich','Oxford Road','green house'],'Juice belongs to a group of exceptions mentioned in class.'),
('syllables','Where is the primary stress in photographic?','Third syllable',['First syllable','Second syllable','Fourth syllable'],'/ˌfəʊtəˈgræfɪk/.'),
('weak','Which is an unstressed weak form of can?','/kən/',['/kæn/','/kɑːn/','/kn/'],'The full vowel /æ/ reduces to schwa.'),
('weak','Which form fits the in the apple in neutral speech?','/ði/',['/ðə/ only','/θi/','/dɪ/'],'Apple starts with a vowel sound. /ði/ is the common weak form here.'),
('weak','Which word is normally a content word?','learn',['of','a','to'],'Learn is a lexical verb.'),
('weak','When should can normally take its strong form?','When it is contrastively stressed',['Whenever it is written in capitals in a book title','Always before a verb','Only at the start of a sentence'],'Emphasis or contrast supports the full vowel /æ/.'),
('weak','English stress timing is best understood as…','A tendency for stress to organize rhythm',['Perfectly equal time between stresses','Every syllable lasting equally long','Never reducing vowels'],'It is a teaching model and rhythmic tendency, not exact isochrony.'),
('endings','Which sound ends kids?','/z/',['/s/','/ɪz/','/t/'],'The preceding /d/ is voiced and not a sibilant.'),
('endings','Which plural ending follows a sibilant?','/ɪz/',['/s/','/z/','/ɪd/'],'The sibilants are /s z ʃ ʒ tʃ dʒ/.'),
('endings','Which past ending follows /t/ or /d/?','/ɪd/',['/d/','/t/','/ɪz/'],'Wanted and needed add a syllable.'),
('endings','Which word has /ŋ/ without /g/?','singer',['finger','anger','longer'],'Sing is a complete morpheme; -er is added to it.'),
('connected','In good boy, /d/ becoming [b] is…','Regressive place assimilation',['Progressive voicing assimilation','Elision','Intrusive r'],'The following bilabial /b/ influences the preceding consonant.'),
('connected','Removing /t/ from next day is…','Elision',['Linking r','Aspiration','HappY tensing'],'A segment is deleted.'),
('connected','Which phrase licenses linking r in RP?','four eggs',['four books','four cars','four cats'],'Eggs starts with a vowel.'),
('connected','An r in law and order is called…','Intrusive r',['Linking r in the narrow historical sense','An affricate','Aspiration'],'There is no historical final /r/ in law.'),
('transcription','What must you state on the exam transcription?','Whether you use RP or GA',['Your favourite English accent','A separate accent for every word','Only the number of syllables'],'The course outline explicitly requires an RP/GA indication.'),
('transcription','Which exam parts must be passed?','Theory and transcription separately',['Only the combined score matters','Theory only','Transcription only'],'The course outline states that both parts must be passed.')]:q(topic_,prompt,a,wrong,ex)
for word,a in [('cats','/s/'),('dogs','/z/'),('buses','/ɪz/'),('benches','/ɪz/'),('racks','/s/'),('rags','/z/'),('wishes','/ɪz/')]:q('endings',f'Choose the plural ending in {word}.',a,[x for x in ['/s/','/z/','/ɪz/','/ɪd/'] if x!=a],'Apply the sound-based plural rule; check sibilants first.')
for word,a in [('looked','/t/'),('played','/d/'),('wanted','/ɪd/'),('needed','/ɪd/'),('kissed','/t/'),('turned','/d/')]:q('endings',f'Choose the past-tense ending in {word}.',a,[x for x in ['/t/','/d/','/ɪd/','/ɪz/'] if x!=a],'Check /t d/ first, then the voicing of the final sound.')

passages=[
 dict(id='mock',title='The official mock · Melbourne',text='My friend believes that Melbourne is without a doubt an extraordinary city. There is a variety of things to do at any time of year.',rp='maɪ ˈfrend bəˈliːvz ðət ˈmelbən ɪz wɪðˈaʊt ə ˈdaʊt ən ɪkˈstrɔːdənəri ˈsɪti ‖ ðər ɪz ə vəˈraɪəti əv ˈθɪŋz tə ˈduː ət ˈeni taɪm əv ˈjɪə',ga='maɪ ˈfrend bəˈliːvz ðət ˈmelbərn ɪz wɪðˈaʊt ə ˈdaʊt ən ɪkˈstrɔːrdəneri ˈsɪt̬i ‖ ðər ɪz ə vəˈraɪət̬i əv ˈθɪŋz tə ˈduː ət ˈeni taɪm əv ˈjɪər',source='Mock 3/3 + Moodle transcription solution (30 June 2026)',focus=['Weak forms: that, an, a, of, to, at.','Stress: believes, extraordinary, variety.','Linking r in there is; keep Melbourne and year accent-consistent.'],official=True),
 dict(id='sammy',title='Short practice · Reading',text='Sammy arrived in Reading just after lunch.',rp='ˈsæmi əˈraɪvd ɪn ˈredɪŋ dʒəst ˈɑːftə ˈlʌntʃ',ga='ˈsæmi əˈraɪvd ɪn ˈredɪŋ dʒəst ˈæftər ˈlʌntʃ',source='Wrap-up · p. 7 (RP); GA adaptation for this trainer',focus=['Reading the place is /ˈredɪŋ/.','The source uses reduced just /dʒəst/.','Do not pronounce a linking r before lunch in RP.'],official=False),
 dict(id='jenny',title='Short practice · Jenny',text='Jenny started to make a fence, but got bored, and then found a slug.',rp='ˈdʒeni ˈstɑːtɪd tə ˈmeɪk ə ˈfens | bət gɒt ˈbɔːd | ənd ˈðen faʊnd ə ˈslʌg',ga='ˈdʒeni ˈstɑːrtɪd tə ˈmeɪk ə ˈfens | bət gɑːt ˈbɔːrd | ənd ˈðen faʊnd ə ˈslʌg',source='Wrap-up · p. 7',focus=['Started adds /ɪd/.','Reduce to, a, but and and.','RP/GA: started, got and bored.'],official=True),
 dict(id='rose',title='Short practice · A single rose',text='She bought a single rose.',rp='ʃi ˈbɔːt ə ˈsɪŋgl̩ ˈrəʊz',ga='ʃi ˈbɔːt ə ˈsɪŋgl̩ ˈroʊz',source='Connected speech I · p. 10',focus=['Single contains /ŋg/.','Syllabic /l/ is possible.','Rose ends in /z/; GOAT differs by accent.'],official=True),
 dict(id='ponder',title='Long practice · Mrs Ponder',text="Mrs Ponder picked up her television remote and turned down the volume on Dancing with the Stars. She could hear people shouting.",rp='mɪsɪz ˈpɒndə ˌpɪkt ˈʌp hə teləˈvɪʒn̩ rɪˈməʊt ənd ˌtɜːnd ˈdaʊn ðə ˈvɒljuːm ɒn ˈdɑːnsɪŋ wɪð ðə ˈstɑːz ‖ ʃi kəd ˈhɪə piːpl̩ ˈʃaʊtɪŋ',ga='mɪsɪz ˈpɑːndər ˌpɪkt ˈʌp hər teləˈvɪʒn̩ rɪˈmoʊt ənd ˌtɝːnd ˈdaʊn ðə ˈvɑːljəm ɑːn ˈdænsɪŋ wɪð ðə ˈstɑːrz ‖ ʃi kəd ˈhɪər piːpl̩ ˈʃaʊt̬ɪŋ',source='Transcription_Mrs_Ponder n · selected sentences; spacing normalized',focus=['Picked /t/ vs turned /d/.','Weak her /hə(r)/ and could /kəd/.','Check syllabic consonants and RP/GA vowels.'],official=True),
 dict(id='transfer',title='New transfer practice · A quiet afternoon',text='Her brother wanted to buy a new book, but the shop was closed.',rp='hə ˈbrʌðə ˈwɒntɪd tə ˈbaɪ ə ˈnjuː ˈbʊk | bət ðə ˈʃɒp wəz ˈkləʊzd',ga='hər ˈbrʌðər ˈwɑːntɪd tə ˈbaɪ ə ˈnuː ˈbʊk | bət ðə ˈʃɑːp wəz ˈkloʊzd',source='Authored transfer exercise · one possible model, not an official key',focus=['Wanted /ɪd/ vs closed /d/.','Reduce her, to, a, but, the and was.','Keep brother, wanted, new, shop and closed in one accent.'],official=False)
]
cards=[]
for t in topics:
 for i,r in enumerate(t['rules']):cards.append(dict(id=t['id']+'-'+str(i),topic=t['id'],source=t['source'],**r))
for c in consonants:cards.append(dict(id='sound-'+c['symbol'],topic='production',q=f"Describe /{c['symbol']}/.",a=f"{c['voice']} {c['place']} {c['manner']}",example=c['example'],trap='Use voicing + place + manner.',source='Consonants · pp. 4–22'))
for v in vowels:cards.append(dict(id='vowel-'+v['symbol'],topic='vowels',q=f"Describe /{v['symbol']}/.",a=f"{v['height']} {v['backness']} {v['lips']}",example=v['example'],trap='Height + backness + lip rounding. The map uses traditional RP.',source='Vowels I–II'))
data=dict(words=words,topics=topics,consonants=consonants,vowels=vowels,weak=weak,questions=questions,cards=cards,passages=passages)
(root/'data.js').write_text('window.SOUNDS = '+json.dumps(data,ensure_ascii=False,indent=2)+';\n')
print({k:len(v) for k,v in data.items()})
