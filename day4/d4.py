"""
Python dictionary 연습 문제
"""

# 1. 평균을 구하시오.
score = {
    '수학': 80,
    '국어': 90,
    '음악': 100
}

# 아래에 코드를 작성해 주세요.
print('==== Q1 ====')

    # 1-1. 기본풀이
result1 = 0
for subject in score.values():
    # result = result + subject
    result1 += subject
print('평균은 {}점입니다.'.format(result1/len(score)))

    # 1-2. sum 함수 활용하기
result2 = sum(score.values())
count = len(score)
print('평균은 {}점입니다.'.format(result2/len(score)))

# 2. 반 평균을 구하시오. -> 전체 평균
scores = {
    'a': {
        '수학': 80,
        '국어': 90,
        '음악': 100
    },
    'b': {
        '수학': 80,
        '국어': 90,
        '음악': 100
    }
}

# 아래에 코드를 작성해 주세요.
print('==== Q2 ====')

  # 2-1 기본풀이
average = {}
for class_name, class_scores in scores.items():
    subject_score = 0
    for subject in class_scores.values():
       subject_score += subject
    average[class_name] = subject_score/len(class_scores)
total_score = 0
for avg in average:
    print('{}반의 평균은 {}입니다'.format(avg,average[avg]))
    total_score += average[avg]
print('전체 평균은 {}입니다.'.format(total_score/len(average)))


# 3. 도시별 최근 3일의 온도입니다.
city = {
    '서울': [-6, -10, 5],
    '대전': [-3, -5, 2],
    '광주': [0, -2, 10],
    '부산': [2, -2, 9],
}

# 3-1. 도시별 최근 3일의 온도 평균은?

# 아래에 코드를 작성해 주세요.
print('==== Q3-1 ====')
"""
출력 예시)
서울 : 값
대전 : 값
광주 : 값
부산 : 값
"""
temperture={}
for city_name, city_temp in city.items():
    temp_sum = sum(city_temp)
    temperture[city_name]=temp_sum/len(city_temp)
    print('{} : {:.1f}'.format(city_name,temperture[city_name]))
        
# 3-2. 도시 중에 최근 3일 중에 가장 추웠던 곳, 가장 더웠던 곳은?

# 아래에 코드를 작성해 주세요.
print('==== Q3-2 ====')

# 모든 지역의 온도를 모두 확인하면서,
count = 0
for name, temp in city.items():
    # 첫번째 반복때에는 모두 다 저장해!
    if count == 0:
        min_temp = min(temp)
        max_temp = max(temp)
        min_city = name
        max_city = name
# 가장 추우면 해당도시와 온도를 기록
    if min(temp) < min_temp:
        min_city = name
        min_temp = min(temp)
# 더울때에도, 해당 도시와 온도 기록
    if max(temp) > max_temp:
        min_city = name
        min_temp = max(temp)
    count += 1
print(f'추운 곳은 {min_city}, 더운 곳은 {max_city}')


# 3-3. 위에서 서울은 영상 2도였던 적이 있나요?

# 아래에 코드를 작성해 주세요.
print('==== Q3-3 ====')
value = False
for temperture in city['서울']:
    if temperture == 2:
        value = True
if value == True:
    print("서울은 영상 2도 였던 적이 있습니다.")
else:
    print("서울은 영상 2도 였던 적이 없습니다.")

    # 풀이 3-3-2 있는지 없는 지 물어보는 if 구문
if 2 in city['서울']:
    print("서울은 영상 2도 였던 적이 있습니다.")
else:
    print("서울은 영상 2도 였던 적이 없습니다.")
    
        
        