# Project Daily Reports

## ⭐ Overview

This project tracks daily work progress through structured reports submitted by all team members.
Push Your Project Daily in Project-report

## ⭐ Reporting Schedule

### 📅 Working Days
Employees are required to push daily reports:
- **Monday to Friday** - Mandatory daily reports
- **Saturday** - No reports required (Weekend)
- **Sunday** - No reports required (Weekend)

### ⏰ Submission Timeline
- **Deadline**: End of each working day
- **Format**: Use the template from `templates/daily-template.md`
- **Location**: `/reports/YYYY-MM-DD/yourname.md`

## ⭐ Weekly Schedule Example

| Day | Report Required | Action |
|-----|----------------|--------|
| Monday | ✅ Yes | Submit daily report |
| Tuesday | ✅ Yes | Submit daily report |
| Wednesday | ✅ Yes | Submit daily report |
| Thursday | ✅ Yes | Submit daily report |
| Friday | ✅ Yes | Submit daily report |
| Saturday | ❌ No | Weekend - No report |
| Sunday | ❌ No | Weekend - No report |

## ⭐ Project Guidelines

### Daily Report Requirements
- **Tasks Completed**: List all finished tasks
- **Pending Work**: Upcoming tasks and priorities
- **Issues/Blockers**: Any obstacles or challenges
- **Time Tracking**: Hours spent on different activities

### Git Workflow for Weekdays
```bash
# Daily routine (Monday-Friday)
git pull origin main
mkdir -p reports/$(date +%Y-%m-%d)
cp templates/daily-template.md reports/$(date +%Y-%m-%d)/yourname.md

# Edit your report
# Then commit and push
git add .
git commit -m "YourName - Daily Report $(date +%Y-%m-%d)"
git push origin main
```

## ⭐ Holiday Policy

- **Public Holidays**: No reports required
- **Vacation Days**: Inform team lead, no reports needed
- **Sick Leave**: No reports required

## ⭐ Compliance

- Missing reports on working days require explanation
- Consistent reporting helps track project progress
- Weekly summaries generated automatically from daily reports