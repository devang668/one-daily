---
layout: default
title: 首页
---

<section class="hero-card">
  <p class="eyebrow">PWA Blog</p>
  <h1>把一天里值得留下来的东西，像记便签一样发到网上。</h1>
  <p class="hero-lead">现在这个博客已经改成移动端优先的 PWA 风格站点。你可以像写普通 Markdown 一样记录，它会自动生成文章并适配手机阅读。</p>
  <div class="hero-actions">
    <a class="primary-action" href="https://github.com/devang668/one-daily/new/main/thoughts" target="_blank" rel="noreferrer">新建一篇</a>
    <a class="secondary-action" href="{{ '/about' | relative_url }}">查看说明</a>
  </div>
</section>

<section class="section-head">
  <div>
    <p class="eyebrow">Latest Notes</p>
    <h2>最近的记录</h2>
  </div>
  <p class="section-note">共 {{ site.posts | size }} 篇</p>
</section>

<ul class="post-grid">
{% for post in site.posts %}
  {% assign preview = post.content | strip_html | strip_newlines | strip | truncate: 96 %}
  <li class="post-card">
    <a class="post-card-link" href="{{ post.url | relative_url }}">
      <div class="post-card-meta">
        <span>{{ post.date | date: "%Y-%m-%d" }}</span>
        <span>随记</span>
      </div>
      <h3>{{ post.title }}</h3>
      <p>{% if preview == "" %}这篇记录很短，打开看完整内容。{% else %}{{ preview }}{% endif %}</p>
      <span class="post-card-more">继续阅读</span>
    </a>
  </li>
{% endfor %}
</ul>
