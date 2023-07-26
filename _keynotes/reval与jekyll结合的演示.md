---
title: Reveal.js与Jekyll结合演示(幻灯片)
description : Reveal.js与Jekyll结合演示(幻灯片)
date: 2023-07-24
author: "greenwinter"
layout: greenwinter
tags:
    - frontend
theme: league
transition: slide 
diagram: true
mathjax: true
---
{% comment %}
	https://kramdown.gettalong.org/options.html
	add {::options syntax_highlighter="nil" /} to disable syntax_highlighter in this page
{% endcomment %}

{::options syntax_highlighter="nil" /}

<section markdown="1">
# Reveal.js + Jekyll 演示

<aside class="notes">
演讲者注记在此: 
TODO: 把这玩意弄成 Note: 的语法
TODO: 现在还有问题，用的是 jekyll kramdown 的markdown渲染器
TODO: 把markdown 两个换行什么的语法搞定
</aside>


</section>
<section markdown="1">

## Maxwell Equations

$$
\begin{align}
  \nabla \times \vec{\mathbf{B}} -\, \frac1c\, \frac{\partial\vec{\mathbf{E}}}{\partial t} & = \frac{4\pi}{c}\vec{\mathbf{j}} \\
  \nabla \cdot \vec{\mathbf{E}} & = 4 \pi \rho \\
  \nabla \times \vec{\mathbf{E}}\, +\, \frac1c\, \frac{\partial\vec{\mathbf{B}}}{\partial t} & = \vec{\mathbf{0}} \\
  \nabla \cdot \vec{\mathbf{B}} & = 0
\end{align}
$$

</section> <section markdown="1">

使用MathJax，语法为 $\LaTeX$。

```tex
$$
\begin{align}
\nabla \times \vec{\mathbf{B}} -\, \frac1c\, \frac{\partial\vec{\mathbf{E}}}{\partial t} & = \frac{4\pi}{c}\vec{\mathbf{j}} \\
\nabla \cdot \vec{\mathbf{E}} & = 4 \pi \rho \\
\nabla \times \vec{\mathbf{E}}\, +\, \frac1c\, \frac{\partial\vec{\mathbf{B}}}{\partial t} & = \vec{\mathbf{0}} \\
\nabla \cdot \vec{\mathbf{B}} & = 0
\end{align}
$$
```

</section> <section markdown="1">

## Seq

```seq
participant Device
participant Browser
participant Server
Browser->Server: username and password
Note over Server: verify password
Note over Server: generate challenge
Server->Browser:  challenge
Browser->Device: challenge
Note over Device: user touches button
Device-->Browser: response
Browser->Server: response
Note over Server: verify response
```

</section> <section markdown="1">

## Seq

语法参见: <https://bramp.github.io/js-sequence-diagrams/>

``````sml
```seq
participant Device
participant Browser
participant Server
Browser->Server: username and password
Note over Server: verify password
Note over Server: generate challenge
Server->Browser:  challenge
Browser->Device: challenge
Note over Device: user touches button
Device-->Browser: response
Browser->Server: response
Note over Server: verify response
```
``````

</section> <section markdown="1">

我定义的语法糖:
sequence类型可以带有动画

```sequence
participant Device
participant Browser
participant Server
Browser->Server: username and password
Note over Server: verify password
Note over Server: generate challenge
Server->Browser:  challenge
Browser->Device: challenge
Note over Device: user touches button
Device-->Browser: response
Browser->Server: response
Note over Server: verify response
```

</section> <section markdown="1">

## Flowchart
```flowchart
a=>operation: Atmel
ATECC508A 
密码学芯片:>http://www.atmel.com/Images/Atmel-8923S-CryptoAuth-ATECC508A-Datasheet-Summary.pdf
b=>operation: Silabs 
EFM8UB11F16G 
单片机 :>https://www.silabs.com/Support%20Documents/TechnicalDocs/EFM8UB1_DataSheet.pdf
c=>inputoutput: USB
d=>operation: 主机

a(right)->b(right)->c(right)->d
```

``````sml
```flowchart
a=>operation: Atmel
ATECC508A 
密码学芯片:>http://www.atmel.com/Images/Atmel-8923S-CryptoAuth-ATECC508A-Datasheet-Summary.pdf
b=>operation: Silabs 
EFM8UB11F16G 
单片机 :>https://www.silabs.com/Support%20Documents/TechnicalDocs/EFM8UB1_DataSheet.pdf
c=>inputoutput: USB
d=>operation: 主机

a(right)->b(right)->c(right)->d
```
``````

参见: <http://flowchart.js.org/>

</section> <section markdown="1">

## Flowchart
```flowchart
st=>start: Start:>http://www.google.com[blank]
e=>end:>http://www.google.com
op1=>operation: My Operation
sub1=>subroutine: My Subroutine
cond=>condition: Yes
or No?:>http://www.google.com
io=>inputoutput: catch something...

st->op1->cond
cond(yes)->io->e
cond(no)->sub1(right)->op1
```

</section> <section markdown="1">

参见: <http://flowchart.js.org/>


``````sml
```flowchart
st=>start: Start:>http://www.google.com[blank]
e=>end:>http://www.google.com
op1=>operation: My Operation
sub1=>subroutine: My Subroutine
cond=>condition: Yes
or No?:>http://www.google.com
io=>inputoutput: catch something...

st->op1->cond
cond(yes)->io->e
cond(no)->sub1(right)->op1
```
``````


</section> <section markdown="1">

## 小目标
 - 首先
 - 先完成一个小目标
 - 比如
 - 开个博客

</section> <section markdown="1">

## One More Thing

</section> <section markdown="1">

它可以远程遥控。Master/Client，以及Token。

控制权限只需要在URL后面加一个GET参数:

```
?multiplex_secret=12345677898098324
```

(由Token获得)

 - 参见本文的[源文件](https://github.com/donlv1997/donlv1997.github.io/blob/main/_keynotes/reval%E4%B8%8Ejekyll%E7%BB%93%E5%90%88%E7%9A%84%E6%BC%94%E7%A4%BA.md)
 - 本文的[控制链接](http://donlv1997.github.io/keynotes/reval与jekyll结合的演示?multiplex_secret=14830192734523284320)

</section> <section markdown="1">

### Tips: 如何手动禁止被控

```javascript
for ( var i in io.managers ) { 
    io.managers[i].removeAllListeners(); 
}
```

我的模板里, 在URL后面加上一个

```
?no_multiplex=true
```

即可执行此段代码.

例如本文的[强制不受控链接](http://donlv1997.github.io/keynotes/reval与jekyll结合的演示?no_multiplex=true)

</section> <section markdown="1">

## Merci.

[Return Home]({{site.url}})

</section> 
