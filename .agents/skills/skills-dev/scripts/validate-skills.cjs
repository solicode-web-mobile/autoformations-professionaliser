#!/usr/bin/env node
/**
 * validate-skills.cjs — Validation statique déterministe des compétences IA
 * Vérifie localement les compétences du projet sous .agents/skills/
 */

const fs = require('fs');
const path = require('path');

function findSkillsDir() {
    const cwd = process.cwd();
    const localSkills = path.join(cwd, '.agents', 'skills');
    if (fs.existsSync(localSkills)) return localSkills;

    let current = cwd;
    while (current !== path.dirname(current)) {
        const candidate = path.join(current, '.agents', 'skills');
        if (fs.existsSync(candidate)) return candidate;
        current = path.dirname(current);
    }
    return null;
}

const skillsDir = findSkillsDir();

console.log('🔍 [VALIDATION SKILLS] Analyse des compétences locales');
if (!skillsDir) {
    console.error('❌ ERREUR : Répertoire .agents/skills/ introuvable.');
    process.exit(1);
}

console.log(`📂 Répertoire : ${skillsDir}\n`);

const entries = fs.readdirSync(skillsDir)
    .filter(f => {
        try { return fs.statSync(path.join(skillsDir, f)).isDirectory(); } catch { return false; }
    });

console.log(`ℹ️ ${entries.length} skill(s) détecté(s)\n`);

let errorsCount = 0;
const requiredYamlKeys = ['name:', 'description:', 'version:'];

entries.forEach(skillName => {
    const skillPath = path.join(skillsDir, skillName);
    const skillFile = path.join(skillPath, 'SKILL.md');
    const readmeFile = path.join(skillPath, 'README.md');

    // 1. Présence de SKILL.md
    if (!fs.existsSync(skillFile)) {
        console.error(`❌ ERREUR [${skillName}] : Fichier SKILL.md manquant !`);
        errorsCount++;
        return;
    }

    // 2. Présence de README.md
    if (!fs.existsSync(readmeFile)) {
        console.error(`❌ ERREUR [${skillName}] : Fichier README.md manquant (documentation obligatoire) !`);
        errorsCount++;
        return;
    }

    // 3. Encodage et frontmatter
    const buffer = fs.readFileSync(skillFile);
    const hasBom = buffer.length >= 3 && buffer[0] === 0xEF && buffer[1] === 0xBB && buffer[2] === 0xBF;
    if (hasBom) {
        console.error(`❌ ERREUR [${skillName}] : Encodage UTF-8 AVEC BOM détecté (strictement interdit) !`);
        errorsCount++;
    }

    const content = buffer.toString('utf8').replace(/^\uFEFF/, '').trimStart();
    if (!content.startsWith('---')) {
        console.error(`❌ ERREUR [${skillName}] : Frontmatter YAML manquant au début !`);
        errorsCount++;
        return;
    }

    const endOfYaml = content.indexOf('---', 3);
    if (endOfYaml === -1) {
        console.error(`❌ ERREUR [${skillName}] : Frontmatter YAML non fermé !`);
        errorsCount++;
        return;
    }

    const yamlHeader = content.substring(3, endOfYaml);
    const missingKeys = requiredYamlKeys.filter(k => !yamlHeader.includes(k));
    if (missingKeys.length > 0) {
        console.error(`❌ ERREUR [${skillName}] : Clés YAML obligatoires manquantes : ${missingKeys.join(', ')}`);
        errorsCount++;
        return;
    }

    console.log(`✅ [${skillName}] : SKILL.md et README.md conformes.`);
});

console.log('\n----------------------------------------');
if (errorsCount > 0) {
    console.error(`❌ VALIDATION ÉCHOUÉE : ${errorsCount} erreur(s) bloquante(s).`);
    process.exit(1);
} else {
    console.log(`✨ TOUS LES SKILLS SONT CONFORMES (0 erreur bloquante) !`);
    process.exit(0);
}
