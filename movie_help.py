def printhelp():
    print('''
          Hello. This Application is here to help you pick a random movie to watch
          
          If you have a letter boxd account and want to pick a random movie from your watchlist please use the following command line entries
          -l (username) -n (amount of random movies to choose )
          Along with this you can use -g (genre) to specify a specific genre. The genres you can pick from include:
          action, adventure, animation, comedy, crime, documentary, drama, family, fantasy. history, horror, music, mystery, romance, science fiction, thriller, tv movie, war, western
          An Example command line entry could look like "-l nolsz -g action -n 2" OR "-l nolsz -n 2"
          
          If you do not have a letterboxd account and just want to get a movie to watch from an IMDB list you can instead use -i
          Similarly if you wish to do so your command line entry would look like -l (username) -n (amount of random movies to choose )
          For IMDB as well you can use -g (genre) to specify a specific genre. The genres you can pick from include:
          Drama, Comedy, Romance, Mystery, Biography, War, History, Music, Western, Sport, Musical, Thriller, Crime, Action, Adventure, Sci-Fi, Fantasy, Horror, Family, Animation, Film-Noir
          An Example command line entry could look like "-i -g Drama -n 2" OR "-i -n 2"
          
          For both command line entries ensure that you use capitals or lowercases as shown
          
          
          
          
          ''')
