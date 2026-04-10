#!/usr/bin/env python3
"""
Marketing Report PDF Generator — AI Marketing Claude Code Skills
Generates professional, client-ready PDF marketing reports with charts,
score visualizations, and prioritized action plans.

Requires: reportlab (pip install reportlab)
"""

import sys
import json
import os
from datetime import datetime

try:
    from reportlab.lib.pagesizes import letter
    from reportlab.lib.units import inch
    from reportlab.lib.colors import HexColor, white, black
    from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
    from reportlab.platypus import (SimpleDocTemplate, Paragraph, Spacer, Table,
                                     TableStyle, PageBreak, Image)
    from reportlab.graphics.shapes import Drawing, Rect, Circle, String, Line, Wedge
    from reportlab.graphics.charts.barcharts import VerticalBarChart
    from reportlab.graphics import renderPDF
except ImportError:
    print("Error: reportlab is required. Install with: pip install reportlab")
    sys.exit(1)


# Color palette
COLORS = {
    "primary": HexColor("#1B2A4A"),
    "accent": HexColor("#2D5BFF"),
    "highlight": HexColor("#FF6B35"),
    "success": HexColor("#00C853"),
    "warning": HexColor("#FFB300"),
    "danger": HexColor("#FF1744"),
    "light_bg": HexColor("#F5F7FA"),
    "text": HexColor("#2C3E50"),
    "text_light": HexColor("#7F8C9B"),
    "border": HexColor("#E0E6ED"),
    "white": white,
    "black": black,
}


def score_color(score):
    """Return color based on score value."""
    if score >= 80:
        return COLORS["success"]
    elif score >= 60:
        return COLORS["accent"]
    elif score >= 40:
        return COLORS["warning"]
    else:
        return COLORS["danger"]


def draw_score_gauge(score, x, y, size=80):
    """Create a circular score gauge drawing."""
    d = Drawing(size + 20, size + 30)

    # Background circle
    d.add(Circle(size / 2 + 10, size / 2 + 15, size / 2,
                 fillColor=COLORS["light_bg"], strokeColor=COLORS["border"], strokeWidth=2))

    # Score arc (simplified as colored inner circle)
    color = score_color(score)
    inner_r = size / 2 - 8
    d.add(Circle(size / 2 + 10, size / 2 + 15, inner_r,
                 fillColor=color, strokeColor=None))

    # White center
    d.add(Circle(size / 2 + 10, size / 2 + 15, inner_r - 10,
                 fillColor=COLORS["white"], strokeColor=None))

    # Score text
    d.add(String(size / 2 + 10, size / 2 + 10, str(int(score)),
                 fontSize=20, fillColor=COLORS["primary"],
                 textAnchor="middle", fontName="Helvetica-Bold"))

    return d


def create_bar_chart(categories, scores, width=450, height=180):
    """Create a horizontal bar chart for category scores."""
    d = Drawing(width, height)

    bar_height = 20
    gap = 8
    max_bar_width = width - 180
    start_y = height - 30
    label_x = 5
    bar_x = 160

    for i, (cat, score) in enumerate(zip(categories, scores)):
        y = start_y - i * (bar_height + gap)

        # Category label
        d.add(String(label_x, y + 5, cat[:22],
                     fontSize=9, fillColor=COLORS["text"],
                     textAnchor="start", fontName="Helvetica"))

        # Background bar
        d.add(Rect(bar_x, y, max_bar_width, bar_height,
                   fillColor=COLORS["light_bg"], strokeColor=None))

        # Score bar
        bar_width = (score / 100) * max_bar_width
        color = score_color(score)
        d.add(Rect(bar_x, y, bar_width, bar_height,
                   fillColor=color, strokeColor=None))

        # Score label
        d.add(String(bar_x + max_bar_width + 10, y + 5, f"{int(score)}",
                     fontSize=10, fillColor=COLORS["text"],
                     textAnchor="start", fontName="Helvetica-Bold"))

    return d


def generate_report(data, output_path):
    """Generate a professional marketing PDF report."""
    doc = SimpleDocTemplate(
        output_path,
        pagesize=letter,
        rightMargin=50,
        leftMargin=50,
        topMargin=50,
        bottomMargin=50
    )

    styles = getSampleStyleSheet()

    # Custom styles
    title_style = ParagraphStyle(
        "CustomTitle",
        parent=styles["Title"],
        fontSize=28,
        textColor=COLORS["primary"],
        spaceAfter=6,
        fontName="Helvetica-Bold"
    )

    subtitle_style = ParagraphStyle(
        "CustomSubtitle",
        parent=styles["Normal"],
        fontSize=14,
        textColor=COLORS["text_light"],
        spaceAfter=20,
        fontName="Helvetica"
    )

    heading_style = ParagraphStyle(
        "CustomHeading",
        parent=styles["Heading1"],
        fontSize=18,
        textColor=COLORS["primary"],
        spaceBefore=20,
        spaceAfter=10,
        fontName="Helvetica-Bold"
    )

    subheading_style = ParagraphStyle(
        "CustomSubheading",
        parent=styles["Heading2"],
        fontSize=14,
        textColor=COLORS["accent"],
        spaceBefore=14,
        spaceAfter=8,
        fontName="Helvetica-Bold"
    )

    body_style = ParagraphStyle(
        "CustomBody",
        parent=styles["Normal"],
        fontSize=10,
        textColor=COLORS["text"],
        spaceAfter=6,
        fontName="Helvetica",
        leading=14
    )

    # Build document elements
    elements = []

    # === COVER PAGE ===
    elements.append(Spacer(1, 1.5 * inch))
    elements.append(Paragraph("Marketing Audit Report", title_style))

    url = data.get("url", "example.com")
    date_str = data.get("date", datetime.now().strftime("%B %d, %Y"))
    elements.append(Paragraph(f"{url}", subtitle_style))
    elements.append(Paragraph(f"Generated: {date_str}", subtitle_style))
    elements.append(Spacer(1, 0.5 * inch))

    # Overall score gauge
    overall_score = data.get("overall_score", 0)
    gauge = draw_score_gauge(overall_score, 0, 0, size=100)
    elements.append(gauge)
    elements.append(Spacer(1, 0.3 * inch))

    grade = "A+" if overall_score >= 90 else "A" if overall_score >= 80 else "B" if overall_score >= 70 else "C" if overall_score >= 60 else "D" if overall_score >= 50 else "F"
    elements.append(Paragraph(f"Overall Marketing Score: {int(overall_score)}/100 (Grade: {grade})", heading_style))

    exec_summary = data.get("executive_summary", "This report provides a comprehensive analysis of the website's marketing effectiveness across content, conversion, SEO, competitive positioning, brand trust, and growth strategy.")
    elements.append(Paragraph(exec_summary, body_style))

    elements.append(PageBreak())

    # === SCORE BREAKDOWN ===
    elements.append(Paragraph("Score Breakdown", heading_style))

    categories = data.get("categories", {})
    cat_names = list(categories.keys()) if categories else [
        "Content & Messaging", "Conversion Optimization", "SEO & Discoverability",
        "Competitive Positioning", "Brand & Trust", "Growth & Strategy"
    ]
    cat_scores = [categories.get(c, {}).get("score", 50) for c in cat_names] if categories else [65, 58, 72, 55, 68, 60]

    # Bar chart
    chart = create_bar_chart(cat_names, cat_scores)
    elements.append(chart)
    elements.append(Spacer(1, 0.3 * inch))

    # Score table
    score_data = [["Category", "Score", "Weight", "Status"]]
    weights = ["25%", "20%", "20%", "15%", "10%", "10%"]
    for i, (name, score) in enumerate(zip(cat_names, cat_scores)):
        status = "Strong" if score >= 75 else "Needs Work" if score >= 50 else "Critical"
        weight = weights[i] if i < len(weights) else "—"
        score_data.append([name, f"{int(score)}/100", weight, status])

    score_table = Table(score_data, colWidths=[180, 70, 60, 90])
    score_table.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, 0), COLORS["primary"]),
        ("TEXTCOLOR", (0, 0), (-1, 0), COLORS["white"]),
        ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),
        ("FONTSIZE", (0, 0), (-1, -1), 9),
        ("ALIGN", (1, 0), (-1, -1), "CENTER"),
        ("GRID", (0, 0), (-1, -1), 0.5, COLORS["border"]),
        ("ROWBACKGROUNDS", (0, 1), (-1, -1), [COLORS["white"], COLORS["light_bg"]]),
        ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
        ("TOPPADDING", (0, 0), (-1, -1), 6),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 6),
    ]))
    elements.append(score_table)

    elements.append(PageBreak())

    # === KEY FINDINGS ===
    elements.append(Paragraph("Key Findings", heading_style))

    findings = data.get("findings", [])
    if not findings:
        findings = [
            {"severity": "Critical", "finding": "Homepage headline lacks clarity — visitors can't understand the value proposition in under 5 seconds"},
            {"severity": "High", "finding": "No social proof on homepage — missing testimonials, client logos, and trust badges"},
            {"severity": "High", "finding": "Primary CTA uses generic text ('Get Started') instead of value-driven copy"},
            {"severity": "Medium", "finding": "Missing meta descriptions on key landing pages"},
            {"severity": "Medium", "finding": "No email capture mechanism or lead magnet visible"},
            {"severity": "Low", "finding": "Blog content lacks internal linking to product pages"},
        ]

    findings_data = [["Severity", "Finding"]]
    for f in findings:
        severity = f.get("severity", "Medium")
        finding = f.get("finding", "")
        findings_data.append([severity, Paragraph(finding, body_style)])

    findings_table = Table(findings_data, colWidths=[70, 400])
    severity_colors = {
        "Critical": COLORS["danger"],
        "High": COLORS["highlight"],
        "Medium": COLORS["warning"],
        "Low": COLORS["accent"]
    }
    table_style_cmds = [
        ("BACKGROUND", (0, 0), (-1, 0), COLORS["primary"]),
        ("TEXTCOLOR", (0, 0), (-1, 0), COLORS["white"]),
        ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),
        ("FONTSIZE", (0, 0), (-1, -1), 9),
        ("GRID", (0, 0), (-1, -1), 0.5, COLORS["border"]),
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("TOPPADDING", (0, 0), (-1, -1), 6),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 6),
        ("ALIGN", (0, 0), (0, -1), "CENTER"),
    ]
    for i, f in enumerate(findings, 1):
        color = severity_colors.get(f.get("severity", "Medium"), COLORS["warning"])
        table_style_cmds.append(("TEXTCOLOR", (0, i), (0, i), color))
        table_style_cmds.append(("FONTNAME", (0, i), (0, i), "Helvetica-Bold"))

    findings_table.setStyle(TableStyle(table_style_cmds))
    elements.append(findings_table)

    elements.append(PageBreak())

    # === ACTION PLAN ===
    elements.append(Paragraph("Prioritized Action Plan", heading_style))

    # Quick Wins
    elements.append(Paragraph("Quick Wins (This Week)", subheading_style))
    quick_wins = data.get("quick_wins", [
        "Rewrite homepage headline to be specific and benefit-driven",
        "Add 3-5 client logos or trust badges above the fold",
        "Change primary CTA to value-driven text (e.g., 'Start Free Trial — No Credit Card')",
        "Add meta descriptions to top 5 landing pages",
    ])
    for i, win in enumerate(quick_wins, 1):
        elements.append(Paragraph(f"{i}. {win}", body_style))

    elements.append(Spacer(1, 0.2 * inch))

    # Medium-Term
    elements.append(Paragraph("Medium-Term (1-3 Months)", subheading_style))
    medium_term = data.get("medium_term", [
        "Build email capture funnel with lead magnet",
        "Create comparison pages for top 3 competitors",
        "Develop 3 case studies with measurable results",
        "Implement blog content strategy targeting high-intent keywords",
    ])
    for i, action in enumerate(medium_term, 1):
        elements.append(Paragraph(f"{i}. {action}", body_style))

    elements.append(Spacer(1, 0.2 * inch))

    # Strategic
    elements.append(Paragraph("Strategic (3-6 Months)", subheading_style))
    strategic = data.get("strategic", [
        "Launch referral program with incentive structure",
        "Build content authority hub with pillar content",
        "Implement full-funnel retargeting campaign",
        "Develop pricing optimization based on value metrics",
    ])
    for i, action in enumerate(strategic, 1):
        elements.append(Paragraph(f"{i}. {action}", body_style))

    elements.append(PageBreak())

    # === COMPETITOR SNAPSHOT ===
    if data.get("competitors"):
        elements.append(Paragraph("Competitive Landscape", heading_style))

        comp_data = [["", data.get("brand_name", "Target")] + [c.get("name", f"Competitor {i+1}") for i, c in enumerate(data["competitors"][:3])]]
        comp_rows = ["Positioning", "Pricing", "Social Proof", "Content"]

        for row_name in comp_rows:
            row = [row_name, data.get("brand_name", "Target")]
            for comp in data["competitors"][:3]:
                row.append(comp.get(row_name.lower().replace(" ", "_"), "—"))
            # Ensure consistent columns
            while len(row) < len(comp_data[0]):
                row.append("—")
            comp_data.append(row)

        col_count = len(comp_data[0])
        col_width = 470 / col_count
        comp_table = Table(comp_data, colWidths=[col_width] * col_count)
        comp_table.setStyle(TableStyle([
            ("BACKGROUND", (0, 0), (-1, 0), COLORS["primary"]),
            ("TEXTCOLOR", (0, 0), (-1, 0), COLORS["white"]),
            ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),
            ("FONTSIZE", (0, 0), (-1, -1), 8),
            ("GRID", (0, 0), (-1, -1), 0.5, COLORS["border"]),
            ("ROWBACKGROUNDS", (0, 1), (-1, -1), [COLORS["white"], COLORS["light_bg"]]),
            ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
            ("TOPPADDING", (0, 0), (-1, -1), 5),
            ("BOTTOMPADDING", (0, 0), (-1, -1), 5),
            ("FONTNAME", (0, 1), (0, -1), "Helvetica-Bold"),
        ]))
        elements.append(comp_table)
        elements.append(PageBreak())

    # === METHODOLOGY ===
    elements.append(Paragraph("Methodology", heading_style))
    elements.append(Paragraph(
        "This audit evaluates six key dimensions of marketing effectiveness. "
        "Each category is scored 0-100 based on industry best practices and competitive benchmarks.",
        body_style
    ))

    method_data = [
        ["Category", "Weight", "What We Measure"],
        ["Content & Messaging", "25%", "Copy quality, value proposition clarity, CTA effectiveness"],
        ["Conversion Optimization", "20%", "Funnel design, forms, social proof, friction reduction"],
        ["SEO & Discoverability", "20%", "On-page SEO, technical SEO, content structure"],
        ["Competitive Positioning", "15%", "Market differentiation, pricing, alternatives strategy"],
        ["Brand & Trust", "10%", "Design quality, trust signals, authority indicators"],
        ["Growth & Strategy", "10%", "Pricing strategy, acquisition channels, retention"],
    ]

    method_table = Table(method_data, colWidths=[140, 50, 280])
    method_table.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, 0), COLORS["primary"]),
        ("TEXTCOLOR", (0, 0), (-1, 0), COLORS["white"]),
        ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),
        ("FONTSIZE", (0, 0), (-1, -1), 9),
        ("GRID", (0, 0), (-1, -1), 0.5, COLORS["border"]),
        ("ROWBACKGROUNDS", (0, 1), (-1, -1), [COLORS["white"], COLORS["light_bg"]]),
        ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
        ("TOPPADDING", (0, 0), (-1, -1), 5),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 5),
    ]))
    elements.append(method_table)

    elements.append(Spacer(1, 0.5 * inch))
    elements.append(Paragraph(
        "Generated by AI Marketing Suite for Claude Code",
        ParagraphStyle("Footer", parent=body_style, fontSize=8, textColor=COLORS["text_light"])
    ))

    # Build PDF
    doc.build(elements)
    return output_path


def main():
    if len(sys.argv) < 2:
        # Demo mode — generate sample report
        sample_data = {
            "url": "https://example.com",
            "date": datetime.now().strftime("%B %d, %Y"),
            "overall_score": 62,
            "executive_summary": "This marketing audit reveals several high-impact opportunities to improve conversion rates and strengthen competitive positioning. The website has solid content foundations but is underperforming in conversion optimization and competitive awareness.",
            "categories": {
                "Content & Messaging": {"score": 68, "weight": "25%"},
                "Conversion Optimization": {"score": 52, "weight": "20%"},
                "SEO & Discoverability": {"score": 74, "weight": "20%"},
                "Competitive Positioning": {"score": 48, "weight": "15%"},
                "Brand & Trust": {"score": 70, "weight": "10%"},
                "Growth & Strategy": {"score": 55, "weight": "10%"},
            },
            "findings": [
                {"severity": "Critical", "finding": "Homepage headline is generic — doesn't communicate specific value to target audience"},
                {"severity": "Critical", "finding": "No social proof visible above the fold on the homepage"},
                {"severity": "High", "finding": "Primary CTA button says 'Submit' — should use value-driven text"},
                {"severity": "High", "finding": "Pricing page lacks comparison features and doesn't address objections"},
                {"severity": "Medium", "finding": "Missing competitor comparison pages — losing high-intent search traffic"},
                {"severity": "Medium", "finding": "Blog posts have no internal links to product pages"},
                {"severity": "Low", "finding": "Social media links in footer but no social proof integration"},
            ],
            "quick_wins": [
                "Rewrite homepage headline: 'We help businesses grow' → 'Get 3x more qualified leads in 30 days — without cold calling'",
                "Add 5 client logos above the fold with 'Trusted by 500+ companies' text",
                "Change form button from 'Submit' to 'Get My Free Marketing Audit'",
                "Add testimonial section with name, photo, company, and specific results",
            ],
            "medium_term": [
                "Build '[Competitor] Alternative' landing pages for top 3 competitors",
                "Create 3 video case studies showing measurable client results",
                "Implement exit-intent popup with lead magnet offer",
                "Launch email nurture sequence for leads who don't convert immediately",
            ],
            "strategic": [
                "Develop content authority hub with 10 pillar pages targeting high-volume keywords",
                "Build referral program with double-sided incentives",
                "Launch retargeting campaigns across Meta and Google with funnel-based messaging",
                "Create free tool or assessment to capture leads at top of funnel",
            ],
            "competitors": [
                {"name": "Comp A", "positioning": "All-in-one platform", "pricing": "$49-199/mo", "social_proof": "10K+ users", "content": "Active blog"},
                {"name": "Comp B", "positioning": "Enterprise focus", "pricing": "Custom", "social_proof": "Fortune 500 logos", "content": "Whitepapers"},
                {"name": "Comp C", "positioning": "Budget-friendly", "pricing": "Free-$29/mo", "social_proof": "4.8★ G2", "content": "YouTube channel"},
            ],
            "brand_name": "Example Co"
        }

        output = "MARKETING-REPORT-sample.pdf"
        generate_report(sample_data, output)
        print(f"Sample report generated: {output}")
        return

    # JSON input mode
    input_file = sys.argv[1]
    output_file = sys.argv[2] if len(sys.argv) > 2 else "MARKETING-REPORT.pdf"

    with open(input_file, "r") as f:
        data = json.load(f)

    generate_report(data, output_file)
    print(f"Report generated: {output_file}")


if __name__ == "__main__":
    main()
