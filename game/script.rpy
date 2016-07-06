init python:
    import magic

image bg meadow = "meadow.jpg"
image bg uni = "uni.jpg"

image sylvie smile = "sylvie_smile.png"
image sylvie surprised = "sylvie_surprised.png"

define s = Character('Sylvie', color="#c8ffc8")
define m = Character('Me', color="#c8c8ff")

label start:
    scene bg uni
    show sylvie smile

    s "Oh, hi, do we walk home together?"
    m "Yes..."
    "I said and my voice was already shaking."

    $ result = magic.add(1, 2)

    "1 + 2 = %(result)d"

    scene bg meadow
    with fade

    "We reached the meadows just outside our hometown."
    "Autumn was so beautiful here."
    "When we were children, we often played here."
    m "Hey... ummm..."

    show sylvie smile at right
    with dissolve

    "She turned to me and smiled."
    "I'll ask her..."
    m "Ummm... will you..."
    m "Will you be my artist for a visual novel?"

menu:
    "It's a story with pictures.":
         jump vn

    "It's a hentai game.":
         jump hentai

label vn:
    m "It's a story with pictures and music."
    jump marry

label hentai:
    m "Why it's a game with lots of sex."
    jump marry

label marry:
    scene black
    with dissolve

    "--- years later ---"
