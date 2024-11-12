'''
"image generator",
    "Consensus",
    "Write For Me",
    "Logo Creator",
    "Canva",
    "Scholar GPT",
    "Code Copilot",
    "Cartoonize Yourself",
    "Diagrams: Show Me | charts, presentations, code",
    "Python",
    "Humanizer Pro",
    "AskYourPDF Research Assistant",
    "PDF Ai PDF",
    "Grimoire",
    "Scholar AI",
    "Wolfram",
    "Video GPT by VEED",
    "WebPilot",
    "GPT-4",
    "?Academic Assistant Pro",
    "Video Maker",
    "?Professional Coder (Auto programming)",
    "math",
    "Whimsical Diagrams",
    "Super Describe",
    "Photo Realistic GPT",
    "Photo Multiverse",
    "Glibatree Art Designer",
    "LOGO",
    "Universal Primer",
    "NEO - Ultimate AI",
    "??All-around Writer (Professional Version)",
    "Slide Maker: PowerPoints, Presentations",
    "code: python java c html sql javascript react web+",
    "Astrology Birth Chart GPT",
    "AI Humanizer Pro",
    "Tutor Me",
    "Excel GPT",
    "Video Maker",
    "Video Tutor????",
    "Finance Wizard",
    "DesignerGPT",
    "Math Solver",
    "Presentation and Slides GPT: PowerPoints, PDFs",
    "SciSpace",
    "Consistent Character GPT?? Fast & High Quality??",
    "Copywriter GPT - Marketing, Branding, Ads",
    "Books",
    "Mia AI, your AI Life Coach with Voice",
    "Voxscript",

names = [
    "image generator",
    "Consensus",
    "Write For Me",
    "Logo Creator",
    "Canva",
    "Scholar GPT",
    "Code Copilot",
    "Cartoonize Yourself",
    "Diagrams: Show Me | charts, presentations, code",
    "Python",
    "Humanizer Pro",
    "AskYourPDF Research Assistant",
    "PDF Ai PDF",
    "Grimoire",
    "Scholar AI",
    "Wolfram",
    "Video GPT by VEED",
    "WebPilot",
    "GPT-4",
    "?Academic Assistant Pro",
    "Video Maker",
    "?Professional Coder (Auto programming)",
    "math",
    "Whimsical Diagrams",
    "Super Describe",
    "Photo Realistic GPT",
    "Photo Multiverse",
    "Glibatree Art Designer",
    "LOGO",
    "Universal Primer",
    "NEO - Ultimate AI",
    "??All-around Writer (Professional Version)",
    "Slide Maker: PowerPoints, Presentations",
    "code: python java c html sql javascript react web+",
    "Astrology Birth Chart GPT",
    "AI Humanizer Pro",
    "Tutor Me",
    "Excel GPT",
    "Video Maker",
    "Video Tutor????",
    "Finance Wizard",
    "DesignerGPT",
    "Math Solver",
    "Presentation and Slides GPT: PowerPoints, PDFs",
    "SciSpace",
    "Consistent Character GPT?? Fast & High Quality??",
    "Copywriter GPT - Marketing, Branding, Ads",
    "Books",
    "Mia AI, your AI Life Coach with Voice",
    "Voxscript",
    "AutoExpert (Dev)",
    "Video Summarizer",
    "Diagrams & Data: Research, Analyze, Visualize",
    "Humanize AI",
    "DeepGame",
    "ロMidjourneyロ -- MJ Prompt Generator (V6)",
    "Drawn to Style",
    "チャットGPT",
    "Image Edit and img2img",
    "Tattoo GPT",
    "Summary ?YouTube PDF Book Article Website",
    "22.500+ Best Custom GPTs",
    "Fully SEO Optimized Article including FAQ's",
    "Browser Pro",
    "KAYAK - Flights, Hotels & Cars",
    "Resume",
    "Midjourney",
    "超级PPT生成（Super PPT）",
    "更勤奋更聪明的GPT4",
    "Link Reader",
    "PDF Reader",
    "?Academic Assistant Pro",
    "Prompt Perfect",
    "physics",
    "super-rephrase-soft",
    "AI Humanizer & Paraphraser",
    "Paper Interpreter (Japanese)",
    "MARKETING",
    "DALL·??3 Ultra: image & art generator+ editing",
    "Murder Mystery Mayhem",
    "CrewAI Assistant",
    "AutoExpert (Academic)",
    "AI Tutor",
    "Blog Expert - SEO Blogs made easy!",
    "PDF Keymate AI Search",
    "Code Tutor",
    "AutoExpert (Chat)",
    "Essay Writer ?",
    "Human Writer, Humanizer, Paraphraser(Human AI)??",
    "Automated Writer",
    "GymStreak Workout Creator",
    "Cover Letter",
    "Python",
    "Mid Journey V6 Prompt Creator",
    "Video Generator",
    "Generator Text to Video Maker",
    "Website Generator",
    "Email",
    "Plot AI",
    "Web Browser",

]
'''

import pandas as pd
import subprocess

def extract_app_names(file_path):
    try:
        # 尝试使用utf-8编码读取CSV文件，如果失败则使用latin1编码
        try:
            df = pd.read_csv(file_path, encoding='utf-8')
        except UnicodeDecodeError:
            df = pd.read_csv(file_path, encoding='gbk')
        # 提取第二列的应用名称
        app_names = df.iloc[:, 1].tolist()  # 假设第二列为应用名称列
        return app_names
    except Exception as e:
        print(f"读取文件时出错: {e}")
        return []

# 设置文件路径
file_path = 'top_1000_gpts_with_new_urls.csv'

# 调用函数并打印应用名称列表
app_names = extract_app_names(file_path)
# print(app_names)

counter = 1
with open("cmd_100.txt", "w", encoding="gbk") as file:
    for name in app_names:
        command = f'python appcrazy.py --appname "{name}" --file "output_add_4/{counter}.csv"'
        file.write(command + "\n")
        counter += 1
        if counter == 11:
            break

def execute_commands_from_file(file_path):
    # 打开文件并逐行读取命令
    with open(file_path, 'r', encoding='gbk') as file:
        i = 1
        for line in file:
            command = line.strip()  # 去除首尾空白字符
            if command:  # 确保命令不为空
                try:
                    # 执行命令并等待完成
                    result = subprocess.run(command, shell=True, check=True, text=True, capture_output=True)
                    print(f"执行成功: {i}\n")
                    i += 1
                except subprocess.CalledProcessError as e:
                    print(f"执行失败: {command}\n")

# 使用函数执行命令
file_path = 'cmd_100.txt'  # 你的 txt 文件路径
execute_commands_from_file(file_path)