import sys

input = sys.stdin.readline

# 저장된 사이트 주소 수 N의, 찾는 사이트 주소의 수 M
# 사이트 주소, 비번 공백으로 구분되어 주어짐
# 사이트 주소 : 알파벳 소문자, 대문자, 대시, 마침표, 중복없음
# 비번 : 알파벳 대문자

# N+2번째 줄부터 M개의 줄에 걸쳐 비번찾으려는 주소가 한줄에 하나씩 입력
site_num, find_num = map(int, input().split())


site_dict = dict()

for num in range(site_num):
    site, pw = input().split()
    site_dict[site] = pw

# print(site_dict)

for num in range(find_num):
    find_pw = input().strip()
    print(site_dict[find_pw])