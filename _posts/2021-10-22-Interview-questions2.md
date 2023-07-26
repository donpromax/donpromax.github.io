---
layout:     post
title:      "招聘用面试题库（easy）- 二叉树的层平均值"
subtitle:   " \"招聘用\""
date:       2021-10-22 13:57:00
author:     "donlv1997"
header-img: "img/post-bg-2015.jpg"
catalog: true
tags:
    - 面试题
---

> “BFS基本问题。”

## 题干

给定一个非空二叉树, 返回一个由每层节点平均值组成的数组。

[跳过废话，直接看答案 ](#build)

## 示例

<p style="margin: 0 0 1em 0"><strong>示例 1：</strong></p>

<pre><strong>输入：</strong>
    3
   / \
  9  20
    /  \
   15   7
<strong>输出：</strong>[3, 14.5, 11]
<strong>解释：</strong>第 0 层的平均值是 3 ,  第1层是 14.5 , 第2层是 11 。因此返回 [3, 14.5, 11] 。
</pre>

二叉树的数据格式定义：

```java
// Definition for a binary tree node.
public class TreeNode {
    int val;
    TreeNode left;
    TreeNode right;
    TreeNode() {}
    TreeNode(int val) { this.val = val; }
    TreeNode(int val, TreeNode left, TreeNode right) {
        this.val = val;
        this.left = left;
        this.right = right;
    }
}
```

复制下面的代码到ide中，并补全函数：

```java
class Solution {
    public List<Double> averageOfLevels(TreeNode root) {

    }
}
```

<p id = "build"></p>

## 题解

二叉树的层序遍历：

```java
class Solution {
    public List<Double> averageOfLevels(TreeNode root) {
        Queue<TreeNode> queue = new LinkedList<>();
        List<Double> res = new ArrayList<>();
        queue.add(root);
        // BFS
        while (!queue.isEmpty()) {
            int size = queue.size();
            double sum = 0;
            for (int i = 0; i < size; i++) {
                TreeNode node = queue.remove();
                sum += node.val;
                if (node.left != null) queue.add(node.left);
                if (node.right != null) queue.add(node.right);
            }
            res.add(sum / size);
        }
        return res;
    }
}
```