import numpy as np
import os



#speakerlist = pd.read_csv(r'speakerlist.csv')

cyan = '#00FFFF'
pink = '#FF00FF'

def assemble(codes):
    output = ''
    for i in codes:
        output=output+i+'\n\n'
    return output

def generate_date_string(i,old=1):
    n_talks = len(i['speakers'])
    if old:
        html = "\n\nThe <span style='color: "+cyan+"'>"+i['date']+"</span> <span style='color: "+pink+"'>Public Works</span> event featured "+str(n_talks)+" talks:\n\n<br><br>"
    else:
        html = "\n\nThe <span style='color: "+cyan+"'>"+i['date']+"</span> <span style='color: "+pink+"'>Public Works</span> event will feature "+str(n_talks)+" talks:\n\n<br><br>"
    return html

    

def generate_s_list(s_list,old=1):
    html = ''

    allcodes = []
    for i in s_list:
        datecode = generate_date_string(i,old)
        count = 1
        talk_codes = [datecode,]
        for j in np.arange(len(i['speakers'])):
            if count%2:
                color = [cyan,pink]
            else:
                color = [pink,cyan]
            if count ==1:
                flavorcode = "A <i>"+i['flavors'][j]+"</i> talk:\n"
            else:
                flavorcode = "\n\n<br><br>and a <i>"+i['flavors'][j]+"</i> talk:\n"
            titlecode = "<h3><span style='color: "+color[0]+"'>"+'"'+i['talk_titles'][j]+'"</span></h3>'
            authorcode = "<span style='color: "+color[1]+"'> by "+i['speakers'][j]+"</span>\n<br>"+i['position'][j]+"\n<br>\n<br>"
            abstractcode = i['abstracts'][j]
            assembledcode = assemble([flavorcode,titlecode,authorcode,abstractcode])
            talk_codes.append(assembledcode)
            count +=1
        eventcodes = assemble(talk_codes)
        allcodes.append(eventcodes)
        allcodes.append('<br><br><br><br>') #add some space to delineate different nights
    allcodes = assemble(allcodes)
        
    return allcodes

            
    


with open('preamble.html', 'r') as file:
    preamble = file.read()

with open('about.html', 'r') as file:
    about = file.read()

with open('footer.html', 'r') as file:
    footer = file.read()

with open('datetime.html', 'r') as file:
    datetime = file.read()

with open('crowd.html','r') as file:
    crowd = file.read()



oct5 = {'date':'October 5th',
        'year':'2022',
        'speakers': ['Dr. Seth Koproski','Dr. Zach Ulibarri'],
        'flavors': ['humanities','physics'],
        'position': ['a Lecturer in Cornell\'s Dept. of Literatures in English','a Postdoc in Cornell\'s Mechanical and Aerospace Engineering Dept.'],
        'talk_titles':['Did We Believe in Dragons?: Fantastic Animals and the Medieval North Atlantic','A Song of Ice and Dust, or: Why We\'re Sending a 40 Million Dollar Flying Trash Can to Europa'],
        'abstracts': ['Stories of phoenixes, werewolves, unicorns, and dragons fill our media, our libraries, and our minds-- yet, for some reason, we tend to think of medieval people as "silly" or "superstitious" for engaging with these same mythic animals. We understand that these creatures are not and were never "real", but they have served the needs of human writers and storytelling for millennia, including today. This talk is about taking these animals, and medieval belief in general, seriously, asking: Why do these beliefs exist and how were these beliefs practiced? In what books and in what places can we find fantastic animals? And what can the (non)existence of the dragon tell us about how medieval people constructed the world around them?',
                      'If you wanted to search for aliens in our very own solar system, where would you look?<br>    What types of signals or measurements could convince you that life is actually there?    <br>    Why is the University of Colorado building a $40 million flying trash can and sending it to Europa?    <br>    How can a flying trash can find signs of habitability or even potentially alien life?    <br>    What in the world does any of that have to do with dust?    <br>Find out at the inaugural Public Works!']
        }
        
nov2 = {'date':'November 2nd',
        'year':'2022',
        'speakers': ['Dr. Eve Snyder','James Nagy'],
        'flavors':['history','humanities'],
        'position': ['Historian at The History Center in Tompkins County and Project Director of HistoryForge',''],
        'talk_titles':['Who Lived Here? Using HistoryForge to Engage People in Local History in Ithaca, NY and Beyond',
                       'Pity, Compassion, and Mercy in Tolkien\'s Writings'],
        'abstracts': ['Have you ever walked down a street and had something about an old building capture your eye? Perhaps an interesting architectural detail caused you to wonder when a house was built, who lived there, and what their lives were like? Ithaca\'s buildings and people of the past can serve as an important entry point into this community\'s history but what then? What does it take to encourage meaningful public engagement with history? Digital history projects have the potential to increase public engagement with the subject matter, but how can they avoid the trap of presenting a curated version of history that limits additional inquiry.<br><br>This talk is about <a href = "https://tompkins.historyforge.net/">HistoryForge</a>, an open-source digital history project from The History Center in Tompkins County that aims to engage the public in historical inquiry at all levels of the project\'s development: from helping to build the project\'s historical infrastructure by creating map layers and transcribing census records, to querying the resulting census data to learn more about the community and exploring the results on historic map layers.',
                      'Among Tolkien\'s many themes, pity, compassion, and mercy stand out as primary motivating elements for the narrative and the characters within it. Tolkien consistently treats these three as intrinsic virtues in a world full of suffering and loss. Explore the centrality of these themes to Tolkien, his world, and today. ']
        }


dec7 = {'date':'December 7th',
        'year':'2022',
        'speakers': ['Dr. Ben Fried','Dr. Lígia Coelho'],
        'flavors': ['humanities','science'],
        'position': ['Visiting Lecturer in the Department of Literatures in English at Cornell University','Fulbright Scholar in the Department of Astronomy at Cornell University'],
        'talk_titles':['The Inside Story: How Editors Shape Books, Institutions, and World Literature','Orange is the New Blue – A Guide to Finding Colorful Aliens'],
        'abstracts': ['This talk will take you to the crossroads of power and creativity. Editors are the invisible gatekeepers of literature, shaping texts and tastes out of public sight. What do they actually do, and how have their actions changed literary history? “The Inside Story” will investigate three remarkable writer-editor relationships and three examples of editorial labor determining the fate of a literary work: one creative, one destructive, and one poised uneasily between the two. We will look at the Nobel laureate V. S. Naipaul getting his start on BBC Radio; the short-story superstar Mavis Gallant falling out with The New Yorker; Penguin India risking it all on Vikram Seth’s A Suitable Boy, one of the longest novels ever written, and dominating the subcontinent as a result. And so we will move through the twentieth century—from the Caribbean to North America to South Asia—uncovering the editorial networks linking literary institutions in London and New York to Anglophone authors around the world. Drawing the editor from backstage to center stage, “The Inside Story” will illuminate the influence of this crucial cultural figure, for good and bad, from heyday to present-day decline.',
                      'Biological pigments or “biopigments” are what make life colorful but also resilient to radiation, lack of available liquid water, and harsh temperatures – the typical weather forecast in space! Microbes that live in ice have a pretty hard time with these conditions too, and so, they tend to be very colorful – which makes them very good references for what life may look like in the cosmos! Future telescopes will be able to search for these colorful features, but first we need to translate them from biology into the language of space missions: spectroscopy!<br><br>What does the spectral fingerprint of a biopigment look like? How can that help us search for life in the cosmos? And more importantly…can we really have planets covered by orange aliens?!']
        }


feb1= {'date':'February 1st',
        'year':'2023',
        'speakers': ['Megan Barrington','Dr. Seth Strickland'],
        'flavors': ['science','humanities'],
        'position': ['PhD Candidate in Earth and Atmospheric Sciences at Cornell University','Joseph F. Martino \'53 Lecturer in the Dept. of Literatures in English at Cornell University'],
        'talk_titles':['Kometes: An Enduring Journey from Fiery Omens to Icy Worlds','The Last Medieval Scribe: John Colyns and Authorial Control'],
        'abstracts': [r'Since bygone eras of antiquity, humans have watched in astonishment, intrigue, and terror as brilliant orbs of light amidst an illuminated drift entered the heavenly spheres. Could they be harbingers of doom? Weather phenomena? Balls of fire in the sky? Wild speculations and superstitions ever follow in their wakes—but what are comets really? And what can we learn from them? After hundreds of years of asking such questions, we finally have some answers, even as so much remains unknown. Join us on a journey of fire and ice to discover how these objects once believed to signal the end of an era could be responsible for the origins of life as we understand it today.',
                      '“The Last Medieval Scribe: John Colyns and Authorial Control,” takes the twilight of medieval manuscript culture as its focus. For a few years until 1521, a bookseller named John Colyns carefully constructed a book that was very ordinary for his time but one of a dying breed. It contained, among other things, both century-old medieval poem and one that was written during his lifetime, both copied by hand -- the latter likely from a copy circulated among friends of the author. Colyns prophesied the fame of the new works in the book to his book-binding efforts – we’ll discover whether his claim is founded or whether other forces upended his plans. With this book as our guide, we\'ll look at some general principles of medieval and early modern hand-made bookmaking to learn how the material of books – the paper, the ink, the binding, and the order of its contents – matters to the ‘material’ of literature – the content and interpretation of the works within.']
        }

def generate_page(s_list,old=1,preamble=preamble,about=about,datetime=datetime,footer=footer,crowd=crowd):
    talks = generate_s_list(s_list,old=old)
    if old:
        preamble = preamble + '\n\n<br><br>'
        outcode = assemble([preamble,crowd,talks,datetime,footer])
    else:
        outcode = assemble([preamble,about,talks,crowd,datetime,footer])
    return outcode


s_list = [feb1,dec7,nov2,oct5]
oldpage = generate_page(s_list[1:],old=1)#ignore most recent entry for old page
homepage = generate_page([s_list[0],],old=0)#use only most recent entry for current page


currentpath = os.path.abspath(os.curdir)
os.chdir("..") #move up one directory for file saving
with open('past_events.html','w',encoding='utf-8') as outfile: #utf-8 required to get 'special' characters like mac's bullshit quotes or whatever.
    n = outfile.write(oldpage)
with open('index.html','w',encoding='utf-8') as outfile: #utf-8 required to get 'special' characters like mac's bullshit quotes or whatever.
    n = outfile.write(homepage)

