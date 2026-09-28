# Phase 4: Project Planning

## 1. Work Plan
| Task | Planned activity | Status |
|---|---|---|
| 1 | Select project idea and define problem | Completed / verify |
| 2 | Identify requirements and tools | In progress / update |
| 3 | Design application flow and interface | In progress / update |
| 4 | Develop FastAPI backend and web form | Implemented / verify |
| 5 | Integrate Gemini story generation | Implemented; subject to quota and API availability |
| 6 | Integrate hosted illustration generation | Implemented; verify provider availability |
| 7 | Test success and failure cases | To be completed and recorded |
| 8 | Prepare documentation and GitHub repository | To be completed |
| 9 | Record and share project demonstration | To be completed |

## 2. Milestones
- M1: Problem statement and project scope finalized.
- M2: Requirements and design documented.
- M3: Basic web application runs locally.
- M4: AI story generation works.
- M5: Illustration generation and display work.
- M6: Testing, documentation, and demonstration completed.

## 3. Risks and Mitigation
| Risk | Mitigation |
|---|---|
| API rate limits or service outages | Show a useful error message; retry after quota reset; avoid repeated test requests |
| Model/provider changes | Record the configured model/provider and check current account availability |
| Internet connection failure | Explain that hosted generation requires internet access |
| API key accidentally uploaded | Keep `.env` ignored by Git; rotate any exposed key immediately |
| Generated image not displayed | Check server logs, saved image path, static route, and template image condition |

## 4. Progress Tracking
Update this file as work progresses. Replace status labels with the actual status and add dates or screenshots as evidence.

## Team Responsibilities

- Member 1: Rujutha G – Team Coordinator and Project Documentation. Responsible for coordinating team activities, maintaining project records, and preparing project reports.

- Member 2: Monisha R – Frontend Developer. Responsible for designing and developing the user interface using HTML and CSS.

- Member 3: Kalpana M – Backend Developer. Responsible for developing the backend using Python and FaAPI and connecting the web interface to the backend.

- Member 4: Vishnu Priya S – AI Integration Developer. Responsible for integrating AI services for comic story generation and illustration generation.

- Member 5: Umera A – Testing and Demonstration Lead. Responsible for testing project functionality, identifying errors, recording test results, and preparing the project demonstration.
