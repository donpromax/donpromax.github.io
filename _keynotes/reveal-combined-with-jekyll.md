---
title: Reveal.js与Jekyll结合演示(幻灯片)
description : Reveal.js与Jekyll结合演示(幻灯片)
date: 2023-07-24
author: greenwinter
layout: keynote
diagram: true
theme: league
tags:
    - frontend
---
{::options syntax_highlighter="nil" /}

{% comment %}
	https://kramdown.gettalong.org/options.html
	add {::options syntax_highlighter="nil" /} to disable syntax_highlighter in this page
{% endcomment %}

{% comment %}
	use markdown="1" to enable kramdown markdown parser
  use data-markdown to enable reveal.js markdown parser
{% endcomment %}

<section data-auto-animate>
<h1> Reveal.js + Jekyll 演示 </h1>

    <aside class="notes">
        Oh hey, these are some notes. They'll be hidden in your presentation, but you can see them if you open the speaker notes window (hit 's' on your keyboard).
    </aside>
</section> 

<section markdown="1" data-auto-animate>

## Maxwell Equations

$$
\begin{align}
  \nabla \times \vec{\mathbf{B}} -\, \frac1c\, \frac{\partial\vec{\mathbf{E}}}{\partial t} & = \frac{4\pi}{c}\vec{\mathbf{j}} \\
  \nabla \cdot \vec{\mathbf{E}} & = 4 \pi \rho \\
  \nabla \times \vec{\mathbf{E}}\, +\, \frac1c\, \frac{\partial\vec{\mathbf{B}}}{\partial t} & = \vec{\mathbf{0}} \\
  \nabla \cdot \vec{\mathbf{B}} & = 0
\end{align}
$$

</section> <section data-markdown data-auto-animate>

使用MathJax，语法为 $\LaTeX$。

```tex [2-7]
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
</section> <section data-markdown data-auto-animate>

## Seq

语法参见: <https://bramp.github.io/js-sequence-diagrams/>

``````plaintext [2-4|5-13]
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

</section> <section markdown="1" data-auto-animate>

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

``````plaintext
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

</section> <section markdown="1" data-auto-animate>

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

</section> <section markdown="1" data-auto-animate>

参见: <http://flowchart.js.org/>


``````plaintext
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


</section> <section markdown="1" data-auto-animate>

## 小目标
 - {: .fragment} 首先
 - {: .fragment} 先完成一个小目标
 - {: .fragment} 比如
 - {: .fragment} 开个博客

</section> <section data-markdown data-auto-animate>

## One More Thing

</section> <section data-markdown data-auto-animate>

可以远程遥控

 - 参见本文的[源文件](https://github.com/donlv1997/donlv1997.github.io/blob/main/_keynotes/reval%E4%B8%8Ejekyll%E7%BB%93%E5%90%88%E7%9A%84%E6%BC%94%E7%A4%BA.md)
 - 本文的[控制链接]({{ page.url }})

</section> <section data-markdown data-auto-animate>

## Merci.

[Return Home]({{site.url}})

</section> 
