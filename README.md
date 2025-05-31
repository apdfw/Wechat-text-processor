# WeChat Text Processor / 微信文本处理器

### Overview/概述
WeChat Text Processor is a Python tool designed to clean and format exported WeChat chat histories. It transforms raw exported text from WeChat's "Export to Email" function into clean, readable format by removing unnecessary elements, anonymizing user names, and organizing the conversation flow.

微信文本处理器是一个Python工具，专门用于清理和格式化导出的微信聊天记录。它将微信"导出到邮箱"功能产生的原始文本转换为干净、易读的格式，通过移除不必要的元素、匿名化用户名称并整理对话流程。

### Features/功能特点
- **Automated Text Cleaning**: Removes headers, timestamps, and system messages
自动文本清理: 移除标题、时间戳和系统消息

- **User Anonymization**: Replaces real names with Speaker1, Speaker2, etc.
用户匿名化: 将真实姓名替换为Speaker1、Speaker2等

- **Chat History Simplification**: Combines consecutive messages from the same speaker
聊天记录简化: 合并同一发言者的连续消息

- **Support for Both Chat Types**: Works with both group chats and private 2-user chats
支持两种聊天类型: 适用于群聊和私人双人聊天

- **Interactive Processing**: Step-by-step guided process with real-time feedback
交互式处理: 逐步引导过程，提供实时反馈

- **Chinese Text Support**: Full support for Chinese characters and punctuation
中文文本支持: 完全支持中文字符和标点符号

### Prerequisites/系统要求
- Python 3.6 or higher
Python 3.6或更高版本

- No additional libraries required (uses only built-in Python modules)
无需额外库（仅使用Python内置模块）

### Installation\安装说明

1. Download the `wechat_processor.py` file
下载wechat_processor.py文件
2. Ensure Python 3.6+ is installed on your system
确保系统已安装Python 3.6+
3. Place the file in your desired working directory
将文件放置在您期望的工作目录中

### Quick Start Guide
快速开始指南


#### Step 1: Export WeChat Chat
步骤1: 导出微信聊天记录

1. Open WeChat on your device
在设备上打开微信
2. Navigate to the chat you want to process (group or private)
导航到要处理的聊天（群聊或私聊）

3. Select up to 100 messages(Despite that Wechat has a limitation of allowing only an export of 100 messages at once, the program can process more than 100 messages at once)
选择最多100条消息(尽管微信最多只能一次导出100条信息，但此程序可以单次运行处理更多条信息)

4. Tap "Export to Email" and copy the text content
点击"导出到邮箱"并复制文本内容


#### Step 2: Run the Processor python wechat_processor.py
步骤2: 运行脚本 python wechat_processor.py

Step 3: Follow the Interactive Prompts
步骤3: 按照交互提示操作

The program will guide you through 6 processing sections:
程序将引导您完成6个处理部分：

1.Information Collection: Paste your exported text and provide chat details
信息收集: 粘贴导出文本并提供聊天详情

2.Simple Processing: Remove basic unnecessary elements
简单处理: 移除基本不必要元素

3.Sophisticated Processing: Replace real names with anonymous speakers
复杂处理: 将真实姓名替换为匿名发言者

4.Time Removal: Remove timestamps from messages
时间移除: 从消息中移除时间戳

5.Full Stop Check: Add proper Chinese punctuation
句号检查: 添加适当的中文标点符号

6.Chat History Simplification: Combine consecutive messages
聊天记录简化: 合并连续消息

Input/Output Examples 输入/输出使用例

Input (Raw WeChat Export)输入部分(原始微信导出的文本):

“Dear:
微信群"这是一个微信群"的聊天记录如下:
—————  2025-5-31  —————
蜘蛛侠 12:57
这是第一句话

蝙蝠侠 13:04
这是第二句话

超人 13:05
这是第三句话

发自我的 iPad”

Output (Processed Text)/输出部分(整理、匿名化后的文本):

“Speaker1: 这是第一句话。
Speaker2: 这是第二句话。
Speaker3: 这是第三句话。”

File Output
文件输出

File Created: wechat_export.txt in the same directory
创建文件: 在同一目录下生成wechat_export.txt
Content: Clean, processed chat history
内容: 干净的处理后聊天记录
Encoding: UTF-8 for proper Chinese character support
编码: UTF-8，确保中文字符正确支持

Common Issues:
常见问题:

Encoding Errors: Ensure your terminal supports UTF-8
编码错误: 确保终端支持UTF-8
Invalid Date Format: Use YYYY-MM-DD or YYYY-M-D format only
无效日期格式: 仅使用YYYY-MM-DD或YYYY-M-D格式
Empty Results: Check if user names were entered correctly
结果为空: 检查用户名是否正确输入
Program Crashes: Verify Python 3.6+ is installed
程序崩溃: 验证已安装Python 3.6+
Device differences: If you have exported the chat history from a device that is not an ipad, just change the replacing string from '发自我的 iPad' into yours corresponding version.
设备差异：如果你导出聊天记录的设备并非是平板，你只需要将程序中的“发自我的 iPad”这一字符替换成你设备的对应版本即可

Error Messages:
报错反馈:

"Invalid choice": Enter only 1 or 2 for chat type selectionInvalid choice": 
聊天类型选择只能输入1或2

"Name cannot be empty": All user names are required
所有聊天记录的对应用户名都需要给予程序的

"Invalid date format": Follow YYYY-MM-DD format guidelines
遵循YYYY-MM-DD格式指南

Processing Sections:处理部分：

Information Collection: Gathers user input and validates data
信息收集: 收集用户输入并验证数据
Simple Processing: Removes "Dear:", "发自我的 iPad", headers, and date separators
简单处理: 移除"Dear:"、"发自我的 iPad"、标题和日期分隔符
Sophisticated Processing: Anonymizes names using Speaker1:, Speaker2:, etc.
复杂处理: 使用Speaker1:、Speaker2:等匿名化姓名

Time Removal: Eliminates HH:MM timestamp patterns
时间移除: 消除HH:MM时间戳模式
Full Stop Check: Adds Chinese periods (。) where missing
句号检查: 在缺失处添加中文句号(。)
Chat History Simplification: Merges consecutive messages from same speaker
聊天记录简化: 合并同一发言者的连续消息
Supported Date Formats(Depends on the date format exported from your Wechat):
支持的日期格式(以您微信导出为邮件后所显示的时间格式而异):

2025-5-31 (single digit month/day)
2025-5-31（单位数月/日）

2025-05-31 (double digit month/day)
2025-05-31（双位数月/日）

2025-5-31 and 2025-05-31 (mixed formats)
2025-5-31和2025-05-31（混合格式）

Communication and feedback联系与反馈
For any questions or advices occurred, please ensure that you've followed all provided formats and guidelines. For contact, please email at xieqiaorui2007@yeah.net 
如有问题或建议，请检查您的输入格式并确保遵循所有使用指南。如需联系，请邮件xieqiaorui2007@yeah.net 

License / 许可证
This project is open source. Feel free to modify and distribute according to your needs.
本项目为开源项目，您可以根据需要自由修改和分发。
