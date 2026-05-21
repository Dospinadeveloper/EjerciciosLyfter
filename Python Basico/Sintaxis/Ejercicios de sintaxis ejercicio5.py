total_grades = 0
current_note = 0
passing_grades = 0
failing_grades = 0
average_failing_grades = 0
average_passing_grades = 0
overall_grade_average = 0
notes_counter = 1

total_grades = int(input("Escriba el numero de notas a calificar: "))

#Aqui validamos que el ciclo se repita mientras el contador sea menor a las notas a calificar
while (notes_counter <= total_grades):
    current_note = int(input(f"Escriba la nota numero {notes_counter} "))
    if current_note < 70:
        failing_grades = failing_grades + 1
        average_failing_grades = average_failing_grades + current_note
    else:
        passing_grades = passing_grades + 1
        average_passing_grades = average_passing_grades + current_note
    #overall_grade_average = overall_grade_average + current_note / total_grades
    overall_grade_average = overall_grade_average + current_note
    notes_counter = notes_counter + 1
overall_grade_average = overall_grade_average / total_grades
if failing_grades > 0:
    average_failing_grades = average_failing_grades / failing_grades
else:
    average_failing_grades = 0

if average_passing_grades > 0:
    average_passing_grades = average_passing_grades / passing_grades
else:
    average_passing_grades = 0


#Aqui mostramos las notas aprobadas
print (f"El estudiante tiene {passing_grades} notas aprobadas")
print (f"Este es el promedio de notas aprobadas: {average_passing_grades}")

#Aqui mostramos las notas desaprobadas
print (f"El estudiante tiene {failing_grades} notas desaprobadas")
print (f"Este es el promedio de notas desaprobadas: {average_failing_grades}")

#Aqui mostramos el promedio total de notas
print (f"Este es el promedio total de notas:  {overall_grade_average}")