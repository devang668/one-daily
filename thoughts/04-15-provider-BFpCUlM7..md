# provider-BFpCUlM7.js报错解决办法


如

npm-global\\node_modules\\openclaw\\dist\\provider-BFpCUlM7.js
    code: 'MODULE_NOT_FOUND',
    requireStack: [

OpenClaw 启动时控制台出现以下警告：                                                                                   
  [gateway-http] stage "slack" threw — skipping: Error: Cannot find module '@slack/bolt'

  错误信息：
  Require stack:
  - D:\at-soft\1-sy\node\npm-global\node_modules\openclaw\dist\provider-BFpCUlM7.js

  原因

  OpenClaw 的 Slack 扩展代码引用了 @slack/bolt 模块，但该模块未随 OpenClaw 一起安装。这是 Slack
  功能的一个可选依赖，不影响其他功能正常运行。

  解决方法

  方法一：注释掉引用代码（推荐）

  找到 provider-BFpCUlM7.js 文件：

  文件路径：
  <openclaw安装目录>/dist/provider-BFpCUlM7.js

  找到并注释掉以下两行（第 69-70 行）：
  // import * as SlackBoltNamespace from "@slack/bolt";
  // import SlackBolt from "@slack/bolt";

  方法二：安装缺失的模块

  如果你需要使用 Slack 功能，可以安装 @slack/bolt：

  cd <openclaw安装目录>
  npm install @slack/bolt

  验证

  重启 OpenClaw，检查控制台输出中是否还有 stage "slack" threw 的警告。如果不再出现，说明问题已解决。

  ---
  适用于 OpenClaw 版本 2026.4.2
