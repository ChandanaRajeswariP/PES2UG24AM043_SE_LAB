# Lab 1 - Requirements Engineering and UML Use-Case Modelling

**Student:** Chandana Rajeswari P  
**Student ID:** PES2UG24AM043

## Scenario

Problem #39: Second-Hand Product Escrow Marketplace.

**GitHub repository:** [ChandanaRajeswariP/SE_LAB](https://github.com/ChandanaRajeswariP/SE_LAB)

## Deliverables

- `Requirements_Table.docx` - exactly five functional requirements (FR-001 to FR-005) and two nonfunctional requirements (NFR-001 and NFR-002), with IDs, type, description, priority, measurable acceptance criteria, rationale, and comments.
- `Use_Case_Diagram.pdf` - system boundary, actors, seven labeled use cases, one `<<include>>`, and one conditional `<<extend>>` relationship.
- `Use_Case_Diagram.svg` - editable vector source for the diagram.
- `Use_Case_Flow.docx` - editable one-page flow for UC-05, including preconditions, postconditions, main success scenario, and one alternate flow.
- `Use_Case_Flow.pdf` - one-page PDF version of the flow.

## Modeling assumptions

- Buyer and Inspection Agent are the scenario's stated actors. Seller, Payment Service, and Dispute Resolution Agent are added to model listing creation, payment processing, and dispute handling end to end; those roles are not separately specified in the scenario.
- Inspection outcomes are Pass or Fail. A seller payout requires a passing inspection and buyer sign-off. Failed or disputed cases remain held until an authorized resolution is recorded; the documents do not prescribe a refund policy.
- The two-second dispute-freeze threshold and 500 concurrent order actions make the supplied NFR-001 sample measurable. Confirm these target values with the instructor or stakeholder if the scenario is extended.
- Requirements-table comments are self-review clarifications. They do not claim that a peer critique took place; replace or supplement them with actual peer feedback if required in class.

## Cross-check against the lab instructions

| Lab requirement | Result |
| --- | --- |
| Exactly five FRs, numbered FR-001 to FR-005 | Complete |
| Exactly two NFRs, numbered NFR-001 and NFR-002 | Complete |
| Required requirement fields and measurable acceptance criteria | Complete |
| At least three actors and at least five use cases | Complete: five actors and seven use cases |
| One `<<include>>` and one `<<extend>>` relation | Complete |
| One-page use-case flow with preconditions, postconditions, main success, and alternate flow | Complete |
| Peer critique with another student | Requires the in-class peer exchange; no peer feedback was supplied |
| Push deliverables to the student's Lab 1 GitHub repository | Folder is prepared for repository submission; add it to the assigned repository |

## Push from PowerShell

If the repository is not already cloned, run:

```powershell
git clone https://github.com/ChandanaRajeswariP/SE_LAB.git "C:\Users\rajes\Downloads\SE_LAB"
Copy-Item -Recurse -LiteralPath "C:\Users\rajes\Downloads\PathSnap_Person2_Handoff\SE Lab 1" -Destination "C:\Users\rajes\Downloads\SE_LAB\SE Lab 1"
Set-Location "C:\Users\rajes\Downloads\SE_LAB"
git add -- "SE Lab 1"
git commit -m "Add Lab 1 requirements engineering submission"
git push -u origin HEAD
```

Git Credential Manager may prompt you to authenticate with GitHub during the push.
