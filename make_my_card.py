### function that takes associative list (sorted so paragraphs are in order, list of key-value pairs
### for paragraphs, each person represented by set of interests)

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

