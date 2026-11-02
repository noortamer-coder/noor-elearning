# Noor E-Learning

Interactive study site for Noor, Pharmacy Year 2 at MSA University (Egypt).
Each module has an explanation tab and an auto-graded quiz with answer explanations.

## Modules
- Pharmacology · Module 1: Pharmacokinetics (ADME, Vd, clearance, half-life simulator, dosing)
- Pharmacology · Module 2: Pharmacodynamics (receptors, potency vs efficacy, antagonism, therapeutic index)

## Run
Open `index.html` in any browser. No build step or server needed.

## Add a module
Add an object to the `MODULES` array in `index.html` with `id`, `code`, `name`, `sub`, `lesson` (HTML) and `quiz` (questions with options `o`, answer index `a`, explanation `e`).
