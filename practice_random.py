# import time
# timerStart = time.time()

# def fib_bottom_up(n=None):
# 	if n == 1 or n == 2:
# 		return 1
# 	fib_list = [0]*(n+1)
# 	fib_list[1] = 1
# 	fib_list[2] = 1
# 	for i in range(3,n+1):
# 		fib_list[i] = fib_list[i-2]+fib_list[i-1]
# 	return fib_list[n]

# print(fib_bottom_up(100000))
# # time.sleep(1)
# timerEnd = time.time()
# print(round(timerEnd-timerStart,2),'seconds')


def longestWord(words) -> str:
		# helper function to check if all prefixes are in dictionary:
		def check_pre(word):
			for i in range(1, len(word)):
				if word[:i] not in words:
					return False
			return True

		# sort by reversed lexicographical order:
		words.sort(reverse = True)
		# sort by length of word:
		words.sort(key = lambda a: len(a))
		print(words)
		# go through all words from end and check prefixes:
		for word in words[::-1]:
			print(word)
			if check_pre(word) == True:
				return word
		return ""

words = ["a", "banana", "app", "appl", "ap", "apply", "apple"]
print(longestWord(words))
