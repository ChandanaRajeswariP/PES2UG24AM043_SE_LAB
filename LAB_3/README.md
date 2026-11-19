# Lab 3 - Component Modelling and Architectural Pattern Selection

**Problem #39 - Second-Hand Product Escrow Marketplace**

This Lab 3 set carries the requirements and transaction flow from Chandana Rajeswari P's Lab 1 and Lab 2 submissions into a component model. It selects a layered modular monolith: one deployable application with explicit UI, access-control, domain, repository, and payment-adapter boundaries.

## Deliverables

| File | Description |
|---|---|
| Architecture_Justification.docx | Editable one-page report with architecture selection, alternatives, two reasons, security, performance, and trade-off. |
| Architecture_Justification.pdf | One-page PDF report matching the editable Word report. |
| Component_Diagram.png | UML component diagram for the marketplace architecture. |
| Component_Diagram.svg | Vector source for the same diagram. |

## Architecture and component responsibilities

| Component | Responsibility | Lab 1 trace |
|---|---|---|
| Marketplace Web Client | Presents listing, order, report review, and case-resolution flows. | FR-002 to FR-005 |
| Marketplace API & Access Control | Authenticated entry point; checks role and relationship to the requested order. | FR-003 to FR-005; NFR-002 |
| Listing & Order Management | Publishes and displays available listings; creates orders linked to buyer and listing. | FR-002, FR-003 |
| Inspection & Dispute Management | Stores assigned inspector reports, buyer sign-off/dispute decisions, and authorized resolutions. | FR-004, FR-005 |
| Escrow & Settlement | Holds and freezes funds; releases seller payout only when conditions hold. | FR-001, FR-005; NFR-001 |
| Transaction Repository | Stores listings, orders, reports, disputes, escrow ledger entries, and access/state audit events. | FR-001 to FR-005; NFR-002 |
| Payment Adapter | Sends authorized hold and payout instructions to the external payment service. | FR-001, FR-005 |

## Interface contracts

| Interface | Provider to consumer | Purpose |
|---|---|---|
| IMarketplaceAPI | Web Client to API & Access Control | Submit authenticated marketplace requests. |
| IListingOrder | API to Listing & Order Management | Publish listings, read availability, create orders. |
| IInspectionDispute | API to Inspection & Dispute Management | Submit reports, decisions, and authorized resolutions. |
| IEscrow | API to Escrow & Settlement | Record holds, freezes, and guarded payout requests. |
| IInspectionDecision | Inspection & Dispute Management to Escrow & Settlement | Provide report outcome, buyer sign-off, and active-dispute status. |
| IListingOrderData | Listing & Order Management to Transaction Repository | Persist listings and orders. |
| IInspectionDisputeData | Inspection & Dispute Management to Transaction Repository | Persist reports and dispute cases. |
| IEscrowLedger | Escrow & Settlement to Transaction Repository | Persist escrow state and settlement records. |
| IPaymentCommand | Escrow & Settlement to Payment Adapter | Send authorized hold or payout commands. |
| IPaymentProvider | Payment Adapter to external Payment Service | Execute an authorized payment operation and return its result. |

The dispute ticket and escrow freeze are designed to commit in one repository transaction. The design supports the Lab 1 target of a two-second p95 freeze at 500 concurrent order actions; deployment load testing is needed to confirm that target. Dispute outcomes remain with an authorized resolution; no refund policy is assumed.

Student: **Chandana Rajeswari P**  |  SRN: **PES2UG24AM043**
