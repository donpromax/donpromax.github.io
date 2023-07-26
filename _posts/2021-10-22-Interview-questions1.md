---
layout:     post
title:      "招聘用面试题库（easy）- 两数之和"
subtitle:   " \"招聘用\""
date:       2021-10-22 13:56:00
author:     "donlv1997"
header-img: "img/post-bg-2015.jpg"
catalog: true
tags:
    - 面试题
---

> “数组遍历基本问题。”

## 题干

给定一个整数数组 `nums` 和一个整数目标值 `target`，请你在该数组中找出**和为目标值 `target`**的那**两个整数**，并返回它们的数组**下标**。

你可以假设每种输入只会对应一个答案。但是，数组中同一个元素在答案里不能重复出现。

你可以按任意顺序返回答案。

[跳过废话，直接看答案 ](#build)

## 示例

<p style="margin: 0 0 1em 0"><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>nums = [2,7,11,15], target = 9
<strong>输出：</strong>[0,1]
<strong>解释：</strong>因为 nums[0] + nums[1] == 9 ，返回 [0, 1] 。
</pre>

<p style="margin: 0 0 1em 0"><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>nums = [2,7,11,15], target = 9
<strong>输出：</strong>[0,1]
<strong>解释：</strong>因为 nums[0] + nums[1] == 9 ，返回 [0, 1] 。
</pre>

<p style="margin: 0 0 1em 0"><strong>示例 3：</strong></p>

<pre>
<strong>输入：</strong>nums = [3,3], target = 6
<strong>输出：</strong>[0,1]
</pre>

复制下面的代码到ide中，并补全函数：

```java
class Solution {
    public int[] twoSum(int[] nums, int target) {

    }
}
```

进阶：尝试使用<img src="https://latex.codecogs.com/svg.latex?o(n)" style="vertical-align:middle;display:inline;margin:0">的算法

提示：试试散列表

<p id = "build"></p>

## 题解

<div style="margin:30px 0">
    <span>利用HashMap实现字典，从而达到</span>
    <img src="https://latex.codecogs.com/svg.latex?o(n)" style="vertical-align:middle;display:inline;margin:0">
    <span>，暴力法为</span>
    <img src="https://latex.codecogs.com/svg.latex?o(n^2)" style="vertical-align:middle;display:inline;margin:0">
    <span>:</span>
</div>

```java
class Solution {
    public int[] twoSum(int[] nums, int target) {
        int n = nums.length;
        Map<Integer, Integer> dict = new HashMap<>();
        for (int i = 0; i < n; i++) {
            dict.put(nums[i], i);
        }
        for (int i = 0; i < n; i++) {
            if (dict.containsKey(target - nums[i])) {
                int idx = dict.get(target - nums[i]);
                if (idx != i) { return new int[] {i, idx}; }
            }
        }
        return null;
    }
}
```