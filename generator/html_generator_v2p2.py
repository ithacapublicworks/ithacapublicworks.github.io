import numpy as np
import os
import csv
import pandas as pd


#speakerlist = pd.read_csv(r'speakerlist.csv')

cyan = '#00FFFF'
pink = '#FF00FF'

def assemble(codes):
    output = ''
    for i in codes:
        output=output+i+'\n\n'
    return output



def generate_date_code(date,year,rows,old=1): #creates alternating colors for the date and public works
    n_talks =len(rows['speaker'])

    if old:
        html = "\n\nThe <span style='color: "+cyan+"'>"+date+", "+year+" </span> <span style='color: "+pink+"'>Public Works</span> event featured "+str(n_talks)+" talks:\n\n<br><br>"
    else:
        html = "\n\nThe <span style='color: "+cyan+"'>"+date+"</span> <span style='color: "+pink+"'>Public Works</span> event will feature "+str(n_talks)+" talks:\n\n<br><br>"
    return html    



def generate_event(rows,old=1):
    #print('in generate')
    #print(rows)
    
    html = ''
    allcodes = ''

    date = str(np.array(rows['date'])[0])
    year = str(int(np.array(rows['year'])[0]))
    eventnum = np.array(rows['event'])[0]

    hashcode = np.array(rows['hashcode'])

    print('hashcode = '+str(hashcode))
    #print(hashcode[0])

    datecode = generate_date_code(date,year,rows,old)
    allcodes = allcodes +datecode

    count = 0
    talk_codes = ''
    for index,row in rows.iterrows():
        if count%2: #alternate colors by making even lines cyan pink and odd lines pink cyan
            color = [cyan,pink]
        else:
            color = [pink,cyan]
        if count ==0: #first speaker needs no line breaks and no 'and'
            flavorcode = row['flavor'].split()[0] + " <i>"+ ' '.join(row['flavor'].split()[1:])+"</i> talk:\n"
        else: #subsequent speakers need line breaks
            flavorcode = "\n\n<br><br>and " + row['flavor'].split()[0] +" <i>"+' '.join(row['flavor'].split()[1:])+"</i> talk:\n"

        titlecode = "<h3 id='"+str(hashcode[count])+"'><span style='color: "+color[0]+"'>"+'"'+row['title']+'"</span></h3>'
        
        #print(color[1])
        #print("<span style='color: "+str(color[1])+"'> by "+row['speaker']+"</span>\n<br>"+row['position'])
        authorcode = "<span style='color: "+str(color[1])+"'> by "+row['speaker']+"</span>\n<br>"+row['position']+"\n<br>\n<br>"
        abstractcode = row['abstract']
        assembledcode = assemble([flavorcode,titlecode,authorcode,abstractcode])
        talk_codes = talk_codes+assembledcode
        count +=1
    #print(allcodes)
    allcodes = allcodes +talk_codes
    allcodes = allcodes +'<br><br><br><br>' #add some space to delineate different nights
    #    allcodes = assemble(allcodes)

    #print(allcodes)
        
    return allcodes
            

def make_pages():
    with open('preamble.html', 'r') as file: #preamble contains the stuff that is at the top of every page, like the menu header and the logo
        preamble = file.read()

    with open('about.html', 'r') as file: #this contains the text used to describe the event
        about = file.read()

    with open('footer.html', 'r') as file: #footer contains the listerv sign up, email addresses for contact, etc.
        footer = file.read()

    with open('datetime.html', 'r') as file: #datetime contains the date, location, and time of the event
        datetime = file.read()

    with open('crowd.html','r') as file: #crowd contains an image of the crowd at the first event
        crowd = file.read()



    events = pd.read_csv('speaker_details.tsv', sep='\t') #import the data
    #print(events)

    n_events = events['event'].max() #get the total number of events


    #print('processing newest event, number '+str(n_events))
    rows = events.loc[events['event']==n_events] #get csv rows of most recent event
    #print(rows)
    newesteventtalks = generate_event(rows,old=0)#generate talk text for it

    #combine all text pieces into one page
    homepage = assemble((preamble,about,newesteventtalks,crowd,datetime,footer))



    htmlcode = assemble([preamble,'\n\n<br><br>',crowd])
    talks = ''
    for i in np.arange(n_events-1, 0, -1): #for every entry except the last one
        #print(i)
        #print('processing event '+str(i))
        rows = events.loc[events['event'] == i] #get locations of each row that matches the current event number
        #print(rows)
        nightcode = generate_event(rows) #generate the html code to describe that night of talks
        talks = talks + nightcode #add each talk to the list of old talks

    htmlcode = assemble([htmlcode,talks,crowd,datetime,footer])



    with open('test_home.html','w',encoding='utf-8') as outfile: #utf-8 required to get 'special' characters like mac's bullshit quotes or whatever.
        n = outfile.write(homepage)

    with open('test_old.html','w',encoding='utf-8') as outfile: #utf-8 required to get 'special' characters like mac's bullshit quotes or whatever.
        n = outfile.write(htmlcode)


    currentpath = os.path.abspath(os.curdir)
    os.chdir("..") #move up one directory for file saving
    with open('past_events.html','w',encoding='utf-8') as outfile: #utf-8 required to get 'special' characters like mac's bullshit quotes or whatever.
        n = outfile.write(htmlcode)
    with open('index.html','w',encoding='utf-8') as outfile: #utf-8 required to get 'special' characters like mac's bullshit quotes or whatever.
        n = outfile.write(homepage)
        
        
def main():
    make_pages()
    
if __name__ == "__main__":
    main()

# layout = [
#           [sg.Text('Public Works Website Maker V2.2',font=('Arial Bold',20))],
#           [sg.Text('For help contact zulibarri@cornell.edu')],
#           #[sg.Input(key='jpgname',default_text=init.get('jpgname'),size=(10,1))],
#           #[sg.Text('RAW Images File Type (For Nikon, usually NEF, for Canon, usually CR2, CR3, or CRW)')],
#           #[sg.Input(key='rawname',default_text=init.get('rawname'),size=(10,1))],
#           
#           [sg.Button('Make It So',key='generate'),sg.Button('Cancel',key='cancel')]]
# 
# window = sg.Window('Aspect', layout)
# 
# 
# currentpath = os.path.abspath(os.curdir)
# print('current path is '+str(currentpath))
# 
# files = os.listdir(os.curdir)  #files and directories
# print('files in current directory are:')
# print(str(files))
# 
# while True:                             # The Event Loop
#     event, values = window.read() #wait until values entered and you press the go button
#     #print('event = '+str(event))
#     if event == 'generate':
#         try:
#             make_pages()
#         except Exception as e:
#             error_message = traceback.format_exc()  # Get full traceback as a string
#             sg.popup("Error!", error_message, title="Error", keep_on_top=True)
# 
#     print('Done!')


