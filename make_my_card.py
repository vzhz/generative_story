### function that takes associative list (sorted so paragraphs are in order, list of key-value pairs
### for paragraphs, each person represented by set of interests)
### database to

SUBJECT_ENTRY =

def ask_user_identity():
    user_name = raw_input("""What is your name?""") # they can enter anything
    user_origin = raw_input("""Where do I know you from?   Space Camp,
                                                           Colgate,
                                                           JPL,
                                                           MIT, and/or
                                                           Recurse Center?""") #they can enter anything although I made suggestions
    user_interest = raw_input("""When we get together, what do we like to talk about? (list all, spell precisely)
                                 Programming, Home Projects, Geology Jokes, Shit Trump Says, Stuff We Like On The Internet, Relationship Things""")
    # need to either return each or send it to a database
    # in the future, want to have front end that asks them which of the things they know me from (in choose as many as you want bubbles)
    # alternatively, could have users input their name/preferences and have something (like many aliases? the spell-checking library? are their better ways?) that will say "yo they meant this"
    # ^Michelle points out (not quite applicable) that you should anticipate many formatting errors, so, for example, "Expecting phone number as (111) 111-1111," is a bullshit error message because you know there are only like 3 ways to type a phone number so you should just take them all
