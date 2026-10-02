from aluno import Aluno
from disciplina import Disciplina

#criar/intanciar 1 aluno
aluno1 = Aluno("João", "123456","Ciencias da computação")

#print(aluno1.notas_por_disciplinas)

#Criar / instanciar 2 displinas

sers = Disciplina("Soluções Renováveis", "Tritiack")
model_mat = Disciplina ("Modelagem Matemática",  "Professor")

aluno1.matricular(sers)
aluno1.matricular(model_mat)

aluno1.adcionar_nota(sers,10)
aluno1.adcionar_nota(sers,8)
aluno1.adcionar_nota(model_mat,10)
aluno1.adcionar_nota(model_mat,7)

print(aluno1.disciplinas[0].nome)

print(aluno1.calcular_media_d(model_mat))

