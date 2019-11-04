#-----Statement of Authorship----------------------------------------#
#
#  This is an individual assessment item.  By submitting this
#  code I agree that it represents my own work.  I am aware of
#  the University rule that a student must not act in a manner
#  which constitutes academic dishonesty as stated and explained
#  in QUT's Manual of Policies and Procedures, Section C/5.3
#  "Academic Integrity" and Section E/2.1 "Student Code of Conduct".
#
#    Student no: N10023780
#    Student name: Gabriel Garate
#
#  NB: Files submitted without a completed copy of this statement
#  will not be marked.  Submitted files will be subjected to
#  software plagiarism analysis using the MoSS system
#  (http://theory.stanford.edu/~aiken/moss/).
#
#--------------------------------------------------------------------#

#-----Task Description-----------------------------------------------#
#
#  News Archivist
#
#  In this task you will combine your knowledge of HTMl/XML mark-up
#  languages with your skills in Python scripting, pattern matching
#  and Graphical User Interface development to produce a useful
#  application for maintaining and displaying archived news or
#  current affairs stories on a topic of your own choice.  See the
#  instruction sheet accompanying this file for full details.
#
#--------------------------------------------------------------------#

#-----Imported Functions---------------------------------------------#
#
# Below are various import statements that were used in our sample
# solution.  You should be able to complete this assignment using
# these functions only.

# Import the function for opening a web document given its URL.
from urllib.request import urlopen

# Import the function for finding all occurrences of a pattern
# defined via a regular expression, as well as the "multiline"
# and "dotall" flags.
from re import findall, MULTILINE, DOTALL, sub

# A function for opening an HTML document in your operating
# system's default web browser. We have called the function
# "webopen" so that it isn't confused with the "open" function
# for writing/reading local text files.
from webbrowser import open as webopen


# An operating system-specific function for getting the current
# working directory/folder.  Use this function to create the
# full path name to your HTML document.
from os import getcwd

# An operating system-specific function for 'normalising' a
# path to a file to the path-naming conventions used on this
# computer.  Apply this function to the full name of your
# HTML document so that your program will work on any
# operating system.
from os.path import normpath
    
# Import the standard Tkinter GUI functions.
from tkinter import *
from tkinter.ttk import Combobox

# Import the SQLite functions.
from sqlite3 import *

# Import the date and time function.
from datetime import datetime
#
#--------------------------------------------------------------------#
#-----Student's Solution---------------------------------------------#
#
# Put your solution at the end of this file.
#

# Name of the folder containing your archived web documents.  When
# you submit your solution you must include the web archive along with
# this Python program. The archive must contain one week's worth of
# downloaded HTML/XML documents. It must NOT include any other files,
# especially image files.
internet_archive = 'InternetArchive'

################ PUT YOUR SOLUTION HERE #################
# Strategy
# 1 Read the content of the webpage as a single string
# 2 Find specific tags
# 3 Extract text within tags and store into variables
# 4 Create a HTML file
# 5 Write the extracted content into the HTML File

# Internet Archive Folder Content
current_dir = getcwd()
website_1 = current_dir +'\\InternetArchive\\BBC_Sports_16.10.2017.html'
website_2 = current_dir +'\\InternetArchive\\BBC_Sports_17.10.2017.html'
website_3 = current_dir +'\\InternetArchive\\BBC_Sports_18.10.2017.html'
website_4 = current_dir +'\\InternetArchive\\BCC_Sports_19.10.2017.html'
website_5 = current_dir +'\\InternetArchive\\BCC_Sports_20.10.2017.html'
website_6 = current_dir +'\\InternetArchive\\BCC_Sports_21.10.2017.html'
website_7 = current_dir +'\\InternetArchive\\BCC_Sports_22.10.2017.html'
 
# Tags to find in the xml downloaded websites:
# <title>, <link>, <description>, <pubDate>, <lastBuildDate>, <image>,<url> and <item>           
# Regular expresions
find_lastbuiltdate = r'<lastBuildDate>([A-Za-z]+, [0-9]+ [A-Za-z]+ [0-9]+).+<'
find_titles = r'<title><!\[CDATA\[(.+)\]\]><' #extracts news articles' titles
find_description = r'<description><!\[CDATA\[(.+)\]\]><' #extracts description of new article
find_newslink = r'<link>(.+)<' #extracts the link to the respective news article
find_pubdate = r'<pubDate>(.+)<' #extracss publication dates only
find_images = r'(.+.jpg)'# extracts the whole image tag
find_imageurl = r'url="(.+)"' # extracts the url image only

# Gets the content of a webpage as a single string
def getHTMLCode(website):
    web_content = open(website, 'U', encoding = 'UTF-8')
    code = web_content.read()
    web_content.close()
    return code

# Get the content within a given tag
def getTags(tags, html):
    return findall(tags, html)
 


def writeArticle(image_url,title,description,newslink,pubdate):
    article = ''
    article = article + '                    <div class="col-sm-4">'
    article = article + '                        <img class="img-fluid" src="' + image_url + '" alt="Image not found">'
    article = article + '                        <h3>' + title + '</h3>'
    article = article + '                        <p>' + description + '</p>'
    article = article + '                        <p><a href="' + newslink + '"><b>Full story here</b></a><br>'
    article = article + '                        <b>Dateline: </b>' + pubdate + '</p>'
    article = article + '                    </div>'
    article = article + '                    <hr>'
    return article

# Read the contents of the webpage as a single string
def extract_content(website):
    html_code = getHTMLCode(website)    

    # Find tags and save them into variables for future use.
    global last_build_date
    global titles
    global website_title
    global descriptions
    global pubdates
    global newslinks
    global images
    global image_urls

    last_build_date = getTags(find_lastbuiltdate, html_code)    
    titles = getTags(find_titles, html_code)    
    website_title = titles[0] # BBC Sport - Football
    descriptions = getTags(find_description, html_code)
    pubdates = getTags(find_pubdate, html_code)
    newslinks = getTags(find_newslink, html_code)
    images = getTags(find_images, html_code) # extract the whole tag
    image_urls = getTags(find_imageurl, html_code) # extract the image url 

    # STEP 4 | Open HTML file for writing
    filename = website_title.replace(' ','_')   # BBC_Sport_-_Football
    filename = filename.replace('_-_','_')+ '.html' # BBC_Sport_Football.html
    html_file = open(filename, 'w', encoding = 'UTF-8')

    # Header
    header = """
    <!DOCTYPE html>
        <html lang="en">
            <head>
                <!-- Title for the browser window/tab -->
                <title>BBC Sport - Football</title>
                <!-- Required meta tags -->
                <meta charset="utf-8">
                <meta name="viewport" content="width=device-width, initial-scale=1">
                <!-- Bootstrap CSS -->
                <!-- Latest compiled and minified CSS -->
                <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css">
                <!-- jQuery library -->
                <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.4.1/jquery.min.js"></script>
                <!-- Popper JS -->
                <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.14.7/umd/popper.min.js"></script>
                <!-- Latest compiled JavaScript -->
                <script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.3.1/js/bootstrap.min.js"></script>
            </head>
            <body>
                <!-- Masthead -->
                <div class="jumbotron text-center">
                    <!-- BBC SPORT Logo -->
                    <img src="https://upload.wikimedia.org/wikipedia/commons/7/7c/BBC_Sport.svg" alt="BBC SPORTS">
                    <h6>NEWS_PUBDATE</h6>
                    <p><b>News source | <a href="http://feeds.bbci.co.uk/sport/football/rss.xml?edition=uk">BBC Sports</a></b><br>
                    <b>Archivist | Gabriel Garate</b></p>
                    <hr>
                </div>
                <div class="container-fluid">
                    <div class="row">
    """.replace('NEWS_PUBDATE',pubdates[0])

    body = ''
    i = 1
    while i <= 12: 
        if len(image_urls) == 0:
            body = body + writeArticle('#', titles[i],descriptions[i],newslinks[i+1],pubdates[i-1])
        else:
            body = body + writeArticle(image_urls[i-1],titles[i], descriptions[i],newslinks[i+1],pubdates[i-1])
        i += 1

    footer = """
                    </div>
                </div>
            </body>          
        </html>
    """
    # Write some content
    html_file.write(header)
    html_file.write(body)
    html_file.write(footer)

    # Close file
    html_file.close()

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# STEP 3 |  Graphical User Interface.
#           Decide whether you want to use push buttons, radio buttons, menus, lists
#           or some other mechanism for choosing, extracting and displaying archived
#           news.
#           Developing the GUI is the “messiest” step, and is best left to the end

# Create a window and give it a title
window = Tk()
window.title('News Archivist')

# Create a list of date choices
dates_list = ['16-Oct-2017',
              '17-Oct-2017',
              '18-Oct-2017',
              '19-Oct-2017',
              '20-Oct-2017',
              '21-Oct-2017',
              '22-Oct-2017',
              'Latest News']

# - - - FUNCTIONS - - - 
# STEP 3 |Develop a function to open a given HTML document in the host computer’s
#         default web browser.  Importantly, this needs to be done in a way that
#         will work on any computing platform.
#         The provided template file contains hints for how to do this, using Python
#         functions for finding the “path” to the folder in which the Python script
#         resides (getcwd), for “normalising” full file names to the local computing
#         environment (normpath), and for opening a file in the host system’s default
#         web browser (called webopen in our template).


# Functions to store the date selected from the date lists menu
def get_date():
    return date_selector.get()

# Functions to extract news from archive after selecting a date
def extract_news():
    date = get_date()
    if date == '16-Oct-2017':
        extract_content(website_1)
        select_date['text'] = """16-Oct-2017 news extracted.
Click on Display extracted news"""
    elif date == '17-Oct-2017':
        extract_content(website_2)
        select_date['text'] = """17-Oct-2017 news extracted.
Click on Display extracted news"""
    elif date == '18-Oct-2017':
        extract_content(website_3)
        select_date['text'] = """18-Oct-2017 news extracted.
Click on Display extracted news"""
    elif date == '19-Oct-2017':
        extract_content(website_4)
        select_date['text'] = """19-Oct-2017 news extracted.
Click on Display extracted news"""
    elif date == '20-Oct-2017':
        extract_content(website_5)
        select_date['text'] = """20-Oct-2017 news extracted.
Click on Display extracted news"""
    elif date == '21-Oct-2017':
        extract_content(website_6)
        select_date['text'] = """21-Oct-2017 news extracted.
Click on Display extracted news"""
    elif date == '22-Oct-2017':
        extract_content(website_7)
        select_date['text'] = """22-Oct-2017 news extracted.
Click on Display extracted news"""
    elif date == 'Latest News':# selecting latest news
        extract_content('Latest_News.html')
        select_date['text'] = """Latest News extracted"""
    else:
        select_date['text'] = """Please select a date"""
 
 
# Functions to display news extracted
def display_news():
    date = get_date()
    if date == '16-Oct-2017':
        webopen('BBC_Sport_Football.html')
        select_date['text'] = """Opening web browser"""
    elif date == '17-Oct-2017':
        webopen('BBC_Sport_Football.html')
        select_date['text'] = """Opening web browser"""
    elif date == '18-Oct-2017':
        webopen('BBC_Sport_Football.html')
        select_date['text'] = """Opening web browser"""
    elif date == '19-Oct-2017':
        webopen('BBC_Sport_Football.html')
        select_date['text'] = """Opening web browser"""
    elif date == '20-Oct-2017':
        webopen('BBC_Sport_Football.html')
        select_date['text'] = """Opening web browser"""
    elif date == '21-Oct-2017':
        webopen('BBC_Sport_Football.html')
        select_date['text'] = """Opening web browser"""
    elif date == '22-Oct-2017':
        webopen('BBC_Sport_Football.html')
        select_date['text'] = """Opening web browser"""
    elif date == 'Latest News':
        webopen('BBC_Sport_Football.html')
        select_date['text'] = """Opening web browser"""
    else:
        select_date['text'] = """Extract some news first"""
        
    
# Functions to archive the latest news    
# Put your web page address here
def latest_download():
    web_page = urlopen('http://feeds.bbci.co.uk/sport/football/rss.xml?edition=uk')
    web_page_contents = web_page.read().decode('UTF-8')
    html_file = open('Latest_News.html', 'w', encoding = 'UTF-8')
    html_file.write(web_page_contents)
    html_file.close()
    select_date['text'] = """Latest news archived.
You can now extract and then display the news"""

# --- --- --- GUI | GRAPHICAL USER INTERFACE --- --- --- 

# Label for image    
BBC_image = PhotoImage(file = 'img-BBC_SPORTS.gif')
Logo = Label(window, image = BBC_image)

# Label above date selector combo box
select_date = Label(window, text = """Select a date below and
click on extract news""")

# - - -   
# Create a combo box widget whose parent container is the
# window
date_selector = Combobox(window, values = dates_list)

# - - - BUTTONS - - - 
# Button to extract news from archive

var1 = bool()
b1 = Button(window,
            text = 'Extract news from archive',
            command = extract_news
            )

# Button to display newx extracted
b2 = Button(window,
            text = 'Display extracted news',
            command = display_news
            )

# Button to archive the latest news
b3 = Button(window,
            text = 'Archive the latest news',
            command = latest_download
            )

# - - - - - - DATABASE INTERACTION - - - 
event_count = 0
# Add record if extract news is pressed
def b1_pushed():
    if record_event == 1:
        # Connect to the dabatase and retrieve a view of the database's contents
        eventlog_db = connect('event_log.db')
        db_view = eventlog_db.cursor()
        # Statement
        statement = """INSERT INTO event_log
                        VALUES (
                        'Event_Number',
                        'The button Extract news was pushed')
                        """.replace('Event_Number', str(event_count))
        # Execute stament
        db_view.execute(statement)
        # Commit change if any
        eventlog_db.commit()
        # Release the connection
        db_view.close()
        eventlog_db.close()
    

        

    
# Adds record if displays news is pressed
def b2_pushed():
    if record_event == 1:
        # Connect to the dabatase and retrieve a view of the database's contents
        eventlog_db = connect('event_log.db')
        db_view = eventlog_db.cursor()
        # Statement
        statement = """INSERT INTO event_log
                        VALUES (
                        'Event_Number',
                        'The button Display news was pushed')
                        """.replace('Event_Number', str(event_count))
        # Execute stament
        db_view.execute(statement)
        # Commit change if any
        eventlog_db.commit()
        # Release the connection
        db_view.close()
        eventlog_db.close()

# Add record if archive latest news is pressed
def b3_pushed():
    if record_event == 1:
        # Connect to the dabatase and retrieve a view of the database's contents
        eventlog_db = connect('event_log.db')
        db_view = eventlog_db.cursor()
        statement = """INSERT INTO event_log
                        VALUES (
                        'Event_Number',
                        'The button Latest news was pushed')
                        """.replace('Event_Number', str(event_count))
        # Execute stament
        db_view.execute(statement)
        # Commit change if any
        eventlog_db.commit()
        # Release the connection
        db_view.close()
        eventlog_db.close()

# Function to check check box status
var = IntVar()
var.set(0)
def record_events():
    global event_count
    event_count = event_count+1
    if var.get() == 0:
        record_events['text'] = 'Log events'
        return 0
    else: # var.get() == 1
        record_events['text'] = 'Events are being recorded'
        return 1
        
        
# Check box Button to record events
record_events = Checkbutton(window,
                            text = "Log events",
                            variable = var,
                            onvalue = 1, offvalue = 0,
                            command = record_events)
    
# Use the geometry manager to "pack" the widgets onto
# the window (with a margin around the widgets for neatness)
margin_size = 5
Logo.pack(pady = margin_size)
select_date.pack(pady = margin_size)
date_selector.pack(pady = margin_size)
b1.pack(pady = margin_size)
b2.pack(pady = margin_size)
b3.pack(pady = margin_size)
record_events.pack(pady = margin_size)


# Start the event loop to react to user inputs
window.mainloop()
