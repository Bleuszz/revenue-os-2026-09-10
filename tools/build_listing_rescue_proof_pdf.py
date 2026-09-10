"""Build the one-page, claim-safe listing-rescue proof sheet."""

from __future__ import annotations

from pathlib import Path

from reportlab.lib.colors import HexColor, white
from reportlab.lib.pagesizes import A4
from reportlab.pdfbase.pdfmetrics import registerFont, stringWidth
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfgen import canvas


NAVY = HexColor("#101827")
INK = HexColor("#172033")
MUTED = HexColor("#5A6578")
GREEN = HexColor("#37D996")
PALE_GREEN = HexColor("#EAFBF4")
PALE_BLUE = HexColor("#EEF4FF")
LINE = HexColor("#DDE4EE")
PAPER = HexColor("#F7F9FC")
REGULAR_FONT = "ProofSheetRegular"
BOLD_FONT = "ProofSheetBold"

registerFont(TTFont(REGULAR_FONT, "C:/Windows/Fonts/arial.ttf"))
registerFont(TTFont(BOLD_FONT, "C:/Windows/Fonts/arialbd.ttf"))


def _wrap(text: str, font: str, size: float, width: float) -> list[str]:
    words = text.split()
    lines: list[str] = []
    current = ""
    for word in words:
        trial = f"{current} {word}".strip()
        if stringWidth(trial, font, size) <= width:
            current = trial
        else:
            if current:
                lines.append(current)
            current = word
    if current:
        lines.append(current)
    return lines


def _draw_wrapped(
    pdf: canvas.Canvas,
    text: str,
    x: float,
    y: float,
    width: float,
    *,
    font: str = REGULAR_FONT,
    size: float = 9,
    leading: float = 12,
    colour=INK,
) -> float:
    pdf.setFont(font, size)
    pdf.setFillColor(colour)
    for line in _wrap(text, font, size, width):
        pdf.drawString(x, y, line)
        y -= leading
    return y


def _label(pdf: canvas.Canvas, text: str, x: float, y: float, colour=GREEN) -> None:
    pdf.setFillColor(colour)
    pdf.setFont(BOLD_FONT, 8)
    pdf.drawString(x, y, text.upper())


def build_pdf(output: Path) -> None:
    output.parent.mkdir(parents=True, exist_ok=True)
    pdf = canvas.Canvas(str(output), pagesize=A4, pageCompression=1, invariant=1)
    width, height = A4
    pdf.setTitle("Listing Rescue - 15 reviewed fixes in 24 hours")
    pdf.setAuthor("Nathan Blagden")
    pdf.setSubject("Illustrative e-commerce listing rescue proof sheet")

    pdf.setFillColor(PAPER)
    pdf.rect(0, 0, width, height, fill=1, stroke=0)
    pdf.setFillColor(NAVY)
    pdf.rect(0, height - 198, width, 198, fill=1, stroke=0)

    pdf.setFillColor(GREEN)
    pdf.roundRect(42, height - 61, 139, 22, 11, fill=1, stroke=0)
    pdf.setFillColor(NAVY)
    pdf.setFont(BOLD_FONT, 8)
    pdf.drawCentredString(111.5, height - 53.5, "FIXED-SCOPE PILOT")

    pdf.setFillColor(white)
    pdf.setFont(BOLD_FONT, 28)
    pdf.drawString(42, height - 102, "15 listing fixes. 24 hours. £99.")
    _draw_wrapped(
        pdf,
        "A careful, reviewed catalogue rescue for UK marketplace sellers - delivered without account access.",
        42,
        height - 130,
        500,
        font=REGULAR_FONT,
        size=11,
        leading=15,
        colour=HexColor("#CFD7E6"),
    )
    pdf.setFont(BOLD_FONT, 9)
    pdf.setFillColor(GREEN)
    pdf.drawString(42, height - 177, "Free 1-3 listing preview before you decide")

    top = height - 226
    left_x = 42
    right_x = 308
    card_width = 245

    _label(pdf, "What you receive", left_x, top)
    y = top - 22
    benefits = [
        "15 source-grounded title improvements",
        "Description improvements ready to paste",
        "Catalogue QA flags and buyer questions",
        "One revision and a structured Excel handoff",
    ]
    for benefit in benefits:
        pdf.setFillColor(GREEN)
        pdf.circle(left_x + 4, y + 3, 3, fill=1, stroke=0)
        y = _draw_wrapped(pdf, benefit, left_x + 15, y, 220, size=9.5, leading=13)
        y -= 7

    _label(pdf, "Simple process", right_x, top)
    y = top - 22
    process = [
        ("1", "Send 1-3 listing URLs or an approved source sheet."),
        ("2", "Review the free first-pass preview and factual questions."),
        ("3", "Approve the £99 sprint; receive all 15 within 24 hours."),
    ]
    for number, step in process:
        pdf.setFillColor(NAVY)
        pdf.circle(right_x + 10, y + 1, 10, fill=1, stroke=0)
        pdf.setFillColor(white)
        pdf.setFont(BOLD_FONT, 8)
        pdf.drawCentredString(right_x + 10, y - 2, number)
        y = _draw_wrapped(pdf, step, right_x + 28, y + 4, 200, size=9.2, leading=12)
        y -= 11

    example_top = height - 390
    pdf.setFillColor(white)
    pdf.setStrokeColor(LINE)
    pdf.setLineWidth(0.8)
    pdf.roundRect(42, example_top - 235, 511, 235, 12, fill=1, stroke=1)

    _label(pdf, "Illustrative QA example", 62, example_top - 27, NAVY)
    pdf.setFillColor(PALE_BLUE)
    pdf.roundRect(405, example_top - 37, 128, 20, 10, fill=1, stroke=0)
    pdf.setFillColor(MUTED)
    pdf.setFont(BOLD_FONT, 7.5)
    pdf.drawCentredString(469, example_top - 30, "FICTIONAL - NO RESULT CLAIM")

    y = example_top - 59
    _label(pdf, "Source title", 62, y, MUTED)
    y = _draw_wrapped(pdf, "BLUE ME DRESS 10", 62, y - 17, 470, font=BOLD_FONT, size=11, leading=14)

    y -= 8
    _label(pdf, "Buyer-approved facts", 62, y, MUTED)
    y = _draw_wrapped(
        pdf,
        "Brand: Example & Co | Department: Women | Type: Mini dress | Colour: Blue | Size: UK 10",
        62,
        y - 17,
        470,
        size=9.2,
        leading=13,
    )

    y -= 8
    _label(pdf, "Proposed title", 62, y, MUTED)
    pdf.setFillColor(PALE_GREEN)
    pdf.roundRect(62, y - 43, 470, 31, 7, fill=1, stroke=0)
    pdf.setFillColor(INK)
    pdf.setFont(BOLD_FONT, 10.5)
    pdf.drawString(74, y - 32, "Example & Co Blue Women's Mini Dress - UK 10")

    y -= 63
    _label(pdf, "QA question before publication", 62, y, MUTED)
    _draw_wrapped(
        pdf,
        "Please confirm that 'ME' in the source was not a model name and that the supplied brand is authorised for the title.",
        62,
        y - 17,
        470,
        size=9.2,
        leading=13,
    )

    boundary_top = height - 650
    pdf.setFillColor(NAVY)
    pdf.roundRect(42, boundary_top - 86, 511, 86, 12, fill=1, stroke=0)
    _label(pdf, "Factual boundary", 62, boundary_top - 23)
    _draw_wrapped(
        pdf,
        "No invented brands, specifications, compatibility, condition or performance claims. Ambiguous source text becomes a visible buyer question. Nothing is published and no marketplace login is requested.",
        62,
        boundary_top - 43,
        470,
        size=9.2,
        leading=13,
        colour=white,
    )

    cta_y = 73
    pdf.setFillColor(INK)
    pdf.setFont(BOLD_FONT, 12)
    pdf.drawString(42, cta_y, "Interested? Reply to Nathan's email with 1-3 listing URLs.")
    pdf.setFillColor(MUTED)
    pdf.setFont(REGULAR_FONT, 8.5)
    pdf.drawString(42, 52, "Nathan Blagden | E-commerce listing rescue | Prepared 10 September 2026")
    pdf.setStrokeColor(LINE)
    pdf.line(42, 41, 553, 41)
    pdf.setFont(REGULAR_FONT, 7.5)
    pdf.drawRightString(553, 25, "Illustrative capability proof - not client work or a performance claim")

    pdf.showPage()
    pdf.save()


def main() -> int:
    root = Path(__file__).resolve().parents[1]
    output = root / "outputs" / "listing-rescue-proof-sheet.pdf"
    build_pdf(output)
    print(f"Created {output}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
