from tkinter import *
from plex_model import *
from tkinter import messagebox

movie_list = []
list_count = 0


def search():
    database.connect()
    for record in Movies.select().where(Movies.sort_title.contains(query.get())):
        movie_list.append({record.sort_title: record.summary})
    for k, v in movie_list[list_count].items():
        lblTitle.configure(text='Title:  {}'.format(k))
        lblSummary.configure(text='Summary: {}'.format(v))
        return list_count

    database.close()


def next_record():
    try:
        global list_count
        list_count += 1
        for k, v in movie_list[list_count].items():
            lblTitle.configure(text='Title:  {}'.format(k))
            lblSummary.configure(text='Summary: {}'.format(v))
        return list_count
    except IndexError:
        messagebox.showinfo('No more movies', 'Out of Movies')


def prev_record():
    try:
        global list_count
        list_count -= 1
        for k, v in movie_list[list_count].items():
            lblTitle.configure(text='Title: {}'.format(k))
            lblSummary.configure(text='Summary: {}'.format(v))
        return list_count
    except IndexError:
        messagebox.showinfo('No more movies', 'Out of Movies')


window = Tk()

window.title('Plex Library Database')
radMovie = Radiobutton(window, text='Movie', value=1)
radTV = Radiobutton(window, text='TV', value=2)
query = Entry(width=50)
search_btn = Button(window, text='Search', command=search)
next_btn = Button(window, text='Next', command=next_record)
prev_btn = Button(window, text='Back', command=prev_record)
lblTitle = Label(window, text='')
lblSummary = Label(window, text='')


radMovie.grid(column=0, row=0, padx=5, pady=5)
radTV.grid(column=1, row=0, padx=5, pady=5)
query.grid(column=0, row=1, padx=5, pady=20, columnspan=5)
search_btn.grid(column=10, row=1, padx=5, pady=5)
next_btn.grid(column=12, row=1, padx=5, pady=5)
prev_btn.grid(column=11, row=1, padx=5, pady=5)
lblTitle.grid(column=0, row=3, padx=5, pady=5)
lblSummary.grid(column=0, row=4, padx=5, pady=5)


window.geometry('650x400')
window.mainloop()
