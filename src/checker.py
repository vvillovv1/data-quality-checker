import pandas as pd
import os

def run_check(file_path: str):
    df = pd.read_csv(file_path)
    report = []
    report.append("===== 数据质检报告 =====\n")
    report.append(f"数据集行数：{len(df)}，列数：{len(df.columns)}\n")

    # 空值检查
    null_info = df.isnull().sum()
    report.append("【空值统计】")
    report.append(str(null_info))

    # 重复行检查
    dup_cnt = df.duplicated().sum()
    report.append(f"\n【重复行数】{dup_cnt}")

    # 负数检查
    for col in df.select_dtypes(include=['number']).columns:
        neg_cnt = (df[col] < 0).sum()
        if neg_cnt > 0:
            report.append(f"⚠️ 字段 {col} 存在负数：{neg_cnt} 条")

    report_text = "\n".join(report)
    print(report_text)

    os.makedirs("output", exist_ok=True)
    with open("output/report.txt", "w", encoding="utf-8") as f:
        f.write(report_text)

if __name__ == "__main__":
    run_check("data/test_data.csv")
