from tkinter import *
from bs4 import BeautifulSoup
import urllib.request
import requests
import random


    #GET BAYEDE NEWS LINKS
    resp = urllib.request.urlopen("https://bayedenews.com/")
    soup = BeautifulSoup(resp, parser, from_encoding=resp.info().get_param('charset'))
    for link in soup.find_all('a', href=True):
        if link['href'].startswith('https://bayedenews.com/20'):
            links.append(link['href'])

    #GET ILANGA NEWS LINKS
    resp = urllib.request.urlopen("https://ilanganews.co.za/")
    soup = BeautifulSoup(resp, parser, from_encoding=resp.info().get_param('charset'))
    for link in soup.find_all('a', href=True):
        if link['href'].startswith('https://ilanganews.co.za/') and not 'category' in link['href'] and not 'author' in link['href']:
            links.append(link['href'])


def generate_corpus():
   definition_label.configure(text='Linda ikhophasi yakho. . . Lokhu kungathatha imizuzu emine')
   
   global result
   result = str(entry.get()).strip().lower()
   res = [ele for ele in get_article_content() if(result in ele)]
   
   if res:
       f = open('corpus.txt', 'w')
       for article in res:
           f.write(article)
           f.write('\n\n')
       f.close()
       message = "Ikhophasi yakho isikhiqiziwe"
   else:
       message = "Alitholakalanga igama kwikhophasi. Uma ikhophasi ingakhiqizeki, faka igama eliyisihlanganiso(isbn: ukuthi, kanye, futhi, ngoba, njll.)"
         
   definition_label.configure(text=message)


root = Tk()
root.geometry("800x400")
root.configure(bg='orange')
root.title('Mthuli Buthelezi')

label = Label(root, bg='orange', fg='#fff',
              text='UHLELO LOKULANDA IKHOPHASI YESIZULU KWI-INTERNET',
              font=("Helvetica", 12), pady=30)
label.pack()
entry = Entry(root, bd=5, width=50)
entry.pack()
space_label1 = Label(root, bg='orange', fg='#fff',)
space_label1.pack()
button = Button(root, text="Khiqiza Ikhophasi", command=generate_corpus, width=20)
button.pack()
space_label = Label(root, bg='orange', fg='#fff')
space_label.pack()
definition_label = Label(root, bg='orange', fg='#fff',
            font=("Helvetica", 12))
definition_label.pack()
root.mainloop()
