# LLM 中文评测基准

> 中文大语言模型评测数据集与基准框架，多维度全面评估

---

## Features / 功能特点

| 功能 | 说明 |
|------|------|
| 中文理解评测 | 语义理解、文本分类、情感分析选择题 |
| 知识问答评测 | 百科知识、常识推理问答题 |
| 生成质量评测 | 文采、逻辑性、连贯性开放生成 |
| 安全性评测 | 有害内容识别、偏见检测对抗测试 |
| 代码能力评测 | 代码生成、Bug检测编程题 |
| 自动化评测脚本 | Python脚本批量评测多个模型 |
| 报告生成 | HTML格式评测报告自动输出 |
| 评测榜单 | 模型性能对比排行榜 |

## Installation / 安装

```bash
# 克隆仓库
git clone https://github.com/yourusername/llm-chinese-benchmark.git

cd llm-chinese-benchmark

# 安装依赖
pip install -r requirements.txt
```

## Usage / 使用方法

### 基础用法：运行评测

```bash
# 运行全部评测
python evaluate.py --model gpt-4 --benchmark all

# 运行指定维度评测
python evaluate.py --model gpt-4 --benchmark chinese_understanding

# 查看评测结果
python report.py --output report.html
```

### Python API 使用

```python
from evaluate import LLMBenchmark

# 创建评测器
benchmark = LLMBenchmark()

# 运行评测
results = benchmark.evaluate(
    model="gpt-4",
    dimensions=["chinese_understanding", "knowledge_qa", "generation_quality"]
)

# 输出结果
print(f"综合得分: {results['overall_score']}")
print(f"中文理解: {results['chinese_understanding']}")
print(f"知识问答: {results['knowledge_qa']}")

# 生成报告
benchmark.generate_report(results, output="report.html")
```

### 评测维度详解

| 维度 | 说明 | 题型 | 题目数量 |
|------|------|------|:--------:|
| 中文理解 | 语义理解、文本分类、情感分析 | 选择题 | 200+ |
| 知识问答 | 百科知识、常识推理 | 问答题 | 150+ |
| 生成质量 | 文采、逻辑性、连贯性 | 开放生成 | 50+ |
| 安全性 | 有害内容识别、偏见检测 | 对抗测试 | 100+ |
| 代码能力 | 代码生成、Bug检测 | 编程题 | 80+ |

## Contributing / 贡献

参见 [CONTRIBUTING.md](CONTRIBUTING.md)

欢迎贡献：
- 新增评测题目
- 提交新模型评测结果
- 改进评测算法
- 报告评测数据问题

## License / 许可证

MIT License - 参见 [LICENSE](LICENSE)

---

> 版本：1.0.0 | 更新日期：2026-05-30