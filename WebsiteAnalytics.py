import pandas as pd
import plotly.graph_objects as go
from plotly.subplots import make_subplots
from datetime import datetime, timedelta
import random


class WebsiteAnalytics:
    def __init__(self):
        # 生成示例数据
        self.generate_sample_data()

    def generate_sample_data(self):
        """生成30天的示例数据"""
        end_date = datetime.now()
        dates = [(end_date - timedelta(days=x)).strftime('%Y-%m-%d') for x in range(30)]

        # 生成随机数据
        self.data = pd.DataFrame({
            'date': dates,
            'users': [random.randint(800, 1500) for _ in range(30)],
            'pageviews': [random.randint(2000, 4000) for _ in range(30)],
            'bounce_rate': [random.uniform(20, 40) for _ in range(30)]
        })

        # 按日期排序
        self.data = self.data.sort_values('date')

    def plot_traffic_trends(self):
        """绘制流量趋势图"""
        # 创建子图
        fig = make_subplots(
            rows=2,
            cols=1,
            subplot_titles=('访问量和页面浏览量', '跳出率'),
            vertical_spacing=0.15
        )

        # 添加访问量曲线
        fig.add_trace(
            go.Scatter(
                x=self.data['date'],
                y=self.data['users'],
                name='访问用户数',
                mode='lines+markers',
                line=dict(color='#1f77b4')
            ),
            row=1, col=1
        )

        # 添加页面浏览量曲线
        fig.add_trace(
            go.Scatter(
                x=self.data['date'],
                y=self.data['pageviews'],
                name='页面浏览量',
                mode='lines+markers',
                line=dict(color='#ff7f0e')
            ),
            row=1, col=1
        )

        # 添加跳出率曲线
        fig.add_trace(
            go.Scatter(
                x=self.data['date'],
                y=self.data['bounce_rate'],
                name='跳出率(%)',
                mode='lines+markers',
                line=dict(color='#2ca02c')
            ),
            row=2, col=1
        )

        # 更新布局
        fig.update_layout(
            height=800,
            title_text="网站流量分析",
            showlegend=True,
            template='plotly_white'
        )

        # 更新x轴
        fig.update_xaxes(tickangle=45)

        # 显示图表
        fig.show()

    def create_funnel_chart(self, stages_data=None):
        """创建转化漏斗图"""
        if stages_data is None:
            # 使用示例数据
            stages_data = {
                '访问量': 1000,
                '注册量': 500,
                '活跃用户': 200,
                '付费用户': 50
            }

        fig = go.Figure(go.Funnel(
            y=list(stages_data.keys()),
            x=list(stages_data.values()),
            textinfo="value+percent initial",
            textposition="inside",
            textfont=dict(size=14),
            marker=dict(
                color=['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728']
            )
        ))

        fig.update_layout(
            title_text="用户转化漏斗图",
            showlegend=False,
            template='plotly_white',
            width=800,
            height=500
        )

        fig.show()

    def get_summary_stats(self):
        """获取统计摘要"""
        summary = {
            '平均日访问量': round(self.data['users'].mean(), 2),
            '最高日访问量': self.data['users'].max(),
            '平均页面浏览量': round(self.data['pageviews'].mean(), 2),
            '平均跳出率': f"{round(self.data['bounce_rate'].mean(), 2)}%",
            '数据统计周期': f"{self.data['date'].min()} 至 {self.data['date'].max()}"
        }
        return summary


# 使用示例
if __name__ == "__main__":
    # 创建分析器实例
    analytics = WebsiteAnalytics()

    # 显示统计摘要
    summary = analytics.get_summary_stats()
    print("\n=== 统计摘要 ===")
    for key, value in summary.items():
        print(f"{key}: {value}")

    # 绘制流量趋势图
    analytics.plot_traffic_trends()

    # 绘制转化漏斗图
    analytics.create_funnel_chart()