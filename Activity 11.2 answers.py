__author__ = 'Alicia'


def ptranscript(transcript):
    for key in transcript:
        print(str(key) + ' class list:')
        for course in transcript[key]:
            print(' '*5 + course[0] + ' ' + course[1] + ' ' + course[2] + ' ' + course[3])
        print('\n')


def semesters(subject):
    for key in transcript:
        for course in transcript[key]:
            if subject == str(course[0]):
                print(key)
    print('\n')


transcript = {'Spring 2012': [['MATH', '281', '01', 'Foundations of Higher Mathematics'],
                              ['MATH', '371', '01', 'Linear Algebra'], ['RLGS', '201', '01', 'Women in Religion']],
              'Fall 2013': [['MATH', '456', '02', 'Modern Algebra'],
                            ['MATH', '351', '01', 'Introduction to Operations Research'],
                            ['ENGL', '226', '02', 'The Holocaust and Literature']],
              'Spring 2013': [['ANTH', '110', '02', 'Cultural Anthropology'], ['MATH', '491', '01', 'Advanced Calculus'],
                              ['PHIL', '101', '02', 'Introduction to Philosophy']],
              'Fall 2014': [['CSCI', '156', '01', 'Computer Science I'], ['MATH', '381', '01', 'Mathematical Statistics'],
                            ['MATH', '401', '01', 'Advanced Engineering Math'], ['PHIL', '282', '02', 'Introduction to Logic']]}

ptranscript(transcript)
semesters('PHIL')
semesters('MATH')