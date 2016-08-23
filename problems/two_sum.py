# coding:utf-8
#
# Given an array of integers, return indices of the two numbers such that
# they add up to a specific target.
# You may assume that each input would have exactly one solution.
#
# Example:
# Given nums = [2, 7, 11, 15], target = 9,
# Because nums[0] + nums[1] = 2 + 7 = 9,
# return [0, 1].
#


class Solution(object):

    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        apps = []
        for num in nums:
            if num <= target:
                if num == target:
                    return [num, ]
                apps.append(num)
        sum = 0
        for app in apps:
            sum = sum + app
            if sum == target:
                pass
print "start"
import requests
url = "http://www.xiami.com/"
proxies = {
    "http": "180.142.128.118:2226",
    "http": "42.159.251.84:41795",
}
headers = {
    "Accept": "application/json, text/javascript, */*; q=0.01",
    "Accept-Encoding": "gzip, deflate",
    "Accept-Language": "zh-CN,zh;q=0.8,en;q=0.6,zh-TW;q=0.4",
    "Cache-Control": "no-cache",
    "Connection": "keep-alive",
    "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
    "Pragma": "no-cache",
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.82 Safari/537.36",
    "Upgrade-Insecure-Requests": 1
}

r = requests.get(url, proxies=proxies, headers=headers, timeout=60)
print r.content
