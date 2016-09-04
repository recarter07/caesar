# caesar.py
import webapp2
import cgi

class Index(webapp2.RequestHandler):
    """ Handles requests coming in to '/' (the root of our site)
        e.g. www.flicklist.com/
    """

    def get(self):

        edit_header = "<h3>Rotate This Phrase</h3>"

        # a form for rotation (action must match class name in post)
        add_form = """
        <form action="/rotate" method="post">
            <label>
                Rotate this phrase
                <input type="text" name="rotation text"/>
                entered in the textbox.
            </label>
            <input type="submit" value="Rotate It"/>
        </form>
        """

        # a form for crossing off movies
        # (first we build a dropdown from the current watchlist items)
        crossoff_options = ""
        for movie in getCurrentWatchlist():
            crossoff_options += '<option value="{0}">{0}</option>'.format(movie)

        crossoff_form = """
        <form action="/cross-off" method="post">
            <label>
                I want to cross off
                <select name="crossed-off-movie"/>
                    {0}
                </select>
                from my watchlist.
            </label>
            <input type="submit" value="Cross It Off"/>
        </form>
        """.format(crossoff_options)

        # if we have an error, make a <p> to display it
        error = self.request.get("error")
        error_element = "<p class='error'>" + error + "</p>" if error else ""

        # combine all the pieces to build the content of our response
        main_content = edit_header + add_form + crossoff_form + error_element
        response = page_header + main_content + page_footer
        self.response.write(response)




# given code
ALPHABET_LOWERCASE = "abcdefghijklmnopqrstuvwxyz"
ALPHABET_UPPERCASE = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def alphabet_position(letter):
    alphabet = ALPHABET_LOWERCASE if letter.islower() else ALPHABET_UPPERCASE
    return alphabet.index(letter)

def rotate_char(char, rotation):
    if not char.isalpha():
        return char

    alphabet = ALPHABET_LOWERCASE if char.islower() else ALPHABET_UPPERCASE
    new_pos = (alphabet_position(char) + rotation) % 26
    return alphabet[new_pos]

def encrypt(text, rotation):
    answer = ""
    for char in text:
        answer += rotate_char(char, rotation)
    return answer


# Helpful stuff below from the studios work:

"""
def post(self):
    # look inside the request to figure out what the user typed
    new_movie = self.request.get("new-movie")
# if the user typed nothing at all, redirect and yell at them
    if new_movie == "":
        error = "Enter a movie please"
        self.redirect('/?error={}'.format(error))
        return

# 'escape' the user's input so that if they typed HTML, it doesn't mess up our site
    new_movie_element = "<strong>" + cgi.escape(new_movie, quote = True) + "</strong>"


# make a helpful error message
    error = "'{0}' is not in your Watchlist, so you can't cross it off!".format(crossed_off_movie)
    error_escaped = cgi.escape(error, quote=True)

# redirect to homepage, and include error as a query parameter in the URL
    self.redirect("/?error=" + error_escaped)
"""

# Helpful stuff below from the Udacity source code
"""
<!DOCTYPE html>
<html>
  <head><title>caesar rotation</title></head>
  <body>
    <h2>Enter some text please:</h2>
    <form method="post">
      <textarea name="text" style="height: 100px; width: 400px;"></textarea>
      <br>
      <input type="submit">
    </form>
  </body>
</html>
"""
