""" Miroslav Sanader
	ms13r"""
from __future__ import print_function
import requests
import json
import sys

def pull_data(url):
	unsorted_list = []
	for i in xrange(1000):
		page = requests.get(url + str(i) + "/hit.json?scrolling")
		if page.text == "" or page.status_code != 200:
			break
		json_page = json.loads(page.text)
		for item in json_page["data"]["captions"]["data"]:
			unsorted_list.append([item["hash"], item["points"], item["title"], item["datetime"]])

	if not unsorted_list:
		return unsorted_list
	unsorted_list.sort(key = lambda x: int(x[1]), reverse = True)
	return unsorted_list

def print_items(list, num):
	for i in range(0,num):
			print(str(i + 1) + ". " + sorted_list[i][0])
			print("Points: " + str(sorted_list[i][1]))
			print("Title: " + sorted_list[i][2])
			print("Date: " + sorted_list[i][3] + "\n")

if __name__ == "__main__":
	user_name = raw_input("Enter username: ")
	sorted_list = pull_data("http://imgur.com/user/" + user_name + "/index/newest/page/")

	if not sorted_list:
		print("Error! The user does not exist or has not posted any comments. Terminating program.")
	else:
		if len(sorted_list) < 5:
			print_items(sorted_list,len(sorted_list))
		else:
			print_items(sorted_list, 5)