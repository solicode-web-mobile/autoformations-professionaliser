const fs = require('fs');
const path = require('path');

const BASE_DIR = "d:\\solicode-web-mobile\\autoformations-professionaliser";

function writeUtf8NoBom(filePath, content) {
  const dir = path.dirname(filePath);
  if (!fs.existsSync(dir)) {
    fs.mkdirSync(dir, { recursive: true });
  }
  fs.writeFileSync(filePath, content.trim() + "\n", { encoding: 'utf8' });
  console.log("Written: " + filePath);
}

// Read the python file to extract variables, or define them directly
const pyContent = fs.readFileSync(path.join(BASE_DIR, 'scratch', 'generate_milestones.py'), 'utf8');

// Simple extractor for the variables in pyContent
function extractVar(varName) {
  const marker = varName + ' = """';
  const start = pyContent.indexOf(marker);
  if (start === -1) throw new Error("Could not find " + varName);
  const contentStart = start + marker.length;
  const end = pyContent.indexOf('"""', contentStart);
  if (end === -1) throw new Error("Could not find end of " + varName);
  return pyContent.substring(contentStart, end);
}

const files = [
  // Milestone 2
  [path.join(BASE_DIR, "_tutos", "D.351.1.scrum", "UA.351.11", "T.351.112", "vision-besoins.md"), extractVar("TUTO_2_MD")],
  [path.join(BASE_DIR, "ua-lab", "scrum", "initiation-scrum", "vision-besoins", "vision-besoins.md"), extractVar("LAB_2_MD")],
  [path.join(BASE_DIR, "ua-lab", "scrum", "initiation-scrum", "vision-besoins", "presentation-vision-besoins.md"), extractVar("PRES_2_MD")],
  [path.join(BASE_DIR, "ua-lab", "scrum", "initiation-scrum", "vision-besoins", "version.yml"), extractVar("VERSION_2_YML")],

  // Milestone 3
  [path.join(BASE_DIR, "_tutos", "D.351.1.scrum", "UA.351.11", "T.351.113", "product-backlog.md"), extractVar("TUTO_3_MD")],
  [path.join(BASE_DIR, "ua-lab", "scrum", "initiation-scrum", "product-backlog", "product-backlog.md"), extractVar("LAB_3_MD")],
  [path.join(BASE_DIR, "ua-lab", "scrum", "initiation-scrum", "product-backlog", "presentation-product-backlog.md"), extractVar("PRES_3_MD")],
  [path.join(BASE_DIR, "ua-lab", "scrum", "initiation-scrum", "product-backlog", "version.yml"), extractVar("VERSION_3_YML")],

  // Milestone 4
  [path.join(BASE_DIR, "_tutos", "D.351.1.scrum", "UA.351.11", "T.351.114", "sprint-planning-execution.md"), extractVar("TUTO_4_MD")],
  [path.join(BASE_DIR, "ua-lab", "scrum", "initiation-scrum", "sprint-planning-execution", "sprint-planning-execution.md"), extractVar("LAB_4_MD")],
  [path.join(BASE_DIR, "ua-lab", "scrum", "initiation-scrum", "sprint-planning-execution", "presentation-sprint-planning-execution.md"), extractVar("PRES_4_MD")],
  [path.join(BASE_DIR, "ua-lab", "scrum", "initiation-scrum", "sprint-planning-execution", "version.yml"), extractVar("VERSION_4_YML")],

  // Milestone 5
  [path.join(BASE_DIR, "_tutos", "D.351.1.scrum", "UA.351.11", "T.351.115", "revue-retrospective.md"), extractVar("TUTO_5_MD")],
  [path.join(BASE_DIR, "ua-lab", "scrum", "initiation-scrum", "revue-retrospective", "revue-retrospective.md"), extractVar("LAB_5_MD")],
  [path.join(BASE_DIR, "ua-lab", "scrum", "initiation-scrum", "revue-retrospective", "presentation-revue-retrospective.md"), extractVar("PRES_5_MD")],
  [path.join(BASE_DIR, "ua-lab", "scrum", "initiation-scrum", "revue-retrospective", "version.yml"), extractVar("VERSION_5_YML")],
];

for (const [filePath, content] of files) {
  writeUtf8NoBom(filePath, content);
}

console.log("\nSuccessfully generated all 16 files via Node.js!");
