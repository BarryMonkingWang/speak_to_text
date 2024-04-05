#!/bin/bash

# 从麦克风生产音频数据
python /Users/wangzhichao/PycharmProjects/faster_whisper/get_mp3_fromMic/get_mp3_mic.py

MP3_FILE="output.mp3"

# 检查MP3文件是否存在
if [ -f "$MP3_FILE" ]; then
    echo "MP3文件已生成，文件路径：$MP3_FILE"
else
    echo "未找到MP3文件，请检查 get_mp3_mic.py 脚本。"
    exit 1
fi

# 使用whisper.py处理音频文件，并将输出信息存储到日志文件
LOG_FILE="/Users/wangzhichao/PycharmProjects/faster_whisper/FasterWhisper/log_file.log" # 请修改为您希望存储日志的实际路径

python /Users/wangzhichao/PycharmProjects/faster_whisper/FasterWhisper/whisper.py "$MP3_FILE" >> "$LOG_FILE" 2>&1

# 定义输出文件位置
# （如果有特定的操作需要定义输出文件位置，请在此处进行）

# 删除output.wav和output.mp3，为下一次录音准备
rm -f output.wav output.mp3

echo "已删除output.wav和output.mp3，可以进行下一次录音。"
echo "whisper.py的输出已存储到日志文件 $LOG_FILE。"
