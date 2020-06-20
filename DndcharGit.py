#Occupations reference: http://arcana.wikidot.com/list-of-medieval-european-professions
#and http://www.tomcamp.org/misc%20docs/colonial%20occupation.html

import rolling
from twitter import *
from random import choice, randint
from charbios import generateBios

firstname = ['Millicent','Margery','Cecily','Agnes','Roh','Alinor','Bayard','Albin',
              'Edwin','Hugh','Kethleen','Fabricia','Aemilia','Septima','Lucia','Tertius',
              'Alus','Marcus','Primus','Merek','Carac','Tybalt','Sadon','Rowan','Fendrel',
             'Brom','Geoffrey','Leofrick','Leif','Barda','Rulf','Arthur','Bryce','Jarin','Asher',
             'Xalcador','Dain','Gorvenal','Alys','Ayleth','Cedany','Ellyn','Peronell',
             'Thea','Amelia','Thea','Brunhild','Isabel','Muriel','Winifred','Catrain',
             'Gussalen','Luanda','Krea','Dimia','Aleida','Loreena','Seraphina','Ryia',
             'Useult','Elspeth','Faolan','Ebba','Slade','Ash','Thorveig','Annag','Eimhir',
             'Abigail','Alice','Anne','Charlotte','Elisabeth','Eliza','Esther','Hephzibah',
             'Phebe','Ebenezer','Elias','Enoch','Ephraim','Henry','Josiah','Nathan',
             'Nathaniel','Oceanus','Samuell','Thaddeus','Zechariah','Zefuyn','Cuthbert',
             'Merewether','Meruyn','Mesquetta','Moss','Toby','Tobin','Tyler','Sare',
             'Jace','Jarett','Kant','Karr','Kean','Leek','Leggatt',
             ]

lastname = ['Genro','Vana','Triswynn','Umemenor','Kealen','Sweetbow','Rockvale','Ironson',
             'Aimar','Sheepell','Lightfoot','Boldalyon','Sulpicius','Sertorius','Darzar',
             'Inman','Aufidius','Cromwell','deGrey','Drake','Falk','Cleves','Warwick',
            'Ackerg','Goodee','Monetf','Fuxg','Freudg','Crus','Messala','Finni','Malloyei',
            'Mulloyi','Payne','Vace','Vandell','Veall','Vellums','Verco','Verrick', 'Vew',
            'Viaris','Vinicumb','Vogt','Vollotton','Vorsfild','Voules','Vrwin','Zabulon',
            'Zwiefell','Zillwood','Zehender','Aben','Aberg','Aberle','Absolon','Achioson',
            'Adair','Adelstone','Adkeson','Adlamn','Ahern','Ainsworth','Aishton','Albiro',
            'Albris','Allardice','Alsager','Ambrose','Anchant','Annot','Arigan','Arpthorp',
            'Arrow','Artsen','Ascoon','Ascough','Asylam','Athias','Auger','Ayrley','Packharnis',
            'Padgett','Painell','Pairce','Palfrey','Pamflett','Paradine','Parcifield','Perfeck',
            'Parfitt','Pargills','Parguot','Parlan','Parloe','Parskell','Pascor','Paskitt',
            'Pasquali','Pastorella','Pavett','Peadon','Pearh','Pedevin','Pedvint','Peripoint',
            'Pemmel','Pendergast','Penistone','Penrith','Pepperel','Perratt','Phiat','Piercay',
            'Philbean','Pimon','Pitblado','Poartt','Poingdestre','Porneuf','Postlethwaite',
            'Prebble','Prengast','Pringwood','Prinscept','Proughton','Pynyot','Radbourn',
            'Rae','Ralissom','Raintoul','Ramsbotham','Rane','Rankilor','Rasmus','Rattrary',
            'Ravenscroft','Rawden','Rayment','Reddercliff','Reddowck','Regram','Reineck',
            'Rennesson','Renoulles','Rickeuts','Riedmuller','Riedmuller','Roantree',
            'Rocklif','Rosedew','Ros','Roystons','Runce','Runshu','Rybread','Rylance',
            'Rynd','Ryne','Haer','Hailstone','Halloran','Halnone','Hanasen','Hapley',
            'Hanlon','Hanten','Hanygan','Haranton','Harbeart','Harbottel','Harkds',
            'Harourt','Harrow','Havenagh','Hawshire','Haymes','Heberon','Heght','Hellon',
            'Hendtas','Hernbery','Hesketh','Hessletine','Hiccabottom','Bachillor',
            'Bailiss','Ballantyne','Barcuss','Barnicott','Barthomu','Baughurst',
            'Baylis','Bayzard','Beany','Beeck','Bickerstaff','Blacdon','Blankinsop',
            'Blustrode','Bogghurst','Bowditch','Braderick','Brathwaite','Bryett',
            'Buttergree','Caffyn','Callaker','Cantril','Carelton','Carneggy','Carrelles',
            'Carruthers','Carruthers','Casbolt','Cavit','Clandel','Claypitt','Clibra',
            'Clidsdall','Cloke','Coar','Coldicott','Collett','Conbernon','Cradick',
            'Crosthwaite','Mafeit','Mailtwoua','Makettrick','Makrobe','Manktellow',
            'Martineau','Marzden','Matton','Mawburn','Meccue','Moggeridge','Mojger',
            'Morle','Mynshal','Yallowdy','Yearnold','Ymmerseel','Youle','Yuil','Wadam',
            'Waithman','Wagnieres','Wasborow','Wathlake','Wedgewood','Weithuck','Wimpory',
            'Withe','Witse','Wogdn','Wollet','Wyet','Wyrm','Uloft','Usler','Uttley',
            'Taige','Tanqweriel','Tewkxberry','Thooren','Thwaites','Tisoe','Treby',
            'Treloar','Trice','Tutnaill','Twomey','Twomey','Twomey','Sintglain',
            'Salkeld','Sarvis','Scarfe','Sibthorpe','Siferin','Skegg','Sterk','Strugnell',
            'Sym','Synnett','Jams','Jee','Jolliff','Journeaux','Kaan','Kebel','Keeho',
            'Keist','Kennifick','Kinsmellagh','Klemon','Kuce','Laen','Lafosse','Laithnait',
            'Lantellum','Lanxon','Lassendy','Lauclund','Leveric','Liddiard','Lidyatt',
            'Littlo','Logsdell','Lunniss','Nelmns','Nokes','Nutt','Nycholls','Oats',
            'Ogg','Quirm',
            ]

adjective = ['agreeable','alert','alluring','ambitious','agressive','arrogant',
             'abrasive','antisocial','apathetic','brave','boastful','bossy','careful',
             'calm','cultured','careless','clingy','cowardly','cruel','childish',
             'confrontational','cynical',
             'charming','courteous','creative','deceitful','dishonest','decisive','diplomatic',
             'determined','disorganized','disrespectful','evasive','greedy','grumpy','eclectic',
             'emotional','exuberant','forceful','forgetful','flaky','frivolus',
             'funny','fussy','generous','gentle','gossipy','grumpy','gullible',
             'hard-working','honest','haughty','impatient','indecisive','jolly',
             'jealous','lucky','modest','mischievious','morbid','moody',
             'narrow-minded','nervous','nosy','overcritical',
             'optimistic','persistent','philosophical','polite','paranoid','pessimistic',
             'pushy','quick-witted',
             'quiet','rational','reliable',
             'rude','romantic','sedate','shrewd','studious','successful','selfish',
             'self-destructive','stingy','stubborn','superstitious',
             'shy','sensitive','tidy','thrifty','tough','unassuming','unhappy',
             'vain','verbose','whiny']

race = [('dragonborn',2,0,0,0,0,1),('dwarf',0,0,2,0,0,0),('elf',0,2,0,0,0,0),('gnome',0,0,0,2,0,0),
        ('half-elf',0,0,0,1,1,2),('halfling',0,2,0,0,0,0),('half-orc',2,0,1,0,0,0),('human',1,1,1,1,1,1),
        ('tiefling',0,0,0,1,0,2),('orc',2,0,1,-2,0,0),('leonin',1,0,2,0,0,0),('satyr',0,1,0,0,0,2),
        ('aarakocra',0,2,0,0,1,0),('genasi',0,0,2,0,0,0),('goliath',2,0,1,0,0,0),('aasimar',0,0,0,0,0,2),
        ('bugbear',2,1,0,0,0,0),('firbolg',1,0,0,0,1,0),('goblin',0,2,1,0,0,0),('hobgoblin',0,0,2,1,0,0),
        ('kenku',0,2,0,0,1,0),('kobold',-2,2,0,0,0,0),('lizardfolk',0,0,2,0,1,0),('tabaxi',0,2,0,0,0,1),
        ('triton',1,0,1,0,0,0),('yuan-ti',0,0,0,1,0,2),('tortle',2,0,0,0,1,0),('changeling',0,0,0,0,1,2),
        ('kalashtar',0,0,0,0,2,1),('shifter',0,0,0,0,0,0),('warforged',1,0,2,0,0,0),('centaur',2,0,0,0,1,0),
        ('loxodon',0,0,2,0,1,0),('minotaur',2,0,1,0,0,0),('vedalken',0,0,0,2,1,0),('locathah',2,1,0,0,0,0)]

occupations = ['cowherd','dairymaid','gardener','farmer','goatherd','horse trainer',
               'ostler','shepherd','swineherd','climmer','falconer','hunter','fewterer',
               'molecatcher','rat catcher','fisherman','leech collector', 'oyster raker',
               'seaweed harvester',"artist's model",'painter','sculptor','composer',
               'playwright','poet','shoemaker','tailor','jeweler','mason','carpenter',
               'weaver','baker','butcher','blacksmith','roofer','locksmith','ropemaker',
               'tanner','rugmaker','vaginarius','armorsmith','arrowsmith','bladesmith',
               'basketmaker','beekeeper','bog iron hunter','bone carver','bookprinter',
               'cartographer','clockmaker','cheesemaker','diamantaire','grave digger',
               'ivorist','lacemaker','netmaker','parchmenter','perfumer','pinmaker',
               'physician','quarryman','sailmaker','tapestrymaker','weaver','bandit',
               'burglar','charlatan','conman','pickpocket','poacher','camp follower',
               'cortesan','actor','bard','singer','guard','diplomat','jailer','judge',
               'watchman','alchemist','apothecary','barber-surgeon','midwife','nurse','pissprophet',
               'toad doctor','banker','innkeeper','ragpicker','shrimper','bodyguard','cook','monk',
               'nun','priest','minister','ferryman','herbalist','librarian','mathematician','philosopher',
               'professor','tutor','scribe','servant','porter','laundress','dog trainer','dung carter',
               'executioner','fortune teller','nightsoil man','rag and bone man','stablehand','tax collector',
               'sin-eater','beggar','housewife','pilgrim','transient','messanger',
               'herb strewer','town crier','astrologer','winemaker','brewer','candlemaker',
               'bloodletter','glassmaker','bonesetter','landlord','toll collector','hair dresser',
               'barber','auctioneer','cheeseman','coroner','day laborer','goose herd',
               'portable soup maker','potato badger','schoolmaster','teacher','soapmaker',
               'spicer','surveyor','mole catcher'
               ]

charStats = rolling.randomRollMethod()
raceStats = (choice(race))
fname = choice(firstname)
newDude = (f'{fname} {choice(lastname)} the {choice(adjective)} {(raceStats[0])} {choice(occupations)}. \n'
      f'{fname}{generateBios()} \n'
      'Strength: ' + str(charStats[0] + raceStats[1]) + '\n'
      'Dexterity: ' + str(charStats[1] + raceStats[2]) + '\n'
      'Constitution: ' + str(charStats[2] + raceStats[3]) + '\n'
      'Intelligence: ' + str(charStats[3] + raceStats[4]) + '\n'
      'Wisdom: ' + str(charStats[4] + raceStats[5]) + '\n'
      'Charisma: '+ str(charStats[5] + raceStats[6]) + '\n'
      )

t.statuses.update(
    status=newDude)
