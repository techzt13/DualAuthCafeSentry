# CAD workspace

Status: parametric FreeCAD macro source created; native FCStd files are generated
when the macro is run in FreeCAD. This environment does not have FreeCAD
installed, so no FCStd file is claimed to have been generated or checked here.

Run the macro:
1. Download `cad/create_enclosures.FCMacro`.
2. Open FreeCAD.
3. Choose File -> Open and select the macro, or run it from the FreeCAD Python console.
4. It creates editable Part Design source geometry as named parametric Part
   objects, saves Pod and Keyfob FCStd documents, and exports STEP/STL drafts.
5. Treat all generated geometry as DRAFT until inspected against real
   component drawings and the matching PCB.
