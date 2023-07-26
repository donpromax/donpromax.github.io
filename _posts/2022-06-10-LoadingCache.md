---
layout:     post
title:      "LoadingCache的使用"
subtitle:   "好久没水"
date:       2022-06-10 14:09:00
author:     "donlv1997"
header-img: "img/post-bg-2015.jpg"
catalog: true
mathjax: true
tags:
    - java
---

## 生成一个LoadingCache对象

```java
 
  LoadingCache userCache = CacheBuilder.newBuilder()
                .maximumSize(10000))//设置缓存上线
                .expireAfterAccess(10, TimeUnit.MINUTES)//设置时间对象没有被读/写访问则对象从内存中删除
                .expireAfterWrite(10, TimeUnit.MINUTES)//设置时间对象没有被写访问则对象从内存中删除
                //移除监听器,缓存项被移除时会触发
                .removalListener(new RemovalListener<String, UserProfile>() {
                    @Override
                    public void onRemoval(RemovalNotification<String, UserProfile> notification) {
                       //逻辑
                        }
                    }
                })
                .recordStats()
                //CacheLoader类 实现自动加载
                .build(new CacheLoader<String, Object>() {
                    @Override
                    public Object load(String key) {
                       // 获取对象
                    }
                });
```

## 使用LoadingCache

1) <code>V get(K k)</code>: 内部调用<code>getOrLoad(K key)</code>方法，缓存中有对应的值则返回，没有则使用<code>CacheLoader.load()</code>方法 <code>getOrLoad(K key)</code>方法为线程安全方法，内部加锁

2) <code>V getIfPresent(Object key)</code>: 缓存中有对应的值则返回，没有则返回<code>NULL</code>

3) <code>long size()</code>: 缓存对象数量

4) <code>put(K key, V value)</code>: 直接显示地向缓存中插入值，这会直接覆盖掉已有键之前映射的值。

5) <code>invalidate(Object key)</code>: 显式地清除指定key的缓存对象

