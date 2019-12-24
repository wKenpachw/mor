from pyDatalog import pyDatalog

pyDatalog.create_terms('chars, skill_text, belongs_to,  char_skill')

#персонаж - расса
+chars('char1', 'half')
+chars('char2', 'elf')
+chars('char3', 'elf')
+chars('char4', 'half')

pyDatalog.create_terms('X, Y')
#навык- описание
+skill_text('Skill1_text', 'skill1')
+skill_text('Skill2_text', 'skill2')

#связь расса - навык
+belongs_to('half', 'skill1')
+belongs_to('elf', 'skill2')

pyDatalog.create_terms('Z, H')
#навыки персонажа
char_skill(X, H) <= chars(X, Z) & belongs_to(Z, Y) & skill_text(H, Y)

print(chars(X, Z))
print(belongs_to(Z, Y))
print(char_skill(X, Y))