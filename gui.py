import tkinter as tk
from tkinter import ttk
from Letterboxd import *
from movie_help import *
from IMDB import *


#Initialize entries list
entries = []

# Letterboxd genres
letterboxd_genres = ["None","action", "adventure", "animation", "comedy", "crime", "documentary", "drama", "family", "fantasy", "history", "horror", "music", "mystery", "romance", "science fiction", "thriller", "tv movie", "war", "western"]

# IMDB genres
imdb_genres = ["None", "Drama", "Comedy", "Romance", "Mystery", "Biography", "War", "History", "Music", "Western", "Sport", "Musical", "Thriller", "Crime", "Action", "Adventure", "Sci-Fi", "Fantasy", "Horror", "Family", "Animation", "Film-Noir"]


#Constructor
root = tk.Tk()
frame = tk.Frame(root)

#set size of window
root.geometry("1600x800")


# Create Text Field Entry Boxes
def create_entry(*labels): #allsows for any amount of inputs to be passed
    for label in labels:
        tk.Label(frame, text=label).pack()
        entry = tk.Entry(frame)
        entry.pack()
        entries.append(entry)

#Create drop down box for Genre Choice (Different Genres for different websites)
def create_dropdown(application):
    global genre_choice
    if application == 'LetterBoxd':
        genre_choice = ttk.Combobox(frame, values = letterboxd_genres)
        genre_choice["foreground"] = "black"
        tk.Label(frame, text="Select Genre").pack()
        genre_choice.pack()
    else:
       genre_choice = ttk.Combobox(frame, values = imdb_genres)
       genre_choice["foreground"] = "black"
       tk.Label(frame, text="Select Genre").pack()
       genre_choice.pack()
        

#Updates Text/Entry Fields being shown dependent on application choice as their functionality is different.
def text_fields(dropdown):   
    global entries
    for widget in frame.winfo_children():  #Reset Text Fields to avoid wrong entires being shown
        widget.destroy()
    
    
    entries = []#Reset entries to avoid wrong data being collected
    
    if application_choice.get() == 'LetterBoxd':
        create_entry("Username")
        create_entry("Amount")
        create_dropdown("LetterBoxd")
        
    elif application_choice.get() == 'IMDB':
       create_entry("Amount")
       create_dropdown("IMDB")
    else:
        pass
    
#Since entries depend on application choice we must use a for loop to grab text entry values
def get_entries():
    entry_values = []
    for entry in entries:
        value = entry.get()  
        entry_values.append(value) 
    dropdown_value = application_choice.get()
    genre_dropdown_value = genre_choice.get() if genre_choice else None
    return entry_values + [dropdown_value, genre_dropdown_value]


#Use letterboxd.py and IMDB.py functions to generate random movie
def generate_movie():
    user_inputs = get_entries()
    
    if application_choice.get() == 'LetterBoxd' and user_inputs[3] is not None:
        username_l = user_inputs[0]
        amount_l = int(user_inputs[1]) #have to cast as int for other fuctions
        genre_l = user_inputs[3]
        result = get_movie_with_genre(username_l, genre_l,amount_l)
        text_result.insert(tk.END, f"You Should Watch: {', '.join(result)}\n")
        return result
    elif application_choice.get() == 'LetterBoxd':
        username_l = user_inputs[0]
        amount_l = int(user_inputs[1])
        result = get_movie_no_genre(username_l, amount_l)
        text_result.insert(tk.END, f"You Should Watch: {', '.join(result)}\n")
        return result
    elif application_choice.get() == 'IMDB' and user_inputs[2] is not None:
        amount_i = int(user_inputs[0])
        genre_i = user_inputs[2]
        result = getMovies_IMDB_Genre(genre_i,amount_i)
        text_result.insert(tk.END, f"You Should Watch: {', '.join(result)}\n")
        return result
    elif application_choice.get() == 'IMDB':
        amount_i = int(user_inputs[0])
        result = getMovies_IMDB(amount_i)
        text_result.insert(tk.END, f"You Should Watch: {', '.join(result)}\n")
        return result
    else:
        pass
        
    
             

#Text Box for results
text_result = tk.Text(root, height =10, width =80)



#DROPDOWN BOX
application_choices = ["","LetterBoxd","IMDB"]
application_choice = ttk.Combobox(root, values=application_choices)
application_choice.set(application_choices[0])
application_choice.bind("<<ComboboxSelected>>", text_fields) #Gives the Dropdown box functionality as it updates the text field function when there is a change

application_choice["foreground"] = "black"
generate_movie = tk.Button(root, text = 'Generate Movie', command = generate_movie)


#initalize to the layout
application_choice.pack()
frame.pack()
generate_movie.pack()
text_result.pack()

#Keeps the root looping
root.mainloop()
