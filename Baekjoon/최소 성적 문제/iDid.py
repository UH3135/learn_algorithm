import math
from decimal import Decimal
def check_condition(gl: int, x: float, ss: int, gs: int, goal: float):
    '''
    소수 셋째 자리에서 버림하는 거로 생기는 오류 제거를 위한 함수
    :param gl: 마지막 학점
    :param x: 구한 값 (맞아야 하는 학점)
    :param ss: 마지막 성적을 제외한 모든 점수의 합
    :param gs: 마지막 성적을 제외한 학점끼리의 합
    :param goal: 넘어야 하는 값
    :return: boolean(점수를 넘기면 그대로 출력, 아니면 한단계 올려서 출력 하도록)
    '''
    tmp = Decimal(gl * x + ss) / (gs + gl)  # 부동 소수점 오차를 막기 위한 코드
    result = math.floor(tmp * 100) / 100

    if result > goal:
        return True
    else:
        return False


n, goal = input().split()

n = int(n)  # Test case 수
goal = float(goal)  # 받아야 하는 성적

grade_ratio = {  # 성적에 따른 점수 비율
    'A+': 4.5,
    'A0': 4.0,
    'B+': 3.5,
    'B0': 3.0,
    'C+': 2.5,
    'C0': 2.0,
    'D+': 1.5,
    'D0': 1.0,
    'F': 0.0
}

score_sum = 0  #과목별 학점 * 평점의 합
grade_sum = 0  # 수강한 학점 총합

for _ in range(n - 1):
    a, x = input().split()
    a = int(a)

    score_sum += a * grade_ratio[x]
    grade_sum += a

grade_last = int(input())  # 마지막 과목 학점

condition_num = math.floor(((goal*(grade_sum + grade_last) - score_sum) / grade_last) * 100) / 100  # 분류 기준이 되는 값

if grade_ratio['F'] > condition_num:  # condition_num가 조건에 맞는 범위에 위치하면 그 최댓값을 기준으로 학점 리턴
    if check_condition(grade_last, grade_ratio['F'], score_sum, grade_sum, goal):  # 소수점으로 인해 생기는 오류방지
        print('F')
    else:
        print('D0')
elif (grade_ratio['F'] < condition_num) and (grade_ratio['D0'] >= condition_num):
    if check_condition(grade_last, grade_ratio['D0'], score_sum, grade_sum, goal):
        print('D0')
    else:
        print('D+')
elif (grade_ratio['D0'] < condition_num) and (grade_ratio['D+'] >= condition_num):
    if check_condition(grade_last, grade_ratio['D+'], score_sum, grade_sum, goal):
        print('D+')
    else:
        print('C0')
elif (grade_ratio['D+'] < condition_num) and (grade_ratio['C0'] >= condition_num):
    if check_condition(grade_last, grade_ratio['C0'], score_sum, grade_sum, goal):
        print('C0')
    else:
        print('C+')
elif (grade_ratio['C0'] < condition_num) and (grade_ratio['C+'] >= condition_num):
    if check_condition(grade_last, grade_ratio['C+'], score_sum, grade_sum, goal):
        print('C+')
    else:
        print('B0')
elif (grade_ratio['C+'] < condition_num) and (grade_ratio['B0'] >= condition_num):
    if check_condition(grade_last, grade_ratio['B0'], score_sum, grade_sum, goal):
        print('B0')
    else:
        print('B+')
elif (grade_ratio['B0'] < condition_num) and (grade_ratio['B+'] >= condition_num):
    if check_condition(grade_last, grade_ratio['B+'], score_sum, grade_sum, goal):
        print('B+')
    else:
        print('A0')
elif (grade_ratio['B+'] < condition_num) and (grade_ratio['A0'] >= condition_num):
    if check_condition(grade_last, grade_ratio['A0'], score_sum, grade_sum, goal):
        print('A0')
    else:
        print('A+')
elif (grade_ratio['A0'] < condition_num) and (grade_ratio['A+'] >= condition_num):
    if check_condition(grade_last, grade_ratio['A+'], score_sum, grade_sum, goal):
        print('A+')
    else:
        print('impossible')
elif grade_ratio['A+'] < condition_num:
    print('impossible')

