import time
import math

alphabet = "abcdefghijklmnopqrstuvwxyz0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"


def reverse_hash(tbHashed):
	rtn_int = 0
	for i in range(0, len(tbHashed)):
		aa = int(math.pow(62, i))
		# print(i, ": aa: ", aa)
		bb = alphabet.find(tbHashed[i])
		# print(i, ": bb: ", bb)
		n = aa * bb
		rtn_int += int(n)
		# print(rtn_int)
	return int(rtn_int)


def get_hash(base_array):
	rtn_str = ""
	for z in base_array:
		rtn_str += alphabet[z]
	return rtn_str


def get_base_array(blur):
	rtn_list = []
	while blur > 0:
		rem = blur % 62
		rtn_list.append(rem)
		blur = int(blur / 62)
	return rtn_list


def tbHash(offset=1560750100158985):
	now = int(time.time() * 1000000)
	blur = now - int(offset)
	# print("blur:", blur, "now:", now)
	base_array = get_base_array(blur)
	# print("ba: ", base_array)
	tbHash = get_hash(base_array)
	return tbHash


if __name__ == "__main__":
	a = tbHash()
	print(a)

	# b = reverse_hash(a)
	# print(b)
