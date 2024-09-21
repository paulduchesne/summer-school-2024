# Digital Archives 2024

Syllabus for Filmuniversität Babelsberg Digital Archiving Summer School 2024.

### Schedule

**Monday 2024-09-23**

| Session | Description | Tutor | Slides |
| --- | --- | --- | --- |
| 10:00 - 12:00 | Welcome & Introduction / Technical Assessment | | | 
|  | Lunch | | |
| 13:00 - 15:00 | Group 1: Scanning / Group 2: Digital Infrastructure | | |
|  | Coffee Break | | |
| 15:30 - 17:30 | Group Switch | | |

**Tuesday 2024-09-24**

| Session | Description | Tutor | Slides |
| --- | --- | --- | --- |
| 09:00 - 10:30 | Intro to Open Source, Command Line and FFmpeg | [@digitensions](https://github.com/digitensions), [@paulduchesne](https://github.com/paulduchesne) | [slides](slides/tuesday_01.html) | 
|  | Coffee Break | | | 
| 11:00 - 12:30 | Intro to Git, Python | [@paulduchesne](https://github.com/paulduchesne) | [slides](slides/tuesday_02.html) | 
|  | Lunch | |  | 
| 13:30 - 15:00 | Validating Files | [@digitensions](https://github.com/digitensions), [@paulduchesne](https://github.com/paulduchesne) | [slides](slides/tuesday_03.html)| 
|  | Coffee Break | | |
| 15:30 - 17:30 | Fixity and Storage | [@digitensions](https://github.com/digitensions), [@paulduchesne](https://github.com/paulduchesne) | [slides](slides/tuesday_04.html) | 

**Wednesday 2024-09-25**

| Session | Description | Tutor | Slides |
| --- | --- | --- | --- |
| 09:00 - 10:30 | FFmpeg Video Encoding, Filters and QC Tools | [@digitensions](https://github.com/digitensions) | [slides](slides/wednesday_01.html) | 
|  | Coffee Break | | | 
| 11:00 - 12:30 | RAWcooked and DCPs | [@digitensions](https://github.com/digitensions), [@paulduchesne](https://github.com/paulduchesne) | [slides](slides/wednesday_02.html)| 
|  | Lunch | | | 
| 13:30 - 15:00 | Extracting Content Metadata | [@paulduchesne](https://github.com/paulduchesne) | [slides](slides/wednesday_03.html)| 
|  | Coffee Break | | |
| 15:30 - 17:30 | External Connections | [@paulduchesne](https://github.com/paulduchesne) | [slides](slides/wednesday_04.html)| 

**Thursday 2024-09-26**

| Session | Description | Tutor | Slides |
| --- | --- | --- | --- |
| 09:00 - 10:30 | Python automation | [@paulduchesne](https://github.com/paulduchesne) | [slides](slides/thursday_01.html)| 
|  | Coffee Break | | | 
| 11:00 - 12:30 | FFmpeg filter output | [@digitensions](https://github.com/digitensions) | [slides](slides/thursday_02.html) | 
|  | Lunch | | | 
| 13:30 - 15:00 | Scaling Digital Preservation Workflows | [@digitensions](https://github.com/digitensions) | [slides](slides/thursday_03.html)| 
|  | Coffee Break | | |
| 15:30 - 17:30 | Multiprocessing, Logging, Containerisation, Orchestration | [@paulduchesne](https://github.com/paulduchesne) | [slides](slides/thursday_04.html) | 

**Friday 2024-09-27**

| Session | Description | Tutor | Slides |
| --- | --- | --- | --- |
| 10:00 - 11:00 | Course discussion | [@digitensions](https://github.com/digitensions), [@paulduchesne](https://github.com/paulduchesne) | [slides](slides/friday_01.html) | 
|  | Coffee Break | | | 
| 11:30 - 13:00 | Community and resources | [@digitensions](https://github.com/digitensions), [@paulduchesne](https://github.com/paulduchesne) | [slides](slides/friday_02.html) | 
|  | Lunch | | | 

### Media

The primary media used for the course is a film scan provided from the Bundesarchiv. This should placed within this repo as so:

```sh
/media/audio.wav
/media/0086400.dpx
/media/0086401.dpx
/media/0086402.dpx
...
```

### Slides

Slides can be deployed locally using Python from within the repository.

```sh
python3 -m http.server 8822
```

### Etherpad

Useful etherpad link: https://etherpad.wikimedia.org/p/digital_archives_2024
