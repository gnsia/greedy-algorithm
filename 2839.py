# 문제
# 상근이는 요즘 설탕공장에서 설탕을 배달하고 있다. 상근이는 지금 사탕가게에 설탕을 정확하게 N킬로그램을 배달해야 한다. 설탕공장에서 만드는 설탕은 봉지에 담겨져 있다. 봉지는 3킬로그램 봉지와 5킬로그램 봉지가 있다.
#
# 상근이는 귀찮기 때문에, 최대한 적은 봉지를 들고 가려고 한다. 예를 들어, 18킬로그램 설탕을 배달해야 할 때, 3킬로그램 봉지 6개를 가져가도 되지만, 5킬로그램 3개와 3킬로그램 1개를 배달하면, 더 적은 개수의 봉지를 배달할 수 있다.
#
# 상근이가 설탕을 정확하게 N킬로그램 배달해야 할 때, 봉지 몇 개를 가져가면 되는지 그 수를 구하는 프로그램을 작성하시오.
#
# 입력
# 첫째 줄에 N이 주어진다. (3 ≤ N ≤ 5000)
#
# 출력
# 상근이가 배달하는 봉지의 최소 개수를 출력한다. 만약, 정확하게 N킬로그램을 만들 수 없다면 -1을 출력한다.



# a = [] # 3kg 봉다리
# b = [] # 5kg 봉다리
# result = []
# result_a = [] # a 봉다리 갯수
# result_b = [] # b 봉다리 갯수

sugar_kg = int(input())
pbag = 0
while (1):
    if sugar_kg % 5 == 0:
        pbag = pbag + (sugar_kg / 5)
        print(int(pbag))
        break

    sugar_kg = sugar_kg - 3
    pbag = pbag + 1

    if sugar_kg < 0 :
        print(-1)
        break



# if n % 5 == 0 :
#     result.append(int(n/5))
# elif n % 5 != 0 :
#     for i in range(1, n+1):
#         if i % 5 == 0 :
#             b.append(i)
#     result.append(len(b))
#     for i in range(1, n + 1 - b[-1]):
#         if i
# print(b[-1])
# print(result)


# for i in range(1,n+1):
#     if i % 3 == 0 :
#         a.append(i)
#
# for i in range(1,n+1):
#     if i % 5 == 0 :
#         b.append(i)
# print(a)
# print(b)
#
# for i in a:
#     for j in b:
#         if i + j == n:
#             result.append(i)
#             result.append(j)
# print("result :",result)
#
# for i in result:
#     if i % 3 == 0 :
#         result_a.append(int(i / 3))
#     elif i % 5 == 0 :
#         result_b.append(int(i / 5))
# print(result_a)
# print(result_b)
#
# answer = result_a[0] + result_b[0]
# print(answer)
#
# last_b = today_b[-1]
# # print(last_b)
#
# find_a = n - last_b
# # print(find_a)
# for i in range(1, find_a+1):
#     if i % a == 0 :
#         # print(i)
#         today_a.append(i)
#
# # print(today_a)
# # print(today_b)
# today_ab = today_a + today_b
# today = len(today_ab)
#
# # print(today)
