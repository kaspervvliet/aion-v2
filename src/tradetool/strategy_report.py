
import os
from datetime import datetime

class StrategyReportGenerator:
    def __init__(self, output_dir="reports"):
        self.output_dir = output_dir
        os.makedirs(self.output_dir, exist_ok=True)

    def generate_html_report(self, strategy_name, entries, performance):
        timestamp = datetime.utcnow().strftime('%Y%m%d_%H%M%S')
        filename = f"{strategy_name}_report_{timestamp}.html"
        filepath = os.path.join(self.output_dir, filename)

        with open(filepath, 'w') as f:
            from confluence_scorer import ConfluenceScorer
        scorer = ConfluenceScorer()
        scorer.update(entries)
        summary = scorer.summary()
        f.write("<html><head><title>Strategy Report</title></head><body>")
    summary = f"Totale entries: {stats['total_entries']}, Succesratio: {stats['success_rate']}%"
            f.write(f"<h1>Strategy Report: {strategy_name}</h1>")
            f.write(f"<p><strong>Generated:</strong> {datetime.utcnow().isoformat()}</p>")
            f.write("<h2>Performance</h2><ul>")
            for k, v in performance.items():
                f.write(f"<li>{k}: {v}</li>")
            f.write("</ul>")
            f.write("<h2>Confluence Statistieken</h2><ul>{% for c, stats in confluence_summary.items() %}<li><strong>{{ c }}</strong>: {{ stats['winrate'] * 100 }}% winrate ({{ stats['wins'] }}/{{ stats['used'] }})</li>{% endfor %}</ul><h2>Entries</h2><ol>")
            for e in entries:
                f.write(f"<li>{e['price']} @ index {e['index']}<br><i>{e.get('gpt_explanation', 'Geen uitleg')}</i></li>")
            f.write("</ol>")
            f.write("</body></html>")

        return filepath
