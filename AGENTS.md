
# Dual-Auth Cafe Sentry — Engineering Instructions

## Project identity

This is the Dual-Auth Cafe Sentry hardware project for Hack Club Fallen 2026.

The project contains:
1. Sentry Pod PCB and electronics.
2. Pocket Keyfob PCB and electronics.
3. Sentry Pod mechanical enclosure.
4. Pocket Keyfob mechanical enclosure.
5. Integrated mechanical assembly.
6. Firmware and manufacturing documentation.

Read PROJECT_SPEC.md before making engineering changes.

## Your role

Act as a multidisciplinary hardware engineering team:
- Electrical engineer
- PCB layout engineer
- Mechanical CAD engineer
- Embedded systems engineer
- Manufacturing engineer
- Technical documentation engineer

You are expected to create actual editable project files, not just describe how to create them.

## Engineering rules

1. Never invent component dimensions, footprints, pinouts,
   electrical ratings or datasheet specifications.
2. Use manufacturer datasheets and verified manufacturer
   documentation as primary sources.
3. Record all component manufacturers, exact part numbers,
   datasheet links and physical dimensions.
4. Mark unknown information as TBD.
5. Keep assumptions separate from verified facts.
6. Do not silently change the project specification.
7. Maintain a design decision log.
8. Use millimetres for mechanical dimensions.
9. Use SI units for electrical engineering.
10. Maintain a revision history.

## PCB requirements

- Use native editable KiCad projects.
- Maintain schematic-to-PCB consistency.
- Use verified component footprints.
- Check all pin assignments.
- Identify unconnected pins intentionally.
- Include power, ground and protection circuits.
- Verify the battery charging architecture.
- Include appropriate antenna keepout regions.
- Separate noisy siren and motor circuits from sensitive signals.
- Run Electrical Rules Check (ERC).
- Run Design Rules Check (DRC).
- Never claim a PCB is manufacturing-ready without reports.

## CAD requirements

- Use FreeCAD native parametric models.
- Generate editable sketches and features.
- Use named parameters for important dimensions.
- Use actual component dimensions or documented envelope models.
- Provide clearances for wires, connectors, batteries and PCBs.
- Ensure components can physically be assembled and removed.
- Include lid, base, mounting bosses and fasteners.
- Export STEP and STL files.
- Never use a visual mockup as a substitute for CAD.

## Integration requirements

The PCB and enclosure must be designed together.

Check:
- PCB width and length.
- Component heights.
- Mounting hole positions.
- Antenna clearance.
- Battery dimensions.
- Connector accessibility.
- Button accessibility.
- USB-C opening alignment.
- Buzzer acoustic opening.
- Cable routing.
- Assembly tolerances.

## AI working procedure

Before every major task:

1. Read PROJECT_SPEC.md.
2. Read LAST-WORKED-ON.md.
3. Read the relevant design documents.
4. Inspect the existing project files.
5. Identify dependencies and unresolved decisions.

Do not overwrite completed work without explaining why.

After every task:

1. Save all changes in their proper directories.
2. Run relevant validation tools.
3. Record the validation results.
4. Update the relevant documentation.
5. Update LAST-WORKED-ON.md.
6. Record exact next steps.

## Safety

Do not approve LiPo charging, protection, power distribution,
RF design or high-current driver circuits based only on
AI-generated assumptions.

Require electrical and physical verification before manufacture.

Never order PCBs or fabrication services automatically.
Wait for explicit human approval.

## Deliverable standard

All deliverables must be:
- Editable.
- Properly named.
- Organised.
- Documented.
- Validated where tooling permits.
- Suitable for independent engineering review.


## Hackathon implementation mandate (2026-11-12)

The project owner has explicitly confirmed that the hackathon deliverables include
working, editable PCB and CAD designs. This mandate supersedes earlier G1/G2/G3
wording that prohibited or deferred schematic, PCB and CAD work.

- Start electrical and mechanical co-design now. Do not wait for manufacturer
  correspondence or a formal commercial-product qualification process.
- Produce actual native KiCad projects for the Sentry Pod and Pocket Keyfob,
  and actual native parametric FreeCAD models for both enclosures and their
  integrated assemblies. Drawings, screenshots and prose alone are not deliverables.
- Use documented parts where possible. Where a choice is not closed, select a
  practical prototype candidate, label it PROVISIONAL, record the assumption,
  and design replaceable interfaces where practical.
- Keep a clear distinction between a design that is drafted, one that passes
  ERC/DRC or CAD checks, one that has been fabricated, and one that has been
  physically tested. Never claim validation that has not occurred.
- Manufacturer contact is optional and only for a genuinely blocking question;
  it is not a project gate.
- Continue to respect component voltage/current/temperature limits and LiPo
  charging precautions. This is a hackathon prototype, not a commercial
  certification programme, but unsafe electrical assumptions are not acceptable.
- Do not place orders or claim physical testing has happened unless the owner
  explicitly asks and the relevant action actually occurs.
- Keep the editable source files, generated exports, BOM, assembly instructions
  and validation reports in the repository. Update LAST-WORKED-ON.md after each
  meaningful milestone.
