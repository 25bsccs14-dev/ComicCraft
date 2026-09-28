# Phase 6: Project Testing

## Test Plan and Results
Run each test and fill in the actual result and date. Do not mark a test as passed until it has been performed.

| Test ID | Test case | Expected result | Actual result / status |
|---|---|---|---|
| TC01 | Start Uvicorn and open the home page | Home page loads | [To test] |
| TC02 | Submit a valid comic idea while Gemini is available | Comic story is displayed | [To test] |
| TC03 | Generate an illustration when image provider is available | Image is saved and displayed | [To test] |
| TC04 | Submit blank input | Validation or helpful response appears | [To test] |
| TC05 | Gemini quota is exceeded or API fails | Clear story-generation error/status appears | [To test] |
| TC06 | Image provider fails while story succeeds | Story remains visible and image failure is reported | [To test] |
| TC07 | Refresh/restart the local server | App can be started again using run instructions | [To test] |
| TC08 | Open a generated image's static URL | Image is served if the file exists | [To test] |

## Testing Procedure
1. Start the server using the instructions in Phase 5.
2. Open the local application.
3. Test with a short, harmless sample idea.
4. Observe the browser output and terminal logs.
5. Record pass/fail, date, and notes for each test.
6. Capture screenshots as evidence, ensuring no API secrets are visible.

## Known Limitations
- AI output may vary between requests.
- External services may impose rate limits, availability restrictions, or account-specific model access.
- Image generation requires a working provider, internet connection, and valid credentials.
- Generation time depends on the external services and network.

## Defect Log
| Date | Issue | Cause (if known) | Fix / current status |
|---|---|---|---|
| [Date] | Gemini API returned a 429 rate-limit error | Free-tier daily request limit was reached, according to the error message | Wait for quota reset; avoid repeated calls; verify current quota |
| [Date] | [Add any other observed issue] | [Cause] | [Fix/status] |
