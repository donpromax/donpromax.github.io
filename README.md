# donlv1997 blog

[click here](https://donpromax.github.io)

本地使用：bundle exec jekyll serve --watch

## tricks

compress img

```shell
cd img/2025/japan
bash -c 'for file in *.png; do cwebp -q 80 "$file" -o "${file%.png}.webp"; done'
rm -rf *.png
```
