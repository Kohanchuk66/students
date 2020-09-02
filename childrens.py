students = {'Student1' : {language for language in ['English', 'Russian', 'Ukrainian', 'Polish']},
            'Student2' : {language for language in ['Polish', 'Ukrainian', 'Germany']},
            'Student3' : {language for language in ['Russian', 'Ukrainian', 'Germany', 'English', 'Polish']},
            'Student4' : {language for language in ['Polish', 'Ukrainian']},
            'Student5' : {language for language in ['Polish', 'Ukrainian', 'Russian']},
            'Student6' : {language for language in ['Polish', 'Germany', 'Ukrainian']}
            }
maxLanguages = 0
generalLanguages = {language for language in ['English', 'Polish', 'Russian', 'Ukrainian', 'Germany']}
sameLanguages = generalLanguages
for student in students.items():
    if len(student[1]) > maxLanguages:
        maxLanguages = len(student[1])
        mostSmartStudent = student[0]
    sameLanguages = sameLanguages.intersection(student[1])
print('The most smart student is', mostSmartStudent)
print('The same languages are', sameLanguages)