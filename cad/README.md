# CAD workspace

Status: **editable parametric enclosure and reference-envelope macro exists; not yet run in FreeCAD.**

The source is [create_enclosures.FCMacro](create_enclosures.FCMacro). It creates:
- Parametric lower shell and lid for the Sentry Pod and Pocket Keyfob.
- Draft component reference envelopes inside the FreeCAD documents.
- Enclosure-only STEP/STL exports.
- Separate assembly-reference STEP/STL exports that include the transparent component envelopes.

## Run on macOS

1. Download or clone the repository to the Mac. Keep the repository folder somewhere stable, for example `~/Projects/DualAuthCafeSentry`.
2. Install and launch FreeCAD 0.21 or newer.
3. In FreeCAD, enable the Python console from **View → Panels → Python console**.
4. In the Python console, run the following command, changing the path if the repository is stored elsewhere:

```python
exec(open("/Users/REPLACE_WITH_MAC_USERNAME/Projects/DualAuthCafeSentry/cad/create_enclosures.FCMacro").read())
```

5. Wait for the two documents to build and save. The macro writes the results to:

```text
~/DualAuthCafeSentry-CAD/
```

6. Open `SentryPod.FCStd` and `PocketKeyfob.FCStd` from that output folder. Inspect the shell, lid and transparent reference solids. Save any later edits as a new revision rather than overwriting the source macro's draft assumptions.
7. Use the files ending in `_enclosure.step` / `_enclosure.stl` for enclosure-only geometry. Use `_assembly_reference.step` / `_assembly_reference.stl` to inspect the enclosure alongside the placeholder component envelopes.

## Important draft limits

- The macro does not create final USB-C, button, speaker, motor-lead, charging-port or fastener cutouts.
- It does not yet add screw bosses, lid joints, gasket grooves, snap fits, PCB standoffs or tolerance allowances.
- The Keyfob C3-Zero USB and antenna envelopes are explicitly placeholders. The antenna-end assumption and the USB-C side must be checked against the actual module orientation.
- The battery models are bare-cell reference envelopes, not protected packs.
- The Pod antenna, battery, and Keyfob motor/module/driver envelopes are not verified fits.
- The Keyfob carrier is 33 x 23 x 1.6 mm in the current PCB draft; the custom C3-Zero land pattern still has estimated pad size and row datum.
- All dimensions are millimetres. The current model is not a manufacturing release.

## Validation still required

1. Run the macro in FreeCAD and resolve any runtime errors.
2. Check body solids, wall/base thicknesses and lid mating geometry.
3. Compare every component envelope with the current datasheet and the exact physical parts.
4. Check USB access, antenna keepout, motor vibration coupling, battery insulation and charging-port access.
5. Add mounting, retention and fastening features.
6. Perform a physical fit check with printed parts and the actual PCB/components.
7. Export STEP/STL only after the geometry is inspected and revisioned.

No FCStd, STEP or STL file is claimed to have been generated or checked in this assistant environment.
