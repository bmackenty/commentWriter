# this program builds report card comments for students. Define the variables below, and the program will build a comment for you.

# NAME: the student's first legal name
# THIRD_PERSON_SINGULAR_PRONOUN: her, his, or their, depending on the student 
# PROJECT_DESCRIPTION: a description of the project
# PROJECT_NOUN: the noun that describes the project
# PROGRAMMING_SKILL: the programming language the student is learning (fairly well, with more room for improvement, very well, masteringly)
# STUDENT_VOICE: the student's voice, as expressed in the student's own words
# POSSESIVE_PRONOUN: him, her, depending on the student, plural 
# POSSESIVE_DETERMINER: her, his, or their, depending on the student, plural
# CLASSROOM_BEHAVIOR: the student's behavior in class
# REFLEXIVE_PRONOUN: himself, herself, themselves, depending on the student


import templates
import os
os.system("clear")

# TODO: slurp / sanitize this from spreadsheet or plaintext file

name = "Ruiqi"
third_person_singular_pronoun = "he"
project_description = "NPC reccomendation based on user's preferences"
project_noun = "npc's" # plural
programming_skill = "to an acceptable level for a beginning programmer"
student_voice = "I want to learn how to code"
possessive_pronoun = "him"
possesive_determiner = "his"
classroom_behavior = "focused, attentive, and actively engaged in his learning"
reflexive_pronoun = "himself"



templates.comments[9] = templates.comments[9].replace("NAME", name)
templates.comments[9] = templates.comments[9].replace("THIRD_PERSON_SINGULAR_PRONOUN", third_person_singular_pronoun)
templates.comments[9] = templates.comments[9].replace("PROJECT_DESCRIPTION", project_description)
templates.comments[9] = templates.comments[9].replace("PROJECT_NOUN", project_noun)
templates.comments[9] = templates.comments[9].replace("PROGRAMMING_SKILL", programming_skill)
templates.comments[9] = templates.comments[9].replace("STUDENT_VOICE", student_voice)
templates.comments[9] = templates.comments[9].replace("POSSESIVE_PRONOUN", possessive_pronoun)
templates.comments[9] = templates.comments[9].replace("POSSESIVE_DETERMINER", possesive_determiner)
templates.comments[9] = templates.comments[9].replace("CLASSROOM_BEHAVIOR",classroom_behavior)
templates.comments[9] = templates.comments[9].replace("REFLEXIVE_PRONOUN", reflexive_pronoun)


new_comment = templates.comments[9]

#  now we need to make sure everything after a period is capitalized
#  we'll do this by splitting the comment into a list of sentences, and then
#  capitalizing the first letter of each sentence

sentences = new_comment.split(".")
new_comment = ""
for sentence in sentences:
    sentence = sentence.strip()
    sentence = sentence.capitalize()
    new_comment += sentence + ". "

# now to remove all line breaks
new_comment = new_comment.replace("\n", " ")

# we should only have one space between words, so we'll remove all extra spaces
new_comment = " ".join(new_comment.split())

print(new_comment)
