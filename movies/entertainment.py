import media
import fresh_tomatoes

toy_story = media.Movie("Toy Story","A story of a boy and his toys that come to life","https://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg","https://www.youtube.com/watch?v=33PUPuAdtqI")
#print(toy_story.storyline)

avatar = media.Movie("Avatar","A marine on an alien planet","https://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg","https://www.youtube.com/watch?v=5PSNL1qE6VY")

#print(avatar.storyline)

shawshank_redemption = media.Movie("Shawshank Redemption","A story of redemption","https://upload.wikimedia.org/wikipedia/en/8/81/ShawshankRedemptionMoviePoster.jpg","https://www.youtube.com/watch?v=NmzuHjWmXOc")
#shawshank_redemption.show_trailer()

the_dark_knight = media.Movie("The Dark Knight","Batman fights the Joker to restore order in Gotham","https://upload.wikimedia.org/wikipedia/en/8/8a/Dark_Knight.jpg","https://www.youtube.com/watch?v=_PZpmTj1Q8Q")

inception = media.Movie("Inception","Dream within dreams","https://upload.wikimedia.org/wikipedia/en/2/2e/Inception_%282010%29_theatrical_poster.jpg","https://www.youtube.com/watch?v=8hP9D6kZseM")

uri = media.Movie("Uri","Revenge of Uri Terrorist Attack","https://upload.wikimedia.org/wikipedia/en/3/3b/URI_-_New_poster.jpg","https://www.youtube.com/watch?v=Cg8sbRFS3zU")

#movies = [toy_story,avatar,shawshank_redemption,the_dark_knight,inception,uri]
#fresh_tomatoes.open_movies_page(movies)
print (media.Movie.VARIABLE_RATINGS)
print (media.Movie.__name__)
print(media.Movie.__module__)
