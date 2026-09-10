import fs from "node:fs/promises";
import path from "node:path";
import { FileBlob, SpreadsheetFile, Workbook } from "@oai/artifact-tool";


const root = path.resolve(import.meta.dirname, "..");
const outputDir = path.join(root, "outputs");
const previewDir = path.join(root, "work");
const outputPath = path.join(outputDir, "listing-rescue-delivery-template.xlsx");
const previewPath = path.join(previewDir, "listing-rescue-delivery-template-preview.png");

await fs.mkdir(outputDir, { recursive: true });
await fs.mkdir(previewDir, { recursive: true });

const workbook = Workbook.create();
const sheet = workbook.worksheets.add("Delivery");
sheet.showGridLines = false;
sheet.tabColor = "#16324F";

const navy = "#16324F";
const blue = "#D9EAF7";
const paleBlue = "#EEF5FA";
const amber = "#FFF2CC";
const red = "#FCE8E6";
const redText = "#9C0006";
const green = "#E2F0D9";
const greenText = "#006100";
const grey = "#F2F4F7";
const line = "#CBD5E1";
const body = "#17212B";
const fontName = "Arial";

sheet.getRange("A1:L30").format.font = { name: fontName, size: 10, color: body };
sheet.getRange("A1:L30").format.verticalAlignment = "center";

sheet.getRange("A2").values = [["Listing rescue delivery"]];
sheet.getRange("A2").format.font = { name: fontName, size: 16, bold: true, color: navy };
sheet.getRange("A3").values = [["Fifteen-listing copy and QA handoff. Buyer review is required before publishing."]];
sheet.getRange("A3:L3").format = {
  font: { name: fontName, size: 10, italic: true, color: "#475569" },
  borders: { bottom: { style: "thin", color: navy } },
};

sheet.getRange("A5:L6").values = [
  ["Client", "[Enter buyer name]", "", "Service", "£99 listing rescue sprint", "", "Prepared", "[Enter date]", "Delivery due", "[Enter due date]", "Version", 1],
  ["Scope", "15 listings", "", "Revision", "One pass", "", "Access", "No marketplace access", "Publishing", "Buyer approval required", "", ""],
];
sheet.getRange("A5:L6").format.borders = {
  bottom: { style: "thin", color: line },
};
for (const address of ["A5", "D5", "G5", "I5", "K5", "A6", "D6", "G6", "I6"]) {
  sheet.getRange(address).format.font = { name: fontName, size: 10, bold: true, color: navy };
}
for (const address of ["B5:C5", "H5", "J5"]) {
  sheet.getRange(address).format.fill = amber;
}

sheet.getRange("A7:J7").values = [[
  "Complete rows", "", "", "Awaiting approval", "", "", "Approved", "", "Overall status", "",
]];
sheet.getRange("B7").formulas = [["=COUNTIFS(K11:K25,\"<>Missing draft\")"]];
sheet.getRange("E7").formulas = [["=COUNTIFS(K11:K25,\"Awaiting approval\")"]];
sheet.getRange("H7").formulas = [["=COUNTIFS(K11:K25,\"Approved\")"]];
sheet.getRange("J7").formulas = [["=IF(B7<15,\"Draft incomplete\",IF(H7=15,\"Buyer-approved\",IF(COUNTIFS(K11:K25,\"Needs confirmation\")+COUNTIFS(K11:K25,\"Pending fact review\")>0,\"Fact review required\",\"Buyer review in progress\")))"]];
for (const address of ["A7", "D7", "G7", "I7"]) {
  sheet.getRange(address).format = {
    fill: blue,
    font: { name: fontName, size: 10, bold: true, color: navy },
  };
}
for (const address of ["B7", "E7", "H7", "J7"]) {
  sheet.getRange(address).format = {
    fill: paleBlue,
    font: { name: fontName, size: 10, bold: true, color: body },
    horizontalAlignment: "center",
  };
}
sheet.getRange("B7:H7").format.numberFormat = "0";

sheet.getRange("A8").values = [["Use only seller-controlled or buyer-approved facts. Keep uncertainties as visible questions; never infer brand, specification, condition, compatibility or performance."]];
sheet.getRange("A8:L8").format.font = { name: fontName, size: 10, italic: true, color: "#475569" };

const headers = [[
  "No.", "Listing URL", "Current title", "Observed issue", "Facts used and source",
  "Proposed title", "Proposed description", "QA question", "Fact review",
  "Buyer approval", "Row status", "Reviewer notes",
]];
sheet.getRange("A10:L10").values = headers;

const rows = [];
for (let number = 1; number <= 15; number += 1) {
  rows.push([
    number, "", "", "", "", "", "", "", "Pending source review", "Pending", "", "",
  ]);
}
sheet.getRange("A11:L25").values = rows;
sheet.getRange("K11").formulas = [[
  "=IF(OR(B11=\"\",C11=\"\",D11=\"\",E11=\"\",F11=\"\",G11=\"\"),\"Missing draft\",IF(I11=\"Buyer confirmation required\",\"Needs confirmation\",IF(I11<>\"Confirmed from supplied source\",\"Pending fact review\",IF(J11=\"Approved\",\"Approved\",IF(J11=\"Changes requested\",\"Changes requested\",\"Awaiting approval\")))))",
]];
sheet.getRange("K11:K25").fillDown();

sheet.getRange("I11:I25").dataValidation = {
  rule: {
    type: "list",
    values: [
      "Pending source review",
      "Confirmed from supplied source",
      "Buyer confirmation required",
      "Excluded",
    ],
  },
};
sheet.getRange("J11:J25").dataValidation = {
  rule: { type: "list", values: ["Pending", "Approved", "Changes requested"] },
};

const table = sheet.tables.add("A10:L25", true, "ListingsTable");
table.style = "TableStyleMedium2";
table.showBandedRows = true;

sheet.getRange("A10:L10").format = {
  fill: navy,
  font: { name: fontName, size: 10, bold: true, color: "#FFFFFF" },
  horizontalAlignment: "center",
  verticalAlignment: "center",
  wrapText: true,
};
sheet.getRange("A11:L25").format.verticalAlignment = "top";
sheet.getRange("A11:L25").format.wrapText = true;
sheet.getRange("A11:A25").format.horizontalAlignment = "center";
sheet.getRange("I11:K25").format.horizontalAlignment = "center";

sheet.getRange("K11:K25").conditionalFormats.add("containsText", {
  text: "Missing draft",
  format: { fill: red, font: { bold: true, color: redText } },
});
sheet.getRange("K11:K25").conditionalFormats.add("containsText", {
  text: "Needs confirmation",
  format: { fill: amber, font: { bold: true, color: "#7F6000" } },
});
sheet.getRange("K11:K25").conditionalFormats.add("containsText", {
  text: "Changes requested",
  format: { fill: amber, font: { bold: true, color: "#7F6000" } },
});
sheet.getRange("K11:K25").conditionalFormats.add("containsText", {
  text: "Approved",
  format: { fill: green, font: { bold: true, color: greenText } },
});

sheet.getRange("A27").values = [["Fact review definitions"]];
sheet.getRange("A27:L27").format = {
  fill: grey,
  font: { name: fontName, size: 10, bold: true, color: navy },
  borders: { bottom: { style: "thin", color: line } },
};
sheet.getRange("A28:B30").values = [
  ["Source confirmed", "Every product fact is traceable to seller-controlled or buyer-approved data."],
  ["Buyer check", "Keep a visible placeholder or question. Do not publish until the buyer confirms it."],
  ["Excluded", "Leave the row out of the final deliverable and explain the reason in reviewer notes."],
];
sheet.getRange("A28:A30").format.font = { name: fontName, size: 10, bold: true, color: navy };
sheet.getRange("B28:B30").format.wrapText = true;

const widths = {
  A: 13, B: 30, C: 28, D: 26, E: 34, F: 34,
  G: 42, H: 28, I: 25, J: 20, K: 21, L: 28,
};
for (const [column, width] of Object.entries(widths)) {
  sheet.getRange(`${column}:${column}`).format.columnWidth = width;
}
sheet.getRange("2:2").format.rowHeight = 24;
sheet.getRange("3:3").format.rowHeight = 22;
sheet.getRange("5:7").format.rowHeight = 24;
sheet.getRange("8:8").format.rowHeight = 28;
sheet.getRange("10:10").format.rowHeight = 34;
sheet.getRange("11:25").format.rowHeight = 72;
sheet.getRange("27:27").format.rowHeight = 26;
sheet.getRange("28:30").format.rowHeight = 38;

sheet.freezePanes.freezeRows(10);
sheet.freezePanes.freezeColumns(2);

workbook.recalculate();

function assertValue(address, expected, step) {
  const actual = sheet.getRange(address).values[0][0];
  if (actual !== expected) {
    throw new Error(`${step}: expected ${address} to be ${expected}, found ${actual}`);
  }
}

// Exercise the row-state workflow, then restore the reusable blank template.
assertValue("K11", "Missing draft", "initial row guard");
sheet.getRange("B11:G11").values = [[
  "https://example.invalid/item-1",
  "Source title",
  "Observed issue",
  "Buyer-approved source facts",
  "Proposed title",
  "Proposed description",
]];
sheet.getRange("I11:J11").values = [["Buyer confirmation required", "Pending"]];
workbook.recalculate();
assertValue("K11", "Needs confirmation", "fact-confirmation guard");
sheet.getRange("I11:J11").values = [["Confirmed from supplied source", "Approved"]];
workbook.recalculate();
assertValue("K11", "Approved", "buyer-approval guard");
sheet.getRange("B11:G11").values = [["", "", "", "", "", ""]];
sheet.getRange("I11:J11").values = [["Pending source review", "Pending"]];
workbook.recalculate();
assertValue("K11", "Missing draft", "restored template guard");

const inspection = await workbook.inspect({
  kind: "table",
  range: "Delivery!A2:L11",
  include: "values,formulas",
  tableMaxRows: 10,
  tableMaxCols: 12,
  maxChars: 18000,
});
console.log(inspection.ndjson);

const formulaErrors = await workbook.inspect({
  kind: "match",
  searchTerm: "#REF!|#DIV/0!|#VALUE!|#NAME\\?|#N/A|#NUM!|#NULL!|#SPILL!|#CALC!",
  options: { useRegex: true, maxResults: 100 },
  summary: "final formula error scan",
});
console.log(formulaErrors.ndjson);

const preview = await workbook.render({
  sheetName: "Delivery",
  range: "A1:L30",
  scale: 1,
  format: "png",
});
await fs.writeFile(previewPath, new Uint8Array(await preview.arrayBuffer()));

const output = await SpreadsheetFile.exportXlsx(workbook);
await output.save(outputPath);

const reopened = await SpreadsheetFile.importXlsx(await FileBlob.load(outputPath));
reopened.recalculate();
const reopenedSheet = reopened.worksheets.getItem("Delivery");
const reopenedStatus = reopenedSheet.getRange("K11").values[0][0];
if (reopenedStatus !== "Missing draft") {
  throw new Error(`reopened workbook guard: expected K11 to be Missing draft, found ${reopenedStatus}`);
}
const reopenedErrors = await reopened.inspect({
  kind: "match",
  searchTerm: "#REF!|#DIV/0!|#VALUE!|#NAME\\?|#N/A|#NUM!|#NULL!|#SPILL!|#CALC!",
  options: { useRegex: true, maxResults: 100 },
  summary: "reopened workbook formula error scan",
});
console.log(reopenedErrors.ndjson);

await fs.rm(`${outputPath}.inspect.ndjson`, { force: true });

console.log(JSON.stringify({ outputPath, previewPath }));
