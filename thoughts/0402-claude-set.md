# 为什么会出现claude code 配置失败

如图，这是我的一个ccmmate里面的配置：

<img width="1740" height="963" alt="image" src="https://github.com/user-attachments/assets/276a397e-e642-4426-aef8-41dd23f9265b" />

非常的简单。

我发现，使用minimax就可以通过，但是，使用支持openai样式的就不可以使用，这就好奇了。

所以决定来搞一搞。

先去使用deepseek，他后来兼容了athropic的样式，同时还支持openai样子的调用。

sk-4f654479949b46b688c7****
https://api.deepseek.com/v1
deepseek-chat

--

athropic  https://api.deepseek.com/anthropic

--

```
# Please install OpenAI SDK first: `pip3 install openai`
import os
from openai import OpenAI

client = OpenAI(api_key=os.environ.get('DEEPSEEK_API_KEY'), base_url="https://api.deepseek.com")

response = client.chat.completions.create(
    model="deepseek-chat",
    messages=[
        {"role": "system", "content": "You are a helpful assistant"},
        {"role": "user", "content": "Hello"},
    ],
    stream=False
)

print(response.choices[0].message.content)
```
最后得到了回答，那么切换成为普通的openai样式的
<img width="1396" height="1204" alt="image" src="https://github.com/user-attachments/assets/b4917fda-eac1-4ad6-85c7-2e2af8b453e9" />


<img width="1730" height="1092" alt="image" src="https://github.com/user-attachments/assets/cd4c0068-e024-433d-9b3b-bba9b050d40e" />

很显然，这个软件自己不支持那样的修改。
