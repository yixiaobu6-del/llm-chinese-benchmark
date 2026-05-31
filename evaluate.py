"""LLM中文评测基准 - 核心评测引擎"""

import json
import os
from typing import Dict, List, Optional


class LLMBenchmark:
    """中文大语言模型多维度评测器"""

    DIMENSIONS = {
        "chinese_understanding": "中文理解",
        "knowledge_qa": "知识问答",
        "generation_quality": "生成质量",
        "safety": "安全性",
        "code": "代码能力",
    }

    def __init__(self, data_dir: str = None):
        self.data_dir = data_dir or os.path.join(os.path.dirname(__file__), "content")
        self.questions = self._load_questions()

    def _load_questions(self) -> dict:
        """加载评测题目"""
        questions_path = os.path.join(self.data_dir, "评测数据.json")
        if os.path.exists(questions_path):
            with open(questions_path, "r", encoding="utf-8") as f:
                return json.load(f)
        return {d: [] for d in self.DIMENSIONS}

    def evaluate(self, model: str,
                 dimensions: Optional[List[str]] = None) -> dict:
        """对指定模型进行评测"""
        dims = dimensions or list(self.DIMENSIONS.keys())
        scores = {}
        total, total_score = 0, 0
        for dim in dims:
            qs = self.questions.get(dim, [])
            if not qs:
                scores[dim] = 0
                continue
            dim_score = sum(self._score_question(q, model) for q in qs)
            avg = dim_score / len(qs)
            scores[f"{dim}_score"] = round(avg, 1)
            total += len(qs)
            total_score += dim_score

        scores["overall_score"] = round(total_score / max(total, 1), 1)
        return scores

    def _score_question(self, question: dict, model: str) -> float:
        """评分单题（存根，实际可对接API）"""
        return question.get("score", 0)

    def generate_report(self, results: dict, output: str = "report.html"):
        """生成评测报告"""
        from datetime import datetime
        html = f"""<!DOCTYPE html>
<html lang="zh-CN">
<head><meta charset="UTF-8"><title>LLM中文评测报告</title>
<style>
body {{ font-family: -apple-system, sans-serif; max-width: 800px; margin: auto; padding: 20px; }}
table {{ width: 100%; border-collapse: collapse; margin: 20px 0; }}
th, td {{ padding: 10px; text-align: left; border-bottom: 1px solid #ddd; }}
th {{ background: #f5f5f5; }}
.score-good {{ color: green; }}
.score-warn {{ color: orange; }}
.score-bad {{ color: red; }}
</style></head>
<body>
<h1>LLM中文评测报告</h1>
<p>生成时间: {datetime.now().strftime("%Y-%m-%d %H:%M")}</p>
<table>
<tr><th>维度</th><th>得分</th></tr>
"""
        for k, v in results.items():
            if k.endswith("_score"):
                label = self.DIMENSIONS.get(k.replace("_score", ""), k)
                cls = "score-good" if v >= 80 else "score-warn" if v >= 60 else "score-bad"
                html += f'<tr><td>{label}</td><td class="{cls}">{v}/100</td></tr>\n'

        html += f'</table>\n<h2>综合得分: <span class="score-{"good" if results.get("overall_score", 0) >= 80 else "warn"}">{results.get("overall_score", 0)}/100</span></h2>'
        html += "</body></html>"

        with open(output, "w", encoding="utf-8") as f:
            f.write(html)
        print(f"报告已生成: {output}")


if __name__ == "__main__":
    bm = LLMBenchmark()
    results = bm.evaluate("test-model")
    print(json.dumps(results, ensure_ascii=False, indent=2))
    bm.generate_report(results)
