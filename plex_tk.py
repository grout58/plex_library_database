from tkinter import *
from plex_model import *

movie_list = []

def search():
    database.connect()
    for record in Movies.select().where(Movies.sort_title.contains(query.get())):
        movie_list.append({record.sort_title: record.summary})
    res_label.configure(text=movie_list[0])
    return movie_list

    database.close()


window = Tk()




window.title('Plex Library Database')
radMovie = Radiobutton(window, text='Movie', value=1)
radTV = Radiobutton(window, text='TV', value=2)
query = Entry(width=50)
search_btn = Button(window, text='Search', command=search)
res_label = Label(window, text='blank')


radMovie.grid(column=0, row=0, padx=5, pady=5)
radTV.grid(column=1, row=0, padx=5, pady=5)
query.grid(column=0, row=1, padx=5, pady=20, columnspan=10)
search_btn.grid(column=10, row=1, padx=5, pady=5)
res_label.grid()


window.geometry('500x200')
window.mainloop()
