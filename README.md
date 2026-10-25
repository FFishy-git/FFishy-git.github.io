# Siyu Chen's homepage

Live at https://ffishy-git.github.io/. Plain static HTML in an al-folio-style layout, so no build step is needed.
The source lives in the `website/` folder of the myCV repo and is published here with `website/deploy.sh`.

- `index.html`: all content (about, news, research highlights, publications, experience)
- `static/css/site.css`: styles, including light/dark themes
- `static/assets/CV.pdf`, `static/assets/img/photo.jpg`: the CV and photo

Publish from the myCV repo root:

```bash
./website/deploy.sh                    # sync and commit into build/pages, don't push
./website/deploy.sh --cv CV_detailed   # also rebuild CV.pdf from CV_detailed.tex
./website/deploy.sh --push             # publish
```
