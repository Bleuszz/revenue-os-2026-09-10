"""Build the unsent Howleys cross-channel QA capability snapshot."""

from __future__ import annotations

import argparse
from pathlib import Path

from reportlab.lib.colors import HexColor, white
from reportlab.lib.pagesizes import A4
from reportlab.pdfbase.pdfmetrics import stringWidth
from reportlab.pdfgen import canvas


PAGE_WIDTH, PAGE_HEIGHT = A4
MARGIN = 42
NAVY = HexColor("#13283F")
TEAL = HexColor("#13A89E")
INK = HexColor("#182534")
MUTED = HexColor("#5E6B78")
PAPER = HexColor("#F4F7F9")
LINE = HexColor("#D9E1E7")
PALE_TEAL = HexColor("#E7F7F5")
PALE_AMBER = HexColor("#FFF4D8")
AMBER = HexColor("#A96C00")


def wrap_lines(text: str, font: str, size: float, max_width: float) -> list[str]:
    words = text.split()
    if not words:
        return [""]
    lines: list[str] = []
    current = words[0]
    for word in words[1:]:
        candidate = f"{current} {word}"
        if stringWidth(candidate, font, size) <= max_width:
            current = candidate
        else:
            lines.append(current)
            current = word
    lines.append(current)
    return lines


def draw_wrapped(
    page: canvas.Canvas,
    text: str,
    x: float,
    y: float,
    width: float,
    *,
    font: str = "Helvetica",
    size: float = 9,
    leading: float = 12,
    color=INK,
) -> float:
    page.setFont(font, size)
    page.setFillColor(color)
    for line in wrap_lines(text, font, size, width):
        page.drawString(x, y, line)
        y -= leading
    return y


def rounded_box(
    page: canvas.Canvas,
    x: float,
    y: float,
    width: float,
    height: float,
    *,
    fill,
    stroke=LINE,
    radius: float = 8,
) -> None:
    page.setFillColor(fill)
    page.setStrokeColor(stroke)
    page.roundRect(x, y, width, height, radius, fill=1, stroke=1)


def draw_label(page: canvas.Canvas, text: str, x: float, y: float, color=TEAL) -> None:
    page.setFillColor(color)
    page.setFont("Helvetica-Bold", 7.5)
    page.drawString(x, y, text.upper())


def build(output_path: Path) -> None:
    output_path.parent.mkdir(parents=True, exist_ok=True)
    page = canvas.Canvas(str(output_path), pagesize=A4)
    page.setTitle("Howleys cross-channel catalogue QA snapshot")
    page.setAuthor("Nathan Blagden")
    page.setSubject("Unsent public-evidence capability sample")

    page.setFillColor(NAVY)
    page.rect(0, PAGE_HEIGHT - 108, PAGE_WIDTH, 108, fill=1, stroke=0)
    page.setFillColor(TEAL)
    page.rect(0, PAGE_HEIGHT - 108, 7, 108, fill=1, stroke=0)

    page.setFillColor(PALE_TEAL)
    page.roundRect(MARGIN, PAGE_HEIGHT - 39, 153, 18, 9, fill=1, stroke=0)
    page.setFillColor(NAVY)
    page.setFont("Helvetica-Bold", 7.3)
    page.drawCentredString(MARGIN + 76.5, PAGE_HEIGHT - 33.5, "UNSENT CAPABILITY SAMPLE")

    page.setFillColor(white)
    page.setFont("Helvetica-Bold", 22)
    page.drawString(MARGIN, PAGE_HEIGHT - 68, "Howleys: cross-channel catalogue QA")
    page.setFont("Helvetica", 9)
    page.setFillColor(HexColor("#D4E0EA"))
    page.drawString(
        MARGIN,
        PAGE_HEIGHT - 89,
        "Prepared 10 Sep 2026 | Public sources only | Human factual review required",
    )

    intro_y = PAGE_HEIGHT - 132
    intro_y = draw_wrapped(
        page,
        "Two current examples show how a structured QA pass separates safe corrections "
        "from product facts that must be confirmed. No store access or publishing is required.",
        MARGIN,
        intro_y,
        PAGE_WIDTH - 2 * MARGIN,
        size=9.4,
        leading=13,
        color=MUTED,
    )

    card_x = MARGIN
    card_width = PAGE_WIDTH - 2 * MARGIN

    card1_y = 454
    card1_h = 204
    rounded_box(page, card_x, card1_y, card_width, card1_h, fill=white)
    draw_label(page, "Finding 01 | cross-channel title mismatch", card_x + 16, card1_y + card1_h - 20)
    page.setFillColor(INK)
    page.setFont("Helvetica-Bold", 13)
    page.drawString(card_x + 16, card1_y + card1_h - 43, "One spelling issue appears on two active storefronts")

    chip_y = card1_y + card1_h - 70
    for chip_x, chip_w, text in (
        (card_x + 16, 122, "HOWLEYS OWN STORE"),
        (card_x + 146, 113, "ONBUY OFFER"),
        (card_x + 267, 204, "EAN 5015934890479 | MPN 99-0198"),
    ):
        page.setFillColor(PAPER)
        page.roundRect(chip_x, chip_y, chip_w, 19, 9.5, fill=1, stroke=0)
        page.setFillColor(MUTED)
        page.setFont("Helvetica-Bold", 6.7)
        page.drawCentredString(chip_x + chip_w / 2, chip_y + 6.2, text)

    draw_label(page, "Current title", card_x + 16, card1_y + 103, color=AMBER)
    page.setFillColor(PALE_AMBER)
    page.roundRect(card_x + 16, card1_y + 68, card_width - 32, 27, 5, fill=1, stroke=0)
    page.setFillColor(INK)
    page.setFont("Helvetica-Bold", 10.4)
    page.drawString(card_x + 27, card1_y + 77, "Barbie Reuseable Bag For Life Shopping Bag")

    draw_label(page, "Safe proposed correction", card_x + 16, card1_y + 51)
    page.setFillColor(PALE_TEAL)
    page.roundRect(card_x + 16, card1_y + 16, card_width - 32, 27, 5, fill=1, stroke=0)
    page.setFillColor(INK)
    page.setFont("Helvetica-Bold", 10.4)
    page.drawString(card_x + 27, card1_y + 25, "Barbie Reusable Bag for Life Shopping Bag")

    note_y = card1_y - 14
    page.setFillColor(PAPER)
    page.roundRect(card_x, note_y - 37, card_width, 38, 7, fill=1, stroke=0)
    draw_label(page, "Inference boundary", card_x + 14, note_y - 13, color=AMBER)
    draw_wrapped(
        page,
        "Matching identifiers suggest a shared source field may propagate the typo. "
        "That is an inference, not proof; confirm the source of truth and active feeds.",
        card_x + 120,
        note_y - 13,
        card_width - 135,
        size=8.1,
        leading=10.5,
        color=MUTED,
    )

    card2_y = 237
    card2_h = 151
    rounded_box(page, card_x, card2_y, card_width, card2_h, fill=white)
    draw_label(page, "Finding 02 | incomplete live title", card_x + 16, card2_y + card2_h - 20)
    page.setFillColor(INK)
    page.setFont("Helvetica-Bold", 12)
    page.drawString(card_x + 16, card2_y + card2_h - 43, "SwimWays Spring Float SunSeat Pool Lounge Chair for")
    page.setFillColor(MUTED)
    page.setFont("Helvetica", 8.3)
    page.drawString(card_x + 16, card2_y + card2_h - 61, "eBay item 366547022465 | observed: 24 sold, 3 available | revised 10 Sep 2026")

    page.setFillColor(PALE_AMBER)
    page.roundRect(card_x + 16, card2_y + 17, card_width - 32, 55, 6, fill=1, stroke=0)
    draw_label(page, "Review action", card_x + 28, card2_y + 53, color=AMBER)
    draw_wrapped(
        page,
        "Flag the incomplete ending and hold the rewrite. Ask what should follow 'for' "
        "instead of borrowing a qualifier from a similar third-party listing.",
        card_x + 28,
        card2_y + 38,
        card_width - 56,
        size=8.6,
        leading=11,
        color=INK,
    )

    offer_y = 107
    offer_h = 112
    rounded_box(page, card_x, offer_y, card_width, offer_h, fill=NAVY, stroke=NAVY)
    page.setFillColor(TEAL)
    page.setFont("Helvetica-Bold", 8)
    page.drawString(card_x + 16, offer_y + offer_h - 21, "FIXED-SCOPE LISTING RESCUE")
    page.setFillColor(white)
    page.setFont("Helvetica-Bold", 18)
    page.drawString(card_x + 16, offer_y + offer_h - 48, "15 listings | 24 hours | GBP 99")
    bullets = [
        "Structured source / current title / proposed title / QA-flag CSV",
        "Catalogue-level patterns plus one factual or copy revision",
        "No credentials, automatic publishing, or unsupported product claims",
    ]
    bullet_y = offer_y + 43
    page.setFont("Helvetica", 8.2)
    for bullet in bullets:
        page.setFillColor(TEAL)
        page.circle(card_x + 20, bullet_y + 2, 1.6, fill=1, stroke=0)
        page.setFillColor(HexColor("#D7E2EC"))
        page.drawString(card_x + 29, bullet_y, bullet)
        bullet_y -= 15

    page.setStrokeColor(LINE)
    page.line(MARGIN, 87, PAGE_WIDTH - MARGIN, 87)
    draw_label(page, "Public source references", MARGIN, 74, color=MUTED)
    sources = (
        "[1] howleys.co.uk/barbie-reuseable-bag-for-life-shopping-bag/   "
        "[2] onbuy.com/gb/p/...~p134694065/   [3] ebay.co.uk/itm/366547022465"
    )
    draw_wrapped(
        page,
        sources,
        MARGIN,
        61,
        PAGE_WIDTH - 2 * MARGIN,
        size=7.2,
        leading=9,
        color=MUTED,
    )
    page.setFillColor(MUTED)
    page.setFont("Helvetica", 7.2)
    page.drawString(MARGIN, 27, "Nathan Blagden | Review-only sample | Revalidate sources before sending")
    page.drawRightString(PAGE_WIDTH - MARGIN, 27, "Page 1 of 1")

    page.showPage()
    page.save()


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "output",
        nargs="?",
        type=Path,
        default=Path("outputs/howleys-cross-channel-qa-snapshot.pdf"),
    )
    return parser.parse_args()


if __name__ == "__main__":
    build(parse_args().output)
