# Треугольник существует только тогда, когда сумма любых двух его сторон больше третьей. Дано a, b, c - стороны предполагаемого треугольника.
# Требуется сравнить длину каждого отрезка-стороны с суммой двух других.
# Если хотя бы в одном случае отрезок окажется больше суммы двух других, то треугольника с такими сторонами не существует.
# Отдельно сообщить является ли треугольник разносторонним, равнобедренным или равносторонним.

#Будем считать, что a - вершина треугольника, тогда стороны ab и ac - его бедра, а сторона bc - основание!

from random import randint

segment_ab = randint(1, 25)
segment_bc = randint(1, 25)
segment_ac = randint(1, 25)


segments_summ1 = segment_ab + segment_bc
segments_summ2 = segment_bc + segment_ac
segments_summ3 = segment_ab + segment_ac
flag_side1 = False                                         # флаг равенства сторон ab и bc
flag_side2 = False                                         # флаг равенства сторон ac и bc
flag_side3 = False                                         # флаг равенства сторон ab и ac
if segment_ab == segment_bc and segment_ab != segment_ac:
    flag_side1 = True
elif segment_bc == segment_ac and segment_bc != segment_ab:
    flag_side2 = True
elif segment_ab == segment_ac and segment_ab != segment_bc:
    flag_side3 = True


if segments_summ1 > segment_ac and segments_summ2 > segment_ab and segments_summ3 > segment_bc:
    print("Треугольник со сторонами", segment_ab, segment_ac, "и основанием", segment_bc, "существует")
    if segment_ab == segment_ac and segment_ab == segment_bc:
        print("Треугольник равносторонний")
    elif segment_ab != segment_bc and segment_ab != segment_ac:
        print("Треугольник разносторонний")
    elif flag_side1 or flag_side2 or flag_side3:
        print("Треугольник равнобедренный")
else:
    print("Треугольника со сторонами", segment_ab, segment_ac, "и основанием", segment_bc, "не существует")