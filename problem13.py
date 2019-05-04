
#Write a python function to generate and return the list of all possible sentences created from the given lists of Subject, Verb and Object.
#Note: The sentence should contain only one subject, verb and object each.

#Sample Input	Expected Output
#
#I Play Hockey
#I Play Football
#I Love Hockey
#I Love Football
#You Play Hockey
#You Play Football
#You Love Hockey
#You Love Football
subjects=["I", "You"]
verbs=["Play", "Love"]
objects=["Hockey","Football"]
def py(subjects,verbs,objects):
    for i in range(0,len(subjects)):
        for j in range(0,len(verbs)):
            for k in range(0,len(objects)):
                 print(subjects[i],' ',verbs[j],' ',objects[k])
                
print(py(subjects,verbs,objects))
