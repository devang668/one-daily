# one-daily
good good study ，day day up

注意如果要克隆一个自己使用
参考`https://github.com/devang668/jbook` 哦,他做了一些优化会更适合一些，他那个是在这个one-daily上进一步优化的。

[网站样子](https://daily.devang.top/)

已经打算重新使用python本地构建了，所以新的blog位于 https://devang.top


[快速开始吧](https://github.com/devang668/one-daily/new/main/thoughts) 

 也可复制  `https://github.com/devang668/one-daily/tree/main/thoughts`

## 写作方式

现在不需要手写 Jekyll 的 `_posts/YYYY-MM-DD-title.md` 和 front matter 了。
站点也已经支持 PWA 风格安装和离线缓存，移动端访问会更像一个轻量应用。

平时只要这样写：

1. 在 `thoughts/` 新建一个 `.md` 文件，文件名可以随意。
2. 第一行写标题。
3. 空一行后直接写正文。
4. 提交推送，GitHub Pages 会自动更新。

示例：

```md
今天的小想法

这里直接写正文。
想贴链接、图片、代码块都可以。
```

补充规则：

- 如果文件名里带日期，比如 `0329.md`、`2026-03-29-ai.md`，系统会优先用它。
- 如果文件名里没有日期，就自动使用这个文件最近一次提交的日期。
- `thoughts/README.md` 不会被当成文章发布。
- 自动发布只扫描 `thoughts/` 目录，其他说明文件不会被误发到博客上。

## Cloudflare Pages

如果部署到 Cloudflare Pages，并使用根域名或子域名，比如 `https://one.devang.top/`，不要直接用默认的 `_config.yml`，否则 `baseurl: /one-daily` 会让样式和脚本地址指错。

Cloudflare Pages 建议这样填：

- Production branch: `main`
- Framework preset: `Jekyll` 或 `None`
- Build command: `python scripts/generate_posts.py && bundle exec jekyll build --config _config.yml,_config.cloudflare.yml`
- Build output directory: `_site`

这样 GitHub Pages 仍然走 `/one-daily/`，Cloudflare Pages 则会自动走根路径 `/`。



# 如果喜欢，给个星星鼓励一下

我的微信
<img width="1080" height="1198" alt="image" src="https://github.com/user-attachments/assets/35b869ea-81dd-416e-a387-2a161f323147" />

