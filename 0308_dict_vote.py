# 투표 결과 리스트
votes = ['김영자', '강승기', '최만수', '김영자', '강승기', '강승기', '최만수', '김영자', \
'최만수', '김영자', '최만수', '김영자', '김영자', '최만수', '최만수', '최만수', '강승기', \
'강승기', '김영자', '김영자', '최만수', '김영자', '김영자', '강승기', '김영자']

# 후보별 득표수 사전
vote_counter = {}
vote_counter['김영자'], vote_counter['강승기'], vote_counter['최만수'] = 0, 0, 0
# 리스트 votes를 이용해서 사전 vote_counter를 정리하기
for name in votes:
    # 코드를 작성하세요.
    vote_counter[name] += 1

# 후보별 득표수 출력
print(vote_counter)
