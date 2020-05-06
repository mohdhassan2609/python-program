#Given the participants score sheet for your university sports day ,you are required find the runner-up score.you are given scores.store them in alist and find the score of runner-up
#input format:the first line contains.second line contains an array of integers each separated  by a space .........constraints:..output format:print the runner-up score
n=int(input())
arr=map(int,input().split())
print(sorted(list(set(arr)))[-2])
