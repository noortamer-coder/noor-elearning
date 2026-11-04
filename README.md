# Noor E-Learning

Study dashboard for Noor, Pharmacy Year 2 at MSA University (Fall 2026).
Built from her MSA e-learning lecture PDFs: each course has lecture-by-lecture explanations and a quiz with answer explanations, filterable by lecture.

## Courses
- PHB221 Molecular Genetics (7 lectures, 140 questions)
- PHO221 Physiology & Pathophysiology (6 lectures, 142 questions)
- PHC223 Pharmaceutical Analytical Chemistry 3 (7 lectures, 133 questions)
- PHT231 Pharmaceutical Dosage Forms 1 (7 lectures, 192 questions)
- PHC213 Pharmaceutical Organic Chemistry 3 (6 lectures, 137 questions)

## Run
Open `index.html` in any browser. Progress (lectures studied, best scores) is saved in the browser.

## Add a lecture
Edit the `COURSES` array in `index.html`: add `{n, t, h}` to a course's `lectures` and `{l, q, o, a, e}` items to its `quiz`.

## Project files
- `index.html` — the whole site (built output).
- `content/quiz/<course>.js` — extra quiz questions (`QX.<id>=[{l,q,o,a,e},...]`), 744 questions in total.
- `content/deep/<course>.js` — detailed English + Arabic lecture explanations (`DEEP[course][n]={en,ar}`).
- `build.py` — injects `content/` into `index.html`. Run `python3 build.py` after editing content.
- `questions/` — question bank PDFs (one per course) and `Noor_Quiz_Question_Bank.xlsx`.

## Status / next steps (as of 4 Nov 2026)
- Done: all 5 courses, 33 lectures, 744 quiz questions (shuffled, answers balanced A–D), PDF + spreadsheet question banks.
- Done: detailed EN+AR explanations for every lecture in all 5 courses (Physiology PHO221 lectures 3–6 added 4 Nov 2026).
- Live links: https://noortamer-coder.github.io/noor-elearning/ and mirror https://raw.githack.com/noortamer-coder/noor-elearning/main/index.html
