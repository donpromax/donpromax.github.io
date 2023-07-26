---
layout:     post
title:      "招聘用面试题库（easy）- 反转链表"
subtitle:   " \"招聘用\""
date:       2021-10-22 13:58:00
author:     "donlv1997"
header-img: "img/post-bg-2015.jpg"
catalog: true
mathjax: true
tags:
    - 面试题
---

> “链表基本问题。”

## 题干

给你单链表的头节点 $head$ ，请你反转链表，并返回反转后的链表。

![alt 属性文本](/img/2021/rev1ex1.jpg)

[跳过废话，直接看答案 ](#build)

## 示例

<p style="margin: 0 0 1em 0"><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>head = [1,2,3,4,5]
<strong>输出：</strong>[5,4,3,2,1]
</pre>

<p style="margin: 0 0 1em 0"><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>head = []
<strong>输出：</strong>[]
</pre>

链表的数据格式定义：

```java
// Definition for singly-linked list.  
class ListNode {  
    int val;  
    ListNode next;  
    ListNode() {}  
    ListNode(int val) { this.val = val; }  
    ListNode(int val, ListNode next) { this.val = val; this.next = next; }  
}  
```

复制下面的代码到ide中，并补全函数：

```java
class Solution {
    public ListNode reverseList(ListNode head) {

    }
}
```
<p id = "build"></p>

## 题解

数据结构基本问题，较容易，但是可以考察面试者基本编码素质和心理素质：

```java
class Solution {
    public ListNode reverseList(ListNode head) {
        if (head == null) { return null; }
        if (head.next == null) { return head; }

        ListNode p, q, tmp;
        p = head;
        q = head.next;

        p.next = null;
        while (q != null) {
            tmp = q.next;
            q.next = p;

            p = q;
            q = tmp;
        }
        return p;
    }
}
```