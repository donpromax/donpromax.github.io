---
layout:     post
title:      "Java Builder流式写法"
subtitle:   "reading effective java"
date:       2021-11-03 11:17:00
author:     "donlv1997"
header-img: "img/post-bg-2015.jpg"
catalog: true
mathjax: true
tags:
    - java
---

> “how to implement elegant constructor in Java”

## Builder Pattern

比如用一个类表示包装食品外面显示的营养成分标签。 这些标签中有几个域是必需的:每份的含量、每罐的含量以及每份的卡路里。还有超过20个的可选域:总脂肪量、饱和脂肪量、转化脂肪、胆固醇、纳，等等。大多数产品在某几个可选域中都会有非零的值。

```java
// Builder Pattern
public class NutritionFacts {
    private final int servingSize;
    private final int servings;
    private final int calories;
    private final int fat;
    private final int sodium;
    private final int carbohydrate;

    public static class Builder {
        // Required parameters
        private final int servingSize;
        private final int servings;

        // Optional parameters - initialized to default values
        private int calories      = 0;
        private int fat           = 0;
        private int sodium        = 0;
        private int carbohydrate  = 0;

        public Builder(int servingSize, int servings) {
            this.servingSize = servingSize;
            this.servings    = servings;
        }

        public Builder calories(int val)
        { calories = val;      return this; }
        public Builder fat(int val)
        { fat = val;           return this; }
        public Builder sodium(int val)
        { sodium = val;        return this; }
        public Builder carbohydrate(int val)
        { carbohydrate = val;  return this; }

        public NutritionFacts build() {
            return new NutritionFacts(this);
        }
    }

    private NutritionFacts(Builder builder) {
        servingSize  = builder.servingSize;
        servings     = builder.servings;
        calories     = builder.calories;
        fat          = builder.fat;
        sodium       = builder.sodium;
        carbohydrate = builder.carbohydrate;
    }
}
```

使用Builder模式的好处在于，可以流式地构建对象，并且对可选性和必选项做了很好的区分（like in python and scala），同时可以保证免受攻击：

```java
NutritionFacts cocaCola = new NutritionFacts.Builder(240, 8)
    .calories(100).sodium(35).carbohydrate(27).build();
```

## 抽象类的Builder Pattern

假设抽象类`Pizza`用来表示各种各样的Pizza

```java
// Builder pattern for class hierarchies
public abstract class Pizza {
    public enum Topping { HAM, MUSHROOM, ONION, PEPPER, SAUSAGE }
    final Set<Topping> toppings;

    abstract static class Builder<T extends Builder<T>> {
        EnumSet<Topping> toppings = EnumSet.noneOf(Topping.class);
        public T addTopping(Topping topping) {
            toppings.add(Objects.requireNonNull(topping));
            return self();
        }

        abstract Pizza build();

        // Subclasses must override this method to return "this"
        protected abstract T self();
    }
    
    Pizza(Builder<?> builder) {
        toppings = builder.toppings.clone();
    }
}
```

Pizza.Builder是一个带有递归的范型`<T extends Builder<T>>`，允许在子类中适当地进行方法链接，不需要转换类型。

这里有两个具体的 Pizza 子类，其中 一个表示经典纽约风味的比萨，另一个表示馅料内置的半月型(calzone)比萨。前者需要一个尺寸参数，后者则要你指定酱汁应该内置还是外置:

```java
// Subclass with hierarchical builder
public class NyPizza extends Pizza {
    public enum Size { SMALL, MEDIUM, LARGE }
    private final Size size;

    public static class Builder extends Pizza.Builder<Builder> {
        private final Size size;

        public Builder(Size size) {
            this.size = Objects.requireNonNull(size);
        }

        @Override public NyPizza build() {
            return new NyPizza(this);
        }

        @Override protected Builder self() { return this; }
    }

    private NyPizza(Builder builder) {
        super(builder);
        size = builder.size;
    }

    @Override public String toString() {
        return "New York Pizza with " + toppings;
    }
}
```

```java
// Subclass with hierarchical builder
public class Calzone extends Pizza {
    private final boolean sauceInside;

    public static class Builder extends Pizza.Builder<Builder> {
        private boolean sauceInside = false; // Default

        public Builder sauceInside() {
            sauceInside = true;
            return this;
        }

        @Override public Calzone build() {
            return new Calzone(this);
        }

        @Override protected Builder self() { return this; }
    }

    private Calzone(Builder builder) {
        super(builder);
        sauceInside = builder.sauceInside;
    }

    @Override public String toString() {
        return String.format("Calzone with %s and sauce on the %s",
                toppings, sauceInside ? "inside" : "outside");
    }
}
```

注意，每个子类的构建器中的`build`方法，都声明返回正确的子类: `NyPizza.Builder`的`build`方法返回`NyPizza`，而`Calzone.Builder`中的则返回`Calzone`。在该方法中，子类方法声明返回超级类中声明的返回类型的子类型，这被称作协变返回类型(covariant return type)。它允许客户端无须转换类型就能使用这些构建器。How to use:

```java
// Using the hierarchical builder
public class PizzaTest {
    public static void main(String[] args) {
        NyPizza pizza = new NyPizza.Builder(SMALL)
                .addTopping(SAUSAGE).addTopping(ONION).build();
        Calzone calzone = new Calzone.Builder()
                .addTopping(HAM).sauceInside().build();
        
        System.out.println(pizza);
        System.out.println(calzone);
    }
}
```

与构造器相比，builder的优势在于，它可以有多个可变(varargs)参数。因为builder是利用单独的方法来设置每一个参数。此外，构造器还可以将多次调用某一个方法而传人的参数集中到一个域中，如前面的调用了两次addTopping方法的代码所示。


