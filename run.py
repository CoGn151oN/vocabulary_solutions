from gtts import gTTS
from pydub.audio_segment import AudioSegment as aseg


hungarian = {
"pitää paikkansa": "megállja a helyét",
"tunnen unkarilaista jarjestelmää": "ismerem a magyar rendszert",
"jotkut on kunnossa ja jotkut ei oli kunnossa ": "van amelyik okés és van amelyik nincs",
"hän selittää hyvin ": "ő jól magyaráz",
"tästä alkaen ": "innentől kezdve",
"se kuulostaa hyvältä ": "jól hangzik",
"hänen hajuvesi tuoksuu hyvältä ": "jó illata van a parfümnek",
"maista sitä ": "kóstold meg ezt",
"tulen juoksemisesta (elatívus) ": "futásból jövök",
"mitä enemmän juoksen, sitä enemmän pitää levätä ": "minél többet futok, annál többet kell pihenni",
"joka toinen päivä ": "minden második nap",
"vartalolle täytyy levätä ": "a testnek muszáj pihenni",
"kun etäisyys pidentyy ": "ahogy nő a távolság",
"ohimennen materiaalin läpi ": "futólag áthaladtam az anyagon",
"hänen vänhä autonsa ei lähde käyntiin ": "az ő öreg autója nem indult be",
"kenties mikä totuus on ": "mit tudom én mi az igazság",
"perusteellinen syy ": "alapos indok",
"Näin perusteellinen pesu tälle sillalle tehdään joka ": "A híd ilyen alapos mosását minden alkalommal elvégzik",
"kaksi vuotta sitten vuokrani oli 200 euroa ": "két évvel ezelőtt a bérleti díjam 200 euró volt",
"Säännöllinen yöjuna Ruotsista Saksaan kulkee ehkä jo kahden vuoden päästä ": "Talán két év múlva indul egy rendszeres éjszakai vonat Svédországból Németországba",
"kahden vuoden kuluttua minulla on tutkintotodistus ": "két év múlva diplomám lesz",
"vuosi sitten olin vielä Kanadassa ": "egy évvel ezelőtt még kanadában voltam",
"kahden vuoden mennessä ": "két éven belül",
"sopimus kestää kaksi vuotta ": "a megállapodás két évig tart",
"Popeye syö paljon pinaattia ": "Popeye sok spenótot eszik",
"auto on hidas, joten se menee hitaasti ": "lassú az autó, ezért lassan megy",
"lähdetkö illalla leffaan? ": "elmész-e este a moziba?",
"olisin halunnut mennä suomessa ": "szerettem volna finnországba menni",
"katsommetaan telkkari illalla ": "nézzünk tévét este",
"monet kauniit tytöt kuorsaavat ": "sok szép nő horkol",
"vaihtelun vuoksi ekseema haluaa rahaa ": "változatosság kedvéért pénzt akar az exem",
"siihen mennessä ": "addig",
"jos opiskelija ei maksa maksua siihen mennessä ": "ha a hallgató addig nem fizeti meg a díjat",
"olet kokonaan / aivan oikeassa ": "teljesen igazad van",
"menen Tallinnaan perheen luokse ": "Tallinnba megyek a családomhoz",
"Olen Elenan luona ": "Elenánál vagyok",
"tuolen mummon luota ": "a nagyitól jövök",
"luokse luona luota ": "Jonny-hez, -nál, -tól",
"vielä kaksi minuuttia ": "még 2 perc",
"lapsi on jo aikuinen ": "már felnőtt a gyerek",
"Miltä sinun talo näyttää? ": "hogy néz ki a házad?",
"Joo, se just ": "ja, így van",
"miltä mun tukka näyttää? ": "milyen a hajam?",
"sitä ei kannata tehdä ": "azt nem érdemes csinálni",
"minä leikaan partaani itse ": "vágom a saját szakállamat",
"minullekin ": "nekem is",
"kenellekään ": "senkinek se",
"ei minullekaan ": "nekem se",
"kukaan ei tiedä ": "senki se tudja",
"koko ajan ": "egész idő alatt, mindig, folymatosan",
"olen matkalla kotiin ": "Úton vagyok haza",
"Anteeksi, että olen myöhässä. ": "elnézést a késésért",
"Elenan luo kylään ": "Elenához",
"en mene enää minnekään ": "már sehova se megyek",
"minun takkia ": "miattam",
"valikoimaon parempi Suomessa ": "finnországban jobb a kínálat",
"se kuulostaa kyvältä ": "jól hangzik",
"kun oli niin paljon liikennettä ": "mikor olyan sok volt a forgalom",
"oli vaikea löytää parkkipaikka ": "nehéz volt parkolóhelyet találni",
"mitäpä tässä ": "semmi különös",
"Moni on ilman työtä ": "sokan vannak munka nélkül",
"En mä ole ihan varma ": "nem vagyok én ebben olyan biztos",
"Mä tulen takaisin vasta sunnuntai-iltana ": "csak vasárnap este jövök vissza",
"mutta muista kuitenkin että ": "de ne felejtsd el hogy",
"ennen kun hän palaa kotiin ": "amielőtt ő haza ér",
"haluan viela lisää ruokaa ": "szeretnék még ételt",
"haluaisin viela enemmän rahaa ": "még több pénzt akarok",
"me olemme opiskelleet suomea enemmän kuin puoli vuottaa ": "mi már több mint fél éve tanulunk finnül",
"minä pyydän sinua tekemään jotain ": "megkérlek, hogy csinálj valamit",
"saanko saattaa Saatanan satamaalle? ": "kikísérhetem a Sátánt a kikötőre?",
"kylven ammeessa ": "kádban fürdök",
"minä alan opiskella ": "elkezdek tanulni",
"näyttää siltä ": "úgy néz ki",
"minä aloitan kurssin ": "elkezdem a kurzust",
"kurssi alkaa tänään ": "ma kezdődik a kurzus",
"alan opiskella ": "kezdek tanulni",
"hän muutti mielensä ": "meggondolta magát",
"nyt hyppää apina vetteen ": "most ugrik a majom a vízbe",
"menen tulevaisuudessa ": "menni a jövőben",
"menin menneisyydessä ": "mentem a múltban",
"ennen huhtikuuta ": "április előtt",
"huhtikuun mennessä ": "áprilisig",
"asun täällä huhtikuun asti ": "itt lakom áprilisig",
"lähetän sinulle huhtikuun mennessä ": "elküldöm neked áprilisig",
"kirjoitan kirjeen hotellille ": "levelet írok a szállodának",
"minä tulen asemalle teitä vastaan ": "kimegyek elétek az állomásra",
"hyvä tyyppi ": "jó fej",
"hän ei ajattelee mitään sellaista ": "ő nem gondol semmi ilyesmit",
"sieltä on kaunis näköala ": "onnan szép a kilátás",
"koko konkkaronkka ": "egész csipetcsapat, siserehad",
"minulla on sekalaisporukka ": "vegyes csoportom van",
"mennä kylään ": "látogatóba menni'",
"olla kylässä ": "látogatóban lenni",
"on vielä paljon jäljillä ": "sok van még hátra",
"olen jälkijunassa ": "le vagyok maradva",
"minä en mennyt mihinkään/minnekään ": "nem mentem sehova",
"mennään johonkin ": "menjünk valahová",
"hän on suht vänhä ": "ő eléggé öreg",
"yhä älykkäämpi ": "egyre okosabb",
"tulevasuudessa ": "jövőben",
"syksyllä aloitan uutta projektia ": "ősszel kezdek új projektet",
"kaikki unkarilaiset on kiukkuiset ": "minden magyar hisztis",
"minusta se on liiottelua ": "szerintem ez túlzás",
"ongelma tulivat esille ": "előjött a probléma",
"jaavat yhteen ": "együtt maradni",
"asiat, jotka liittyvät toisiaan ": "egymáshoz kapcsolódó dolgok",
"olisi pitänyt ostaa ": "kellett volna venni",
"se oli halvempi, kuin ennen ": "olcsóbb lett mint volt",
"äläs nyttä ": "ne már",
"hän harrastaa nyrkäily ": "ő boxol",
"Silloin hän on paikalla ": "Mert ő van a helyen",
"Lakkasitko jo itkemasta? ": "Abbahagytad már a sírást?",
"huolehtiä jostakin ": "gondoskodni valamiről",
"minua huolestuttaa ": "engem aggaszt",
"puin päälle ": "felöltöztem",
"Eduskunnan päätös oli yksimielinen eli kukaan kansanedustaja ei vastustanut erottamista ": "A Parlament döntése egyhangú volt, vagyis egyetlen képviselő sem ellenezte az elbocsátást",
"Betty ei enää luottanut häneen ": "Betty már nem bízott benne",
"Epäselvyyksiä oli esimerkiksi Bobbin matkakuluissa ja muussa viraston rahojen käytössä ": "Voltak kétértelműségek például Bobby útiköltségeiben és az ügynökség pénzének egyéb felhasználásában",
"muualla maassa on aurinkoista ": "az ország többi része napos",
"kerran kuussa ": "egyszer a hónapban",
"kaksi kertaa kuussa ": "kétszer egy hónapban",
"ei ole pakko työskennellä niin usein ": "nem kell olyan gyakran dolgozni",
"vaihtelun vuoksi ": "a változatosság kedvéért",
"jonkin ajan kuluttua ": "valamennyi idő elteltével",
"he päättivät mennä naimisiin seuraavana kesänä ": "úgy döntöttek mennek összeházasodnak következő nyáron",
"He halusivat perustaa perheen yhdessä ": "családot akartak alapítani együtt",
"He päättivät pitää häät kesällä ": "Úgy döntöttek nyáron tartják a lakodalmat",
"he valmistelivat hääjuhlaa ": "előkészítik az esküvői bulit",
"He eivät voineet pitää juhlaa kotona, koska heidän asuntonsa oli niin pieni ": "nem tudtak otthon bulit tartani mert túl kicsi a lakás",
"Ravintolaan ei päässyt autolla, vaan se sijaitsi pienellä saarella kaupungin edustalla. Kaikki kulkivat sinne ve-neellä. ": "Az étterembe nem lehet autóval menni, hanem ez egy szigeten helyezkedik el a város előtt. Mindenki csónakkal járt oda.",
"Anne oli hermostunut ja valvoi koko yön ": "Anne ideges volt és felügyelte egész éjjel",
"He eivät olleet nähneet pitkään aikaan ": "Hosszú ideje nem látták egymást"}

english = {
"tavalliset ihmiset": "ordinary people",
"hän on töissä suuressa yrityksessä": "she works for a large company",
"tuo yritys harjoittaa markkinointia": "that company deals with marketing",
"hän on kotoisin Virosta": "she is from Estonia",
"hän on töissä": "she is working in, or, she is working at",
"hän on taas myöhässä töistä": "she is late for work again",
"Kuinka vanha sinä olet?": "How old are you?",
"he ovat naapureita": "they are neighbours",
"hän on naapurini": "she's my neighbour",
"hän asuvat Puistotiellä Helsingissä": "she lives at Park Way in Helsinki",
"hän asuu yksin": "she lives alone",
"hän on töissä pankissa": "she works in a bank",
"hän opettaa päiväkodissa": "she teaches in kindergarten",
"She forgot her shoes at school again. It`s the second time this week already, and it's only Tuesday. She is so forgetful, but at least she is pretty.": "Hän unohti kengänsä koulussa jälleen. Se on jo toinen kerta tällä viikolla, ja se on vasta tiistaina. Hän on niin unohtava, mutta ainakin hän on kaunis.",
"tutustuminen toisiinsa": "getting to know each other",
"Anteeksi, että oli liian nopea. Voitko sanoa sen taas hitaasti. Miten se kirjoitetaan?": "Sorry, that was too fast. Can you say it again slowly. How do you spell it? (written)",
"entä rahat, jotka olet minulle velkaa": "what about the money you owe me",
"keskiviikkoina käytämme aina vaaleanpunaista vaatteita": "on Wednesdays we always wear pink clothes",
"Haluatko tietää salaisuuden? Mutta älä kerro kenellekään, koska minun täytyy tappaa sinut. Kukaan meistä ei koskaan käytä alushousuja, koska olemme suurimpia lutkat toimistossa.": "Want to know the secret? But don't tell anyone, because I`ll have to kill you. None of us ever wear underwear, because we are the biggest sluts in the office.",
"Kaksituhatta neljäsataa kolmekymmentä kahdeksan jaettuna viidelläkymmenellä kolmella, kaksikymmentä yhdeksällä, miinus sata kahdeksankymmentäkahdeksan vastaa yhtä monta numeroa, jota en halua kertoa sinulle": "2438 / 53 x 29 - 188 = a number I don`t care to tell you",
"toissapäivänä oli lauantai, eilen oli sunnuntai, Tänään on maanantai, huomenna on tiistai, ylihuomenna on keskiviikko,": "day before yesterday was Saturday, yesterday was Sunday, today is Monday, tomorrow is Tuesday, day after tomorrow will be Wednesday",
"Tänään on aika tylsää. Eilen oli kauheaa, minulla oli erittäin huono krapula. En voinut nousta sängystä koko päivän. Makasin vain sängyssä ja join Gatoraden. Mutta toissapäivänä oli erittäin hyvä. Tapasin kaksi vaaleaa tyttöä juhlissa, ja minulla oli kolmikko. Yksi on tulossa huomenna, ja panen toisen ylihuomenna.": "Today is pretty boring. Yesterday was terrible, I had a very bad hangover. I couldn't get out of bed all day. I just lay in bed and drank Gatorade. But the day before yesterday was very good. I met two blonde girls at a party, and had a threesome. One is coming over tomorrow, and I`m sleeping with other one after tomorrow.",
"ärsyttävä kissa puristaa ruokaa ääneen": "the annoying cat is chewing her food loudly",
"luokassa on paljon kauniita tyttöjä": "there are a lot of pretty girls in the class",
"kyllä, älä huoli, voin tehdä sen": "yes, don´t worry, I can do that",
"tietysti olet tervetullut": "of course you're welcome",
"tietysti olet oikeassa": "of course you are right",
"Minkämaalainen sinä olet?": "What country are you from?",
"Tykkään urheilla, käydä vaelluksella vuorilla ja juhlia niin kuin ei ole huomenna": "I like to play sports, go hiking in the mountains, and party like there is no tomorrow",
"Muut opiskelijat menivät kotiin, mutta Lexa ja Jenna kävivät ostoksilla. Lexa päätti ostaa kenkäparin ja pullon vodkaa. Jenna ei ostanut mitään, koska hän ei ole rikas ja hänen täytyy säästää rahaa.": "The other students went home, but Lexa and Jenna went shopping. Lexa decided to buy a pair of shoes and a bottle of vodka. Jenna did not buy anything, because she is not rich and has to save money.",
"venäläinen malli nauhoittaa Camsodan maksamaan koulusta": "the russian model strips on Camsoda to pay for school",
"sitten hän vei vaatteensa pois ja meni suihkuun": "then she took her clothes off and went to shower",
"onneksi hän muisti harjata hampaat ennen haastattelua": "luckily he remembered to brush his teeth before the interview",
"tuuli puhalsi Marylinin hameen, joten hän istui nurmikolla puistossa": "the wind blew up Marylin`s skirt so she sat on the grass in the park",
"se ei ollut onnettomuus. Lyötte tarkoituksella takapuoleni. Näen sinun merkkisi suoraan täällä": "it was not an accident. You intentionally slapped my butt. I can see your handmark right there",
"entä sinä Jenna, mistä olet kotoisin, ja mikä on äidinkielesi": "what about you Jenna where are you from and what is your mother tongue",
"hän ajaa bussipysäkillä matkalla kotiin": "she drives by the bus stop on her way home",
"ruokakauppa on lähellä juna asemaa": "the grocery store is close to the train station",
"Pohjois-Korea ei ole niin mukava kuin Etelä-Korea": "North Korea is not as nice as South Korea",
"Hyvät elokuvat eivät ole Länsi-Saksasta, vaan Itä-Saksasta": "The good movies are not from West-Germany, but from East-Germany",
"pohjoinen, itä, etelä, länsi": "North, East, South, West",
"minäkin haluaisin myös kahvia, kiitos": "I (also) would like some coffee too, please",
"tiet ovat selkeät, voimme ajaa nyt": "the roads are clear, we can drive now",
"-kin": "also",
"tuleeko joku muu liittymään sinuun tänään?": "will there be anyone else joining you tonight?",
"se on hyvä hinta lipulle": "that is a good price for a ticket",
"En pidä kolikoista, pidän parempana seteleitä": "I don't like coins, I prefer bills",
"hän rentoutuu lämpimässä kylvyssä pitkän päivän jälkeen": "she relaxes in a warm bath after a long day",
"kaikilla miehillä on oltava partat ja tatuoinnit": "all men must have beards and tattoos",
"Vapaus ei ole vapaa, tiedät": "freedom is not free you know",
"sitten ansaitse se": "then go and earn it",
"mitä luulet tekeväsi": "what do you think you're doing",
"Korjaa kaikki elämäsi virheet, jos haluat olla täydellinen": "Correct all the errors in your life if you want to be perfect",
"voitko sanoa sen englanniksi, en tiedä sitä suomeksi": "can you say it in english, I don't know that in finnish",
"on hassua, että luulet olevan hauska": "it's funny that you think you're funny",
"maanantaisin katson elokuvia suomeksi": "on Mondays I watch movies in finnish",
"Aamulla hän yleensä istuu keittiössä ja lukee uutisia": "In the morning she usually sits in the kitchen and reads the news",
"asunto on pieni ja siksi me muutamme elokuussa": "the apartment is small and therefore we are moving in August",
"Täällä on nyt lämmin ilma. On kaksikymmentäviisi astetta ja aurinko paistaa. Suomen kesä on kaunis. Yöllä on joskus vaikea nukkua, koska on valoissa.": "There is warm air here now. It is twenty-five degrees and the sun is shining. The Finnish summer is beautiful. At night it is sometimes difficult to sleep, because it is bright.",
"toivottavasti hän ymmärtää, että tarvitsen enemmän kuin yhden naisen": "hopefully she will understand that I need more than one woman",
"Palauta tämä paketti lähettäjälle, koska vastaanottoosoitetta ei ole. Ihmiset ovat tyhmiä joskus.": "Return this package to the sender as there is no receiving address. People are stupid sometimes.",
"Kirjan nimi on Terveisiä pelistä. Siinä on sanoja, lauseita, kappaleita ja kappalet. Jokaisella sivulla.": "The title of the book is Greetings from the Game. It has words, sentences, paragraphs, and chapters. On every page.",
"Opiskelija-asunnossa on melkein kaikkia tyttöjä, joten toivottavasti ilma ei haise kaloilta": "There are almost all girls in the student housing, so hopefully the air doesn't smell like fish",
"ilma makuuhuoneessa on viileää, muista sulkea ikkuna": "the air in the bedroom is cool, remember to close the window",
"Pakkanen sulaa siksi ulkona on helle ja selkea": "The frost is melting because it is hot and clear outside",
"se on sumuista ja viileää ulkona": "it is foggy and cool outside",
"Sataa sadetta ja ukkosta. Eilen satoi myös.": "It is raining sleet and thundering. It was raining yesterday too.",
"Myrsky on ja se on tuulinen, ja Marilynin mekko nousee tuulen kohdalta": "There is a storm and it is windy, and Marilyn's dress will rise up from the wind",
"Kiitos kaikesta avustasi": "thanks for all your help",
"mitä se tarkoittaa": "what does it mean",
"Talvella päivä on lyhyt jä yö on pitkä, valoisaa on vain pari tuntia päivässä": "In the winter the day is short and the night is long, it is only bright for a couple of hours a day",
"kenellä on se sitten": "who has it then",
"kenen sitten": "whose then",
"Etsittekö työntekijöitä? Etsin baarimikon tai tarjoilijan työtä. Minulla on paljon kokemusta. Tässä on CVni.": "Are you hiring? I am looking for a bartender or waiter job. I have a lot of experience. Here is my CV.",
"minullä ei ole töitä suomessa vielä, mutta minä etsin työpaikkaa": "I don´t have a job in Finland yet, but I`m searching for a workplace",
"Jenna ei ole pitkä. Hän on lyhyt ja hoikka, mutta ei laiha. Hänen ystävänsä Andyllä on isot tissit. Molemmilla tytöillä on vaaleat hiukset. Jennalla on ruskeat silmät ja Andyllä siniset silmät. Kumpikaan ei ole ujo, mutta ovat molemmat rehellisiä.": "Jenna is not tall. She is short and slim, but not skinny. Her friend Andy has big boobies. Both girls have blonde hair. Jenna has brown eyes and Andy has blue eyes. Neither is shy, but theyre both honest.",
"Hän on iloinen puhelias nainen, mutta viettää tunteja kylpyhuoneessa suoristaen kiharaisia hiuksiaan.": "She's a cheerful talkative woman, but she spends hours in the bathroom straightening her curly hair.",
"Bussikuski on iso rasvaa vatsa ja viikset niin hän näyttää Mario": "The bus driver has a big fat belly and moustache so he looks like Mario",
"Minkänäköinen hän on?": "What does she look like?",
"Hänellä on pitkä vaalea suora tukka, siniset silmät ja silmälasit. Hän on pitkä, hoikka ja nätti": "She has long blond straight hair, blue eyes and glasses. She is tall, slim and pretty",
"Sinun on täytettävä lomake henkilökohtaisilla tiedoillasi ja annettava se sihteerilleni tarkistettavaksi": "You need to fill out the form with your personal information and give it to my secretary to review",
"Ensin avaat naiselle oven, sitten kun hän alkaa kiittää sinua, keskeytät hänet välittömästi sanoen: älä huoli rakas, sen vaikea tehdä.": "First you open the door for the lady, then when she starts to thank you, you immediately interrupt her saying: don't worry dear its hard to do.",
"hänen parvekekoti on korkeassa harmaassa kerrostalossa": "her balcony home is in a tall gray apartment building",
"älä hyppää uima-altaan matalaan päähän": "don't jump into the shallow end of the pool",
"Minusta Jenna on tosi nätti": "I think Jenna is really pretty",
"viime aikoina": "lately, recently",
"huolehtii lounaasta": "he takes care of lunch",
"ottaa huomioon": "take into consideration",
"ei ole ihme, että": "no wonder that",
"ja niin edelleen": "and so on",
"jäädä pois": "to get off",
"herätyskello kainalossa": "with the alarm clock under his armpit",
"sinun kannattaa ostaa kirja": "you should buy a book",
"kerta kaikkiaan": "once and for all",
"eipä kestää": "don't worry about it",
"minulla on kiire koko talven": "I'm busy all winter",
"kuka kukin on": "who is who",
"ottaa kyytiin": "pick someone up",
"minun on pakko oppia": "I have to learn",
"taivas on pilvessä": "the sky is cloudy",
"silloin tällöin": "here and there",
"hänellä ei ole tapoja": "she doesn't have manners",
"ynnä muuta": "and so on",
"Voisitteko suositella jotain?": "can I get you anything else?",
"Haluaisitko vielä jotain?": "would you like anything else?",
"Mitä saisi olla?": "how can I help you?",
"taas täällä": "over here again",
"vai niin": "is that so..",
"totta kai": "of course"
}

silence = aseg.silent(duration=2000)
intermission = aseg.silent(duration=1200)
i = 1

for k, v in english.items():
        print(i, k, v)
        fin = gTTS(text=k, lang='fi', slow=False)
        fin.save(f'{i}_fin.mp3')
        tra = gTTS(text=v, lang='en', slow=False)
        tra.save(f'{i}_tra.mp3')

        ogkush = aseg.from_mp3(f'C:/Users/dblin/PycharmProjects/Estonian_Vocab_1000/{i}_fin.mp3')
        trakush = aseg.from_mp3(f'C:/Users/dblin/PycharmProjects/Estonian_Vocab_1000/{i}_tra.mp3')

        wazz = ogkush + silence + trakush + silence + ogkush + silence + intermission
        wazz.export(f'C:/Users/dblin/PycharmProjects/Estonian_Vocab_1000/__{i}_wazz.mp3', format='mp3')
        i += 1