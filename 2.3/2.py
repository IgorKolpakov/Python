answers, student_answers = [
    "Dryopithecus",
    "Ramapithecus",
    "Australopithecus",
    "Homo Erectus",
    "Homo Sapiens Neanderthalensis",
    "Homo Sapiens Sapiens"
], []
error = 0

for i in range(len(answers)):
    student_answers.append(input(f'Vopros: {i + 1} etap razvitiy cheloveka?: '));
    if answers[i].lower() != student_answers[i].lower():
        error = error + 1;

print(f'Resultat testirovania\nPravilnie: {len(answers) - error}\t Oshibki: {error}\nPravilniy otvet:\n');
print(' => '.join(answers));