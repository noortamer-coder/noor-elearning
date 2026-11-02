# Noor E-Learning

Study dashboard for Noor, Pharmacy Year 2 at MSA University (Fall 2026).
Built from her MSA e-learning lecture PDFs: each course has lecture-by-lecture explanations and a quiz with answer explanations, filterable by lecture.

## Courses
- PHB221 Molecular Genetics (7 lectures, 22 questions)
- PHO221 Physiology & Pathophysiology (6 lectures, 28 questions)
- PHC223 Pharmaceutical Analytical Chemistry 3 (7 lectures, 20 questions)
- PHT231 Pharmaceutical Dosage Forms 1 (7 lectures, 27 questions)
- PHC213 Pharmaceutical Organic Chemistry 3 (6 lectures, 26 questions)

## Run
Open `index.html` in any browser. Progress (lectures studied, best scores) is saved in the browser.

## Add a lecture
Edit the `COURSES` array in `index.html`: add `{n, t, h}` to a course's `lectures` and `{l, q, o, a, e}` items to its `quiz`.
