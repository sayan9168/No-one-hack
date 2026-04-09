import datetime

class ReportGenerator:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.created_at = datetime.datetime.utcnow()

    def generate_report(self):
        report = f"Report Title: {self.title}\n"
        report += f"Author: {self.author}\n"
        report += f"Created At: {self.created_at.strftime('%Y-%m-%d %H:%M:%S')} UTC\n"
        return report

    def save_report(self, filename):
        with open(filename, 'w') as file:
            file.write(self.generate_report())

# Example usage:
# generator = ReportGenerator("Monthly Report", "sayan9168")
# generator.save_report("monthly_report.txt")
