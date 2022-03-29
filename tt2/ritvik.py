print('Welcome to a Python Quiz, dedicated to Basketball')
answer=input('Ready to begin? (yes/no) ')
score=0
total_questions=3
 
if answer.lower()=='yes':
    answer=input('Question 1: Who won the 2021 NBA MVP? {last name} ')
    if answer=='Jokic':
        score += 1
        print('correct')
    else:
        print('Wrong Answer')
 
 
    answer=input('Question 2: Who won the 2021 NBA Championship? {name of team} ')
    if answer=='Bucks':
        score += 1
        print('correct')
    else:
        print('Wrong Answer')
 
    answer=input('Question 3: Who wears #10 on the Cleveland Cavaliers? {last name} ')
    if answer=='Garland':
        score += 1
        print('correct')
    else:
        print('Wrong Answer')

mark=(score/total_questions)*100
print('Score:',mark)