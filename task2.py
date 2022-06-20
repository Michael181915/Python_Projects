import math

centre_points = 'файл1.txt'
coord_points = 'файл2.txt'
result_points_coord = 'файл3.txt'
result_points = 'файл4.txt'

try:
    myfile1 = open(centre_points, mode = 'r', encoding = 'utf_8') #latin_1
    myfile2 = open(coord_points, mode = 'r', encoding = 'utf_8')
    myfile3 = open(result_points_coord, mode = 'w', encoding = 'utf_8')
    myfile4 = open(result_points, mode = 'w', encoding = 'utf_8')
except Exception:
    print('Файл не найден')
    print(sys.exc_info())
else:
    print('Операция выполняется:')
    def len_array(file):
        with open(file) as f:
            n = 0
            for line in f:
                n += 1
        return n

    def count_number(number):
        n = str(number)
        if '.' in n:
            return abs(n.find('.') - len(n)) - 1 
        else:
            return 0

    def int_float(number):                       #Интегрировнный тип данных int и float
        if (count_number(number) == 0):
            return int(number)
        else:
            return float(number)

    def start_array_float(file, array):
        double_array = [[] for i in range(int(len_array(file)))]
        with open(file) as start_file:
            for i in range(int(len_array(file))):                
                double_array[i] = [float(j) for j in start_file.readline().split()]
        return double_array

    def start_array(file, array):
        double_array = [[] for i in range(int(len_array(file)))]
        with open(file) as start_file:
            for i in range(int(len_array(file))):                
                double_array[i] = [int_float(j) for j in start_file.readline().split()]
        return double_array

    def centre_coord_x_y():
        return start_array(centre_points, centre_result_1)[0]
    
    def radius():
        return start_array(centre_points, centre_result_1)[1][0]


    centre_result_1 = []
    centre_result_2 = []

    print()
    print('Уравнение окружности имеет вид: (x - ' + str(centre_coord_x_y()[0]) + 
          ') ^ 2 + (y - ' + str(centre_coord_x_y()[1]) + 
          ') ^ 2 = ' + str(radius())) 
    print()
    print('Классификация соответствия ответов для точки координатов, по отношению к окружности: ')
    print('0 - точка лежит на окружности')
    print('1 - точка внутри')
    print('2 - точка снаружи')
    print()

    coord_result_1 = []
    coord_result_2 = []
    class_result = []
    
    for value in start_array(coord_points, centre_result_2):
        coord_result_1.append(value)

    def class_coord(file_arr, array, elem):
        if(len(start_array(file_arr, array)[0]) == 2):
            if(math.sqrt((elem[0] - centre_coord_x_y()[0])**2 + (elem[1] - centre_coord_x_y()[1])**2) == radius()):
                return 0
            elif(math.sqrt((elem[0] - centre_coord_x_y()[0])**2 + (elem[1] - centre_coord_x_y()[1])**2) < radius()):
                return 1
            else:
                return 2
        else:
            return 'Выберите другой файл с координатами, где число столбцов равно:' + str(len(centre_coord_x_y()[0]))

    for value in start_array(coord_points, centre_result_2):
        class_result.append(class_coord(coord_points, centre_result_2, value))
        
    print('Вывод символа каждого положения точки через новую строку')
    print(class_result)
    print()
    
    for value_1 in class_result:
        myfile3.write(str(value_1) + '\n')

    final_result_1 = []
    final_result_2 = []

    for value1 in coord_result_1:
        for value2 in value1:
            final_result_1.append(value2)

    

    for value1 in range(len(coord_result_1)):
        final_result_2.append(coord_result_1[value1])
        coord_result_1[value1].append(class_result[value1])
 

    for value_1 in final_result_2:
        for value_2 in value_1:
            print(value_2, end=' ')
        print()
    
    for value_1 in final_result_2:
        for value_2 in value_1:
            myfile4.write(str(value_2) + ' ')
        myfile4.write('\n')
    
finally:
    myfile1.close()
    myfile2.close()
    myfile3.close()
    myfile4.close()
